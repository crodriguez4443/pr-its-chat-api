# Weather (WX)

Road weather information systems, mobile weather observations. (also: winter maintenance, anti-icing, de-icing, snow removal, weather responsive management)

## Service Packages in This Architecture

### Weather Services
*RWIS, mobile observations, weather alerts (also: road weather information system, ESS, environmental sensor station, weather station, road weather station)*

- [Service Package mpSH1_WX01-02(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_WX01-02(Municipal))
- [Service Package mpSH1_WX01-02(MunicipalTrafficDPW)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_WX01-02(MunicipalTrafficDPW))
- [Service Package mpSH28_WX01-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH28_WX01-01(PRHTA))
- [Service Package mpSH112_WX02-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH112_WX02-01(PRHTA))
- [Service Package mpSH1_WX02-04(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_WX02-04(Municipal))
- [Service Package mpSH1_WX02-04(MunicipalTrafficDPW)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_WX02-04(MunicipalTrafficDPW))

## Key Elements (15 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Metropistas TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Website](https://www.consystec.com/pr2026proto/web/element.htm?id=52) | Existing | Municipal Traffic and Maintenance Agencies |
| [National Weather Service](https://www.consystec.com/pr2026proto/web/element.htm?id=96) | Existing | NOAA |
| [Other Municipal Public Works Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=172) | Planned | Municipal Traffic and Maintenance Agencies |
| [PR Police Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=106) | Existing | PR Police |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Travelers Vehicles](https://www.consystec.com/pr2026proto/web/element.htm?id=252) | Existing | Private Travelers |
| [Private Weather Information Provider](https://www.consystec.com/pr2026proto/web/element.htm?id=189) | Existing | Private Weather Information Provider |
| [Private Weather Support Services System](https://www.consystec.com/pr2026proto/web/element.htm?id=248) | Existing | Private Weather Information Provider |
| [State Emergency Management Agency Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=102) | Existing | State Emergency Management Agency |

## Related Functional Requirements (21 found)

- [Functional Requirements: TMC Roadway Warning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=108)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=177)
- [Functional Requirements: MCM Winter Maintenance Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=214)
- [Functional Requirements: Emergency Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=225)
- [Functional Requirements: TIC Road Weather Advisories and Warnings](https://www.consystec.com/pr2026proto/web/funreq.htm?id=32)
- [Functional Requirements: Roadway Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=33)
- [Functional Requirements: MCV Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=34)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=35)
- [Functional Requirements: TMC Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=36)
- [Functional Requirements: MCM Environmental Information Processing](https://www.consystec.com/pr2026proto/web/funreq.htm?id=38)
- [Functional Requirements: TMC Road Weather Advisories and Warnings](https://www.consystec.com/pr2026proto/web/funreq.htm?id=428)
- [Functional Requirements: Transit Center Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=431)
- [Functional Requirements: TIC Traveler Information Broadcast](https://www.consystec.com/pr2026proto/web/funreq.htm?id=55)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=83)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el104)

*... and 6 more*

## Deployment Guidance

When planning a deployment in Weather:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

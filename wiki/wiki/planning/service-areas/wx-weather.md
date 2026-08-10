# Weather (WX)

Road weather information systems, mobile weather observations. (also: winter maintenance, anti-icing, de-icing, snow removal, weather responsive management)

## Service Packages in This Architecture

### Weather Services
*RWIS, mobile observations, weather alerts, spot weather impact warning, roadway micro-prediction (also: road weather information system, ESS, environmental sensor station, weather station, road weather station)*

- [Service Package WX01-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX01-01(PRHTA))
- [Service Package WX01-02(Municipal)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX01-02(Municipal))
- [Service Package WX01-02(MunicipalTrafficDPW)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX01-02(MunicipalTrafficDPW))
- [Service Package WX02-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-01(PRHTA))
- [Service Package WX02-02(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-02(PRHTA))
- [Service Package WX02-03(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-03(PRHTA))
- [Service Package WX02-04(Municipal)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-04(Municipal))
- [Service Package WX02-04(MunicipalTrafficDPW)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-04(MunicipalTrafficDPW))
- [Service Package WX02-05(Municipal)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-05(Municipal))
- [Service Package WX02-05(MunicipalTrafficDPW)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX02-05(MunicipalTrafficDPW))
- [Service Package WX03-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX03-01(PRHTA))
- [Service Package WX03-02(Municipal)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX03-02(Municipal))
- [Service Package WX03-02(MunicipalTrafficDPW)](https://www.consystec.com/pr/web/spinstance.htm?id=/WX03-02(MunicipalTrafficDPW))

## Key Elements (19 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Metropistas TMC](https://www.consystec.com/pr/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal Public Works Dispatch](https://www.consystec.com/pr/web/element.htm?id=47) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal SMCs](https://www.consystec.com/pr/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Website](https://www.consystec.com/pr/web/element.htm?id=52) | Existing | Municipal Traffic and Maintenance Agencies |
| [National Weather Service](https://www.consystec.com/pr/web/element.htm?id=96) | Existing | NOAA |
| [Other Municipal Public Works Dispatch](https://www.consystec.com/pr/web/element.htm?id=172) | Planned | Municipal Traffic and Maintenance Agencies |
| [PR Police Dispatch](https://www.consystec.com/pr/web/element.htm?id=106) | Existing | PR Police |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Information Services](https://www.consystec.com/pr/web/element.htm?id=115) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Maintenance and Construction Systems](https://www.consystec.com/pr/web/element.htm?id=128) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Public Information Office](https://www.consystec.com/pr/web/element.htm?id=153) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Travelers Vehicles](https://www.consystec.com/pr/web/element.htm?id=252) | Existing | Private Travelers |
| [Private Weather Information Provider](https://www.consystec.com/pr/web/element.htm?id=189) | Existing | Private Weather Information Provider |
| [Private Weather Support Services System](https://www.consystec.com/pr/web/element.htm?id=248) | Existing | Private Weather Information Provider |
| [State Emergency Management Agency Systems](https://www.consystec.com/pr/web/element.htm?id=102) | Existing | State Emergency Management Agency |

## Interfaces (25 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Interface: Municipal ITS Field Equipment → environmental sensor data → Municipal Public Works Dispatch (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor data interface](https://www.consystec.com/pr/web/interface.htm?id=45-47)
- Interface: Municipal ITS Field Equipment → environmental sensor data → Municipal SMCs (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor data interface](https://www.consystec.com/pr/web/interface.htm?id=45-51)
- Interface: Municipal Public Works Dispatch → environmental sensor control → Municipal ITS Field Equipment (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor control interface](https://www.consystec.com/pr/web/interface.htm?id=45-47)
- Interface: Municipal SMCs → environmental sensor control → Municipal ITS Field Equipment (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor control interface](https://www.consystec.com/pr/web/interface.htm?id=45-51)
- Interface: Municipal SMCs → road network conditions → Municipal Public Works Dispatch (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=47-51)
- Interface: Municipal SMCs → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=51-115)
- Interface: National Weather Service → environmental conditions data status → PRHTA Information Services — [environmental conditions data status interface](https://www.consystec.com/pr/web/interface.htm?id=96-115)
- Interface: National Weather Service → qualified environmental conditions data → Municipal Public Works Dispatch — [qualified environmental conditions data interface](https://www.consystec.com/pr/web/interface.htm?id=47-96)
- Interface: National Weather Service → qualified environmental conditions data → Municipal SMCs — [qualified environmental conditions data interface](https://www.consystec.com/pr/web/interface.htm?id=51-96)
- Interface: PRHTA ITS Field Devices → environmental sensor data → PRHTA TMC (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor data interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA ITS Field Devices → environmental sensor data → Private Weather Support Services System (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor data interface](https://www.consystec.com/pr/web/interface.htm?id=248-264)
- Interface: PRHTA ITS Field Devices → variable speed limit status → PRHTA TMC (US: NTCIP Message Sign - SNMPv1) — [variable speed limit status interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA Information Services → road network environmental situation data → Municipal SMCs ((None-Data) - Secure Internet (ITS)) — [road network environmental situation data interface](https://www.consystec.com/pr/web/interface.htm?id=51-115)
- Interface: PRHTA Information Services → road network environmental situation data → PRHTA TMC ((None-Data) - Secure Internet (ITS)) — [road network environmental situation data interface](https://www.consystec.com/pr/web/interface.htm?id=115-154)
- Interface: PRHTA Information Services → road weather advisories → Private Travelers Vehicles (TPEG2 - Wide Area Broadcast) — [road weather advisories interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: PRHTA Public Information Office → road weather information_ud → PRHTA Information Services — [road weather information_ud interface](https://www.consystec.com/pr/web/interface.htm?id=115-153)
- Interface: PRHTA TMC → environmental sensor control → PRHTA ITS Field Devices (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor control interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA TMC → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=115-154)
- Interface: PRHTA TMC → variable speed limit control → PRHTA ITS Field Devices (US: NTCIP Message Sign - SNMPv1) — [variable speed limit control interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: Private Travelers Vehicles → vehicle environmental data → PRHTA Information Services (US: SAE Weather Info - Secure Wireless Internet (ITS)) — [vehicle environmental data interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: Private Weather Information Provider → qualified environmental conditions data → Municipal Public Works Dispatch — [qualified environmental conditions data interface](https://www.consystec.com/pr/web/interface.htm?id=47-189)
- Interface: Private Weather Information Provider → qualified environmental conditions data → Municipal SMCs — [qualified environmental conditions data interface](https://www.consystec.com/pr/web/interface.htm?id=51-189)
- Interface: Private Weather Support Services System → environmental sensor control → PRHTA ITS Field Devices (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor control interface](https://www.consystec.com/pr/web/interface.htm?id=248-264)
- Interface: Private Weather Support Services System → qualified environmental conditions data → PRHTA Information Services ((None-Data) - Secure Internet (ITS)) — [qualified environmental conditions data interface](https://www.consystec.com/pr/web/interface.htm?id=115-248)
- Interface: Private Weather Support Services System → qualified environmental conditions data → PRHTA TMC ((None-Data) - Secure Internet (ITS)) — [qualified environmental conditions data interface](https://www.consystec.com/pr/web/interface.htm?id=154-248)

## Related Functional Requirements (29 found)

- [Functional Requirements: TMC Roadway Warning](https://www.consystec.com/pr/web/funreq.htm?id=108)
- [Functional Requirements: EV On-Board Incident Management Communication](https://www.consystec.com/pr/web/funreq.htm?id=149)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr/web/funreq.htm?id=177)
- [Functional Requirements: MCM Winter Maintenance Management](https://www.consystec.com/pr/web/funreq.htm?id=214)
- [Functional Requirements: Emergency Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=225)
- [Functional Requirements: Vehicle Traveler Information Reception](https://www.consystec.com/pr/web/funreq.htm?id=23)
- [Functional Requirements: TIC Road Weather Advisories and Warnings](https://www.consystec.com/pr/web/funreq.htm?id=32)
- [Functional Requirements: Roadway Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=33)
- [Functional Requirements: MCV Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=34)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr/web/funreq.htm?id=35)
- [Functional Requirements: TMC Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=36)
- [Functional Requirements: MCM Environmental Information Processing](https://www.consystec.com/pr/web/funreq.htm?id=38)
- [Functional Requirements: TMC Road Weather Advisories and Warnings](https://www.consystec.com/pr/web/funreq.htm?id=428)
- [Functional Requirements: Transit Center Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=431)
- [Functional Requirements: TIC Traveler Information Broadcast](https://www.consystec.com/pr/web/funreq.htm?id=55)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr/web/funreq.htm?id=83)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr/web/funreq.htm?id=_el104)
- [Functional Requirements: MCV Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=_el127)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr/web/funreq.htm?id=_el153)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr/web/funreq.htm?id=_el172)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr/web/funreq.htm?id=_el177)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr/web/funreq.htm?id=_el248)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr/web/funreq.htm?id=_el254)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr/web/funreq.htm?id=_el263)
- [Functional Requirements: Vehicle Traveler Information Reception](https://www.consystec.com/pr/web/funreq.htm?id=_el275)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr/web/funreq.htm?id=_el47)
- [Functional Requirements: MCV Environmental Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=_el48)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr/web/funreq.htm?id=_el52)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr/web/funreq.htm?id=_el68)

## Deployment Guidance

When planning a deployment in Weather:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

# Commercial Vehicle Operations (CVO)

Freight credentialing, electronic screening, HAZMAT tracking, oversize/overweight permits. (also: hazardous material, hazardous materials, dangerous goods, HAZMAT routing)

## Service Packages in This Architecture

### Commercial Vehicle Operations
*Credentialing, screening, HAZMAT, fleet management, freight administration, road weather, drayage optimization, HAZMAT security, driver logs, intelligent access, speed compliance, international border (also: hazardous material, hazardous materials, dangerous goods, HAZMAT routing; also: winter maintenance, anti-icing, de-icing, snow removal, weather responsive management)*

- [Service Package CVO01-01](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO01-01)
- [Service Package CVO03-01](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO03-01)
- [Service Package CVO03-02](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO03-02)
- [Service Package CVO04-01](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO04-01)
- [Service Package CVO04-02](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO04-02)
- [Service Package CVO05-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO05-01(PRHTA))
- [Service Package CVO07-01](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO07-01)
- [Service Package CVO07-02](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO07-02)
- [Service Package CVO08-01](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO08-01)
- [Service Package CVO09-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO09-01(PRHTA))
- [Service Package CVO10-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO10-01(PRHTA))
- [Service Package CVO12-01](https://www.consystec.com/pr/web/spinstance.htm?id=/CVO12-01)

## Key Elements (28 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [FMCSA Safety and Fitness Electronic Record (SAFER)](https://www.consystec.com/pr/web/element.htm?id=205) | Existing | Federal Motor Carrier Safety Administration |
| [IFTA Clearinghouse](https://www.consystec.com/pr/web/element.htm?id=64) | Existing | IFTA |
| [IRP Clearinghouse](https://www.consystec.com/pr/web/element.htm?id=67) | Existing | American Association of Motor Vehicle Administrato |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal SMCs](https://www.consystec.com/pr/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [National Weather Service](https://www.consystec.com/pr/web/element.htm?id=96) | Existing | NOAA |
| [PR Accident Reporting System](https://www.consystec.com/pr/web/element.htm?id=1) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR CVIEW System](https://www.consystec.com/pr/web/element.htm?id=99) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR CVO Credentials Interface](https://www.consystec.com/pr/web/element.htm?id=114) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR E-Citation Process](https://www.consystec.com/pr/web/element.htm?id=57) | Planned | PR Police Commercial Vehicle Enforcement |
| [PR Electronic Bypass Stations](https://www.consystec.com/pr/web/element.htm?id=58) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR Electronic Permitting System](https://www.consystec.com/pr/web/element.htm?id=105) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR Motor Carrier Database](https://www.consystec.com/pr/web/element.htm?id=54) | Existing | PR Department of Motor Vehicles |
| [PR Police CVO Enforcement](https://www.consystec.com/pr/web/element.htm?id=277) | Planned | PR Police Commercial Vehicle Enforcement |
| [PR Police Dispatch](https://www.consystec.com/pr/web/element.htm?id=106) | Existing | PR Police |
| [PR Roadside Safety Inspection System](https://www.consystec.com/pr/web/element.htm?id=204) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR Safetynet](https://www.consystec.com/pr/web/element.htm?id=206) | Existing | PR Police Commercial Vehicle Enforcement |
| [PR Weigh Stations](https://www.consystec.com/pr/web/element.htm?id=81) | Existing | PR Police Commercial Vehicle Enforcement |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Information Services](https://www.consystec.com/pr/web/element.htm?id=115) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Truck Parking Management Systems](https://www.consystec.com/pr/web/element.htm?id=263) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Fleet Management Systems](https://www.consystec.com/pr/web/element.htm?id=61) | Existing | Private Motor Carriers |
| [Private Freight Shipping System](https://www.consystec.com/pr/web/element.htm?id=63) | Existing | Private Motor Carriers |
| [Private Motor Carrier Vehicles](https://www.consystec.com/pr/web/element.htm?id=41) | Existing | Private Motor Carriers |
| [Private Travelers Personal Computing Devices](https://www.consystec.com/pr/web/element.htm?id=187) | Existing | Private Travelers |
| [Private Weather Support Services System](https://www.consystec.com/pr/web/element.htm?id=248) | Existing | Private Weather Information Provider |
| [State Emergency Management Agency Systems](https://www.consystec.com/pr/web/element.htm?id=102) | Existing | State Emergency Management Agency |

## Interfaces (96 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Interface: FMCSA Safety and Fitness Electronic Record (SAFER) → accident report → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [accident report interface](https://www.consystec.com/pr/web/interface.htm?id=205-277)
- Interface: FMCSA Safety and Fitness Electronic Record (SAFER) → commercial vehicle archive data → PR Motor Carrier Database (Data for Distribution (TBD) - OMG DDS) — [commercial vehicle archive data interface](https://www.consystec.com/pr/web/interface.htm?id=54-205)
- Interface: FMCSA Safety and Fitness Electronic Record (SAFER) → commercial vehicle violation notification → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [commercial vehicle violation notification interface](https://www.consystec.com/pr/web/interface.htm?id=205-277)
- Interface: Municipal Public Safety Dispatch → emergency plan coordination → Municipal SMCs ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=51-89)
- Interface: Municipal Public Safety Dispatch → emergency plan coordination → PRHTA TMC ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=89-154)
- Interface: Municipal Public Safety Dispatch → emergency route request → Municipal SMCs ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency route request interface](https://www.consystec.com/pr/web/interface.htm?id=51-89)
- Interface: Municipal Public Safety Dispatch → emergency route request → PRHTA TMC ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency route request interface](https://www.consystec.com/pr/web/interface.htm?id=89-154)
- Interface: Municipal SMCs → emergency plan coordination → Municipal Public Safety Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=51-89)
- Interface: Municipal SMCs → emergency plan coordination → PR Police Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=51-106)
- Interface: Municipal SMCs → emergency plan coordination → State Emergency Management Agency Systems ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=51-102)
- Interface: Municipal SMCs → emergency routes → Municipal Public Safety Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency routes interface](https://www.consystec.com/pr/web/interface.htm?id=51-89)
- Interface: Municipal SMCs → emergency routes → PR Police Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency routes interface](https://www.consystec.com/pr/web/interface.htm?id=51-106)
- Interface: Municipal SMCs → emergency routes → State Emergency Management Agency Systems ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency routes interface](https://www.consystec.com/pr/web/interface.htm?id=51-102)
- Interface: Municipal SMCs → road network conditions → Municipal Public Safety Dispatch (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=51-89)
- Interface: Municipal SMCs → road network conditions → PR Police Dispatch (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=51-106)
- Interface: Municipal SMCs → road network conditions → State Emergency Management Agency Systems (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=51-102)
- Interface: PR Accident Reporting System → accident report → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [accident report interface](https://www.consystec.com/pr/web/interface.htm?id=1-277)
- Interface: PR Accident Reporting System → commercial vehicle violation notification → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [commercial vehicle violation notification interface](https://www.consystec.com/pr/web/interface.htm?id=1-277)
- Interface: PR Accident Reporting System → safety inspection report → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [safety inspection report interface](https://www.consystec.com/pr/web/interface.htm?id=1-99)
- Interface: PR CVIEW System → accident report → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [accident report interface](https://www.consystec.com/pr/web/interface.htm?id=99-277)
- Interface: PR CVIEW System → commercial vehicle archive data → PR Motor Carrier Database (Data for Distribution (TBD) - OMG DDS) — [commercial vehicle archive data interface](https://www.consystec.com/pr/web/interface.htm?id=54-99)
- Interface: PR CVIEW System → commercial vehicle violation notification → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [commercial vehicle violation notification interface](https://www.consystec.com/pr/web/interface.htm?id=99-277)
- Interface: PR CVIEW System → cv driver record → Private Fleet Management Systems ((None-Data) - Secure Internet (ITS)) — [cv driver record interface](https://www.consystec.com/pr/web/interface.htm?id=61-99)
- Interface: PR CVIEW System → route restrictions → Private Fleet Management Systems ((None-Data) - Secure Internet (ITS)) — [route restrictions interface](https://www.consystec.com/pr/web/interface.htm?id=61-99)
- Interface: PR CVO Credentials Interface → commercial vehicle permit → Private Fleet Management Systems ((None-Data) - Secure Internet (ITS)) — [commercial vehicle permit interface](https://www.consystec.com/pr/web/interface.htm?id=61-114)
- Interface: PR Electronic Bypass Stations → daily site activity data → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [daily site activity data interface](https://www.consystec.com/pr/web/interface.htm?id=58-99)
- Interface: PR Electronic Bypass Stations → electronic screening request → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [electronic screening request interface](https://www.consystec.com/pr/web/interface.htm?id=41-58)
- Interface: PR Electronic Bypass Stations → pass/pull-in → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - WAVE IPv6) — [pass/pull-in interface](https://www.consystec.com/pr/web/interface.htm?id=41-58)
- Interface: PR Electronic Bypass Stations → screening event record → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [screening event record interface](https://www.consystec.com/pr/web/interface.htm?id=41-58)
- Interface: PR Electronic Permitting System → commercial vehicle check station status_ud → PRHTA TMC — [commercial vehicle check station status_ud interface](https://www.consystec.com/pr/web/interface.htm?id=105-154)
- Interface: PR Motor Carrier Database → archive status → FMCSA Safety and Fitness Electronic Record (SAFER) (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr/web/interface.htm?id=54-205)
- Interface: PR Motor Carrier Database → archive status → PR CVIEW System (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr/web/interface.htm?id=54-99)
- Interface: PR Police Dispatch → emergency plan coordination → Municipal SMCs ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=51-106)
- Interface: PR Police Dispatch → emergency plan coordination → PRHTA TMC ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=106-154)
- Interface: PR Police Dispatch → emergency route request → Municipal SMCs ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency route request interface](https://www.consystec.com/pr/web/interface.htm?id=51-106)
- Interface: PR Police Dispatch → emergency route request → PRHTA TMC ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency route request interface](https://www.consystec.com/pr/web/interface.htm?id=106-154)
- Interface: PR Roadside Safety Inspection System → accident report → FMCSA Safety and Fitness Electronic Record (SAFER) ((None-Data) - Secure Internet (ITS)) — [accident report interface](https://www.consystec.com/pr/web/interface.htm?id=204-205)
- Interface: PR Roadside Safety Inspection System → citation → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [citation interface](https://www.consystec.com/pr/web/interface.htm?id=99-204)
- Interface: PR Roadside Safety Inspection System → citation → PR E-Citation Process ((None-Data) - Secure Internet (ITS)) — [citation interface](https://www.consystec.com/pr/web/interface.htm?id=57-204)
- Interface: PR Roadside Safety Inspection System → commercial vehicle violation notification → FMCSA Safety and Fitness Electronic Record (SAFER) ((None-Data) - Secure Internet (ITS)) — [commercial vehicle violation notification interface](https://www.consystec.com/pr/web/interface.htm?id=204-205)
- Interface: PR Roadside Safety Inspection System → daily site activity data → FMCSA Safety and Fitness Electronic Record (SAFER) ((None-Data) - Secure Internet (ITS)) — [daily site activity data interface](https://www.consystec.com/pr/web/interface.htm?id=204-205)
- Interface: PR Roadside Safety Inspection System → daily site activity data → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [daily site activity data interface](https://www.consystec.com/pr/web/interface.htm?id=99-204)
- Interface: PR Roadside Safety Inspection System → pass/pull-in → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - WAVE IPv6) — [pass/pull-in interface](https://www.consystec.com/pr/web/interface.htm?id=41-204)
- Interface: PR Roadside Safety Inspection System → safety inspection record → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [safety inspection record interface](https://www.consystec.com/pr/web/interface.htm?id=41-204)
- Interface: PR Roadside Safety Inspection System → safety inspection report → FMCSA Safety and Fitness Electronic Record (SAFER) ((None-Data) - Secure Internet (ITS)) — [safety inspection report interface](https://www.consystec.com/pr/web/interface.htm?id=204-205)
- Interface: PR Roadside Safety Inspection System → safety inspection report → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [safety inspection report interface](https://www.consystec.com/pr/web/interface.htm?id=99-204)
- Interface: PR Roadside Safety Inspection System → safety inspection request → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [safety inspection request interface](https://www.consystec.com/pr/web/interface.htm?id=41-204)
- Interface: PR Safetynet → accident report → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [accident report interface](https://www.consystec.com/pr/web/interface.htm?id=206-277)
- Interface: PR Safetynet → commercial vehicle violation notification → PR Police CVO Enforcement ((None-Data) - Secure Internet (ITS)) — [commercial vehicle violation notification interface](https://www.consystec.com/pr/web/interface.htm?id=206-277)
- Interface: PR Weigh Stations → commercial vehicle violation notification → PR Electronic Permitting System ((None-Data) - Secure Internet (ITS)) — [commercial vehicle violation notification interface](https://www.consystec.com/pr/web/interface.htm?id=81-105)
- Interface: PR Weigh Stations → daily site activity data → PR Electronic Permitting System ((None-Data) - Secure Internet (ITS)) — [daily site activity data interface](https://www.consystec.com/pr/web/interface.htm?id=81-105)
- Interface: PR Weigh Stations → electronic screening request → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [electronic screening request interface](https://www.consystec.com/pr/web/interface.htm?id=41-81)
- Interface: PR Weigh Stations → pass/pull-in → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - WAVE IPv6) — [pass/pull-in interface](https://www.consystec.com/pr/web/interface.htm?id=41-81)
- Interface: PR Weigh Stations → request tag data → Private Motor Carrier Vehicles ((None-Data) - WAVE WSMP) — [request tag data interface](https://www.consystec.com/pr/web/interface.htm?id=41-81)
- Interface: PR Weigh Stations → screening event record → Private Motor Carrier Vehicles (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [screening event record interface](https://www.consystec.com/pr/web/interface.htm?id=41-81)
- Interface: PRHTA ITS Field Devices → roadway dynamic signage status → PRHTA TMC (US: NTCIP Message Sign - SNMPv1) — [roadway dynamic signage status interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA ITS Field Devices → traffic images → PRHTA TMC — [traffic images interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA Information Services → road network environmental situation data → Private Fleet Management Systems ((None-Data) - Secure Internet (ITS)) — [road network environmental situation data interface](https://www.consystec.com/pr/web/interface.htm?id=61-115)
- Interface: PRHTA Information Services → road weather advisories → Private Fleet Management Systems (US: TMDD - NTCIP Messaging) — [road weather advisories interface](https://www.consystec.com/pr/web/interface.htm?id=61-115)
- Interface: PRHTA TMC → emergency plan coordination → Municipal Public Safety Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=89-154)
- Interface: PRHTA TMC → emergency plan coordination → PR Police Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=106-154)
- Interface: PRHTA TMC → emergency plan coordination → State Emergency Management Agency Systems ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=102-154)
- Interface: PRHTA TMC → emergency routes → Municipal Public Safety Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency routes interface](https://www.consystec.com/pr/web/interface.htm?id=89-154)
- Interface: PRHTA TMC → emergency routes → PR Police Dispatch ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency routes interface](https://www.consystec.com/pr/web/interface.htm?id=106-154)
- Interface: PRHTA TMC → emergency routes → State Emergency Management Agency Systems ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency routes interface](https://www.consystec.com/pr/web/interface.htm?id=102-154)
- Interface: PRHTA TMC → road network conditions → Municipal Public Safety Dispatch (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=89-154)
- Interface: PRHTA TMC → road network conditions → PR Police Dispatch (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=106-154)
- Interface: PRHTA TMC → road network conditions → State Emergency Management Agency Systems (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=102-154)
- Interface: PRHTA TMC → roadway dynamic signage data → PRHTA ITS Field Devices (US: NTCIP Message Sign - SNMPv1) — [roadway dynamic signage data interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA TMC → video surveillance control → PRHTA ITS Field Devices (US: NTCIP Video Switches - SNMPv1) — [video surveillance control interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA Truck Parking Management Systems → parking availability → Private Travelers Personal Computing Devices (Data for Distribution (TBD) - OMG DDS over Wireless) — [parking availability interface](https://www.consystec.com/pr/web/interface.htm?id=187-263)
- Interface: PRHTA Truck Parking Management Systems → parking availibility_ud → PRHTA ITS Field Devices — [parking availibility_ud interface](https://www.consystec.com/pr/web/interface.htm?id=263-264)
- Interface: PRHTA Truck Parking Management Systems → parking availibility_ud → PRHTA TMC — [parking availibility_ud interface](https://www.consystec.com/pr/web/interface.htm?id=154-263)
- Interface: Private Fleet Management Systems → audit data → PR CVO Credentials Interface ((None-Data) - Secure Internet (ITS)) — [audit data interface](https://www.consystec.com/pr/web/interface.htm?id=61-114)
- Interface: Private Fleet Management Systems → credential application → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [credential application interface](https://www.consystec.com/pr/web/interface.htm?id=61-99)
- Interface: Private Fleet Management Systems → credential application → PR CVO Credentials Interface ((None-Data) - Secure Internet (ITS)) — [credential application interface](https://www.consystec.com/pr/web/interface.htm?id=61-114)
- Interface: Private Fleet Management Systems → cv repair status → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [cv repair status interface](https://www.consystec.com/pr/web/interface.htm?id=61-99)
- Interface: Private Fleet Management Systems → fleet to driver update → Private Motor Carrier Vehicles ((None-Data) - Secure Wireless Internet (ITS)) — [fleet to driver update interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Fleet Management Systems → request for permit → PR CVIEW System ((None-Data) - Secure Internet (ITS)) — [request for permit interface](https://www.consystec.com/pr/web/interface.htm?id=61-99)
- Interface: Private Fleet Management Systems → request for permit → PR CVO Credentials Interface ((None-Data) - Secure Internet (ITS)) — [request for permit interface](https://www.consystec.com/pr/web/interface.htm?id=61-114)
- Interface: Private Fleet Management Systems → road weather advisories → Private Motor Carrier Vehicles (TPEG2 - Secure Wireless Internet (ITS)) — [road weather advisories interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Fleet Management Systems → tax filing → PR CVO Credentials Interface ((None-Data) - Secure Internet (ITS)) — [tax filing interface](https://www.consystec.com/pr/web/interface.htm?id=61-114)
- Interface: Private Motor Carrier Vehicles → commercial vehicle location data → Private Fleet Management Systems (US: SAE Other J2735 - Secure Wireless Internet (ITS)) — [commercial vehicle location data interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Motor Carrier Vehicles → driver to fleet request → Private Fleet Management Systems ((None-Data) - Secure Wireless Internet (ITS)) — [driver to fleet request interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Motor Carrier Vehicles → on-board safety data → Private Fleet Management Systems (US: SAE J3067 (J2735 SE) - Secure Wireless Internet (ITS)) — [on-board safety data interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Motor Carrier Vehicles → on-board vehicle data → Private Fleet Management Systems ((None-Data) - Secure Wireless Internet (ITS)) — [on-board vehicle data interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Motor Carrier Vehicles → safety inspection record → PR Roadside Safety Inspection System (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [safety inspection record interface](https://www.consystec.com/pr/web/interface.htm?id=41-204)
- Interface: Private Motor Carrier Vehicles → screening event record → PR Electronic Bypass Stations (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [screening event record interface](https://www.consystec.com/pr/web/interface.htm?id=41-58)
- Interface: Private Motor Carrier Vehicles → screening event record → PR Weigh Stations (US: SAE J3067 (J2735 SE) - Local Unicast Wireless (1609.2)) — [screening event record interface](https://www.consystec.com/pr/web/interface.htm?id=41-81)
- Interface: Private Motor Carrier Vehicles → tag data → PR Weigh Stations ((None-Data) - Local Unicast Wireless (1609.2)) — [tag data interface](https://www.consystec.com/pr/web/interface.htm?id=41-81)
- Interface: Private Motor Carrier Vehicles → trip log → Private Fleet Management Systems ((None-Data) - Secure Wireless Internet (ITS)) — [trip log interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: Private Motor Carrier Vehicles → vehicle environmental data → Private Fleet Management Systems (US: SAE Weather Info - Secure Wireless Internet (ITS)) — [vehicle environmental data interface](https://www.consystec.com/pr/web/interface.htm?id=41-61)
- Interface: State Emergency Management Agency Systems → emergency plan coordination → Municipal SMCs ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=51-102)
- Interface: State Emergency Management Agency Systems → emergency plan coordination → PRHTA TMC ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency plan coordination interface](https://www.consystec.com/pr/web/interface.htm?id=102-154)
- Interface: State Emergency Management Agency Systems → emergency route request → Municipal SMCs ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency route request interface](https://www.consystec.com/pr/web/interface.htm?id=51-102)
- Interface: State Emergency Management Agency Systems → emergency route request → PRHTA TMC ((None-Data) - Guaranteed Secure Internet (ITS)) — [emergency route request interface](https://www.consystec.com/pr/web/interface.htm?id=102-154)

## Related Functional Requirements (29 found)

- [Functional Requirements: CV On-Board Cargo Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=145)
- [Functional Requirements: CVAC Information Exchange](https://www.consystec.com/pr/web/funreq.htm?id=185)
- [Functional Requirements: CVAC Safety and Security Administration](https://www.consystec.com/pr/web/funreq.htm?id=186)
- [Functional Requirements: CVCE Electronic Screening](https://www.consystec.com/pr/web/funreq.htm?id=187)
- [Functional Requirements: CV On-Board Electronic Screening Support](https://www.consystec.com/pr/web/funreq.htm?id=189)
- [Functional Requirements: Fleet Administration](https://www.consystec.com/pr/web/funreq.htm?id=194)
- [Functional Requirements: CV On-Board Trip Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=195)
- [Functional Requirements: TIC Freight-Specific Travel Planning](https://www.consystec.com/pr/web/funreq.htm?id=196)
- [Functional Requirements: CV On-Board Safety and Security](https://www.consystec.com/pr/web/funreq.htm?id=197)
- [Functional Requirements: CVCE Citation and Accident Electronic Recording](https://www.consystec.com/pr/web/funreq.htm?id=199)
- [Functional Requirements: CVAC Credentials and Taxes Administration](https://www.consystec.com/pr/web/funreq.htm?id=201)
- [Functional Requirements: Emergency Commercial Vehicle Response](https://www.consystec.com/pr/web/funreq.htm?id=226)
- [Functional Requirements: Fleet Credentials and Taxes Management and Reporting](https://www.consystec.com/pr/web/funreq.htm?id=316)
- [Functional Requirements: CVCE Weigh-In-Motion](https://www.consystec.com/pr/web/funreq.htm?id=347)
- [Functional Requirements: TMC Incident Detection](https://www.consystec.com/pr/web/funreq.htm?id=378)
- [Functional Requirements: Fleet Maintenance Management](https://www.consystec.com/pr/web/funreq.htm?id=451)
- [Functional Requirements: Freight Administration and Management](https://www.consystec.com/pr/web/funreq.htm?id=5)
- [Functional Requirements: CVAC Credentials and Taxes Administration](https://www.consystec.com/pr/web/funreq.htm?id=_el1)
- [Functional Requirements: CVAC Credentials and Taxes Administration](https://www.consystec.com/pr/web/funreq.htm?id=_el105)
- [Functional Requirements: CVAC Credentials and Taxes Administration](https://www.consystec.com/pr/web/funreq.htm?id=_el114)
- [Functional Requirements: CVCE Citation and Accident Electronic Recording](https://www.consystec.com/pr/web/funreq.htm?id=_el204)
- [Functional Requirements: CVAC Information Exchange](https://www.consystec.com/pr/web/funreq.htm?id=_el205)
- [Functional Requirements: CVAC Information Exchange](https://www.consystec.com/pr/web/funreq.htm?id=_el206)
- [Functional Requirements: CV On-Board Cargo Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=_el41)
- [Functional Requirements: CVAC Information Exchange](https://www.consystec.com/pr/web/funreq.htm?id=_el57)
- [Functional Requirements: CVCE Citation and Accident Electronic Recording](https://www.consystec.com/pr/web/funreq.htm?id=_el58)
- [Functional Requirements: Fleet Administration](https://www.consystec.com/pr/web/funreq.htm?id=_el61)
- [Functional Requirements: CVCE Citation and Accident Electronic Recording](https://www.consystec.com/pr/web/funreq.htm?id=_el81)
- [Functional Requirements: CVAC Credentials and Taxes Administration](https://www.consystec.com/pr/web/funreq.htm?id=_el99)

## Deployment Guidance

When planning a deployment in Commercial Vehicle Operations:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

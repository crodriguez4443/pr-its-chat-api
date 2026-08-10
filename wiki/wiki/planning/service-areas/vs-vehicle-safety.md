# Vehicle Safety (VS)

V2V safety, automated driving, platooning, collision avoidance. (also: vehicle to vehicle, V2X)

## Service Packages in This Architecture

### Vehicle Safety & Automation
*V2V, automated vehicles, platooning, collision avoidance, autonomous vehicle safety, basic safety, situational awareness, special vehicle alert, stop sign gap assist, road weather alert, restricted lane warnings, cooperative adaptive cruise control, METR, VRU clustering (also: vehicle to vehicle, V2X; also: self-driving, automated driving, ADS, ADAS, advanced driver assistance; also: winter maintenance, anti-icing, de-icing, snow removal, weather responsive management)*

- [Service Package VS07-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/VS07-01(PRHTA))
- [Service Package VS08-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/VS08-01(PRHTA))
- [Service Package VS09-01(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/VS09-01(PRHTA))
- [Service Package VS12-01(Municipal)](https://www.consystec.com/pr/web/spinstance.htm?id=/VS12-01(Municipal))
- [Service Package VS12-02(PRHTA)](https://www.consystec.com/pr/web/spinstance.htm?id=/VS12-02(PRHTA))

## Key Elements (11 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Municipal Connected Vehicle Equipment](https://www.consystec.com/pr/web/element.htm?id=261) | Planned | Municipal Traffic and Maintenance Agencies |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal SMCs](https://www.consystec.com/pr/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Other Vehicle OBEs](https://www.consystec.com/pr/web/element.htm?id=255) | Planned | Private Travelers |
| [PRHTA Connected Vehicle Equipment](https://www.consystec.com/pr/web/element.htm?id=268) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Information Services](https://www.consystec.com/pr/web/element.htm?id=115) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Third Party Information Providers](https://www.consystec.com/pr/web/element.htm?id=254) | Existing | Private Traffic Data Providers |
| [Private Travelers Personal Computing Devices](https://www.consystec.com/pr/web/element.htm?id=187) | Existing | Private Travelers |
| [Private Travelers Vehicles](https://www.consystec.com/pr/web/element.htm?id=252) | Existing | Private Travelers |

## Interfaces (49 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Interface: Municipal Connected Vehicle Equipment → intersection geometry → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [intersection geometry interface](https://www.consystec.com/pr/web/interface.htm?id=252-261)
- Interface: Municipal Connected Vehicle Equipment → intersection safety application status → Municipal SMCs ((None-Data) - Secure Internet (ITS)) — [intersection safety application status interface](https://www.consystec.com/pr/web/interface.htm?id=51-261)
- Interface: Municipal Connected Vehicle Equipment → intersection safety warning → Private Travelers Vehicles (US: SAE Other J2735 - WAVE WSMP) — [intersection safety warning interface](https://www.consystec.com/pr/web/interface.htm?id=252-261)
- Interface: Municipal Connected Vehicle Equipment → intersection status → Private Travelers Personal Computing Devices (US: SAE Signal Control Messages - WAVE WSMP) — [intersection status interface](https://www.consystec.com/pr/web/interface.htm?id=187-261)
- Interface: Municipal Connected Vehicle Equipment → intersection status → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [intersection status interface](https://www.consystec.com/pr/web/interface.htm?id=252-261)
- Interface: Municipal Connected Vehicle Equipment → proxied personal location → Private Travelers Vehicles ((None-Data) - WAVE WSMP) — [proxied personal location interface](https://www.consystec.com/pr/web/interface.htm?id=252-261)
- Interface: Municipal Connected Vehicle Equipment → signal service request → Municipal ITS Field Equipment (US: NTCIP Signal Priority - SNMPv3/TLS) — [signal service request interface](https://www.consystec.com/pr/web/interface.htm?id=45-261)
- Interface: Municipal ITS Field Equipment → intersection control status → Municipal Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [intersection control status interface](https://www.consystec.com/pr/web/interface.htm?id=45-261)
- Interface: Municipal ITS Field Equipment → mixed use crossing status → Municipal Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [mixed use crossing status interface](https://www.consystec.com/pr/web/interface.htm?id=45-261)
- Interface: Municipal ITS Field Equipment → mixed use safety warning status → Municipal SMCs (US: NTCIP Traffic Signal - SNMPv1) — [mixed use safety warning status interface](https://www.consystec.com/pr/web/interface.htm?id=45-51)
- Interface: Municipal SMCs → intersection safety application info → Municipal Connected Vehicle Equipment ((None-Data) - Secure Internet (ITS)) — [intersection safety application info interface](https://www.consystec.com/pr/web/interface.htm?id=51-261)
- Interface: Municipal SMCs → mixed use safety warning control → Municipal ITS Field Equipment (US: NTCIP Traffic Signal - SNMPv1) — [mixed use safety warning control interface](https://www.consystec.com/pr/web/interface.htm?id=45-51)
- Interface: Other Vehicle OBEs → vehicle control event → Private Travelers Vehicles (US: SAE Basic Safety Messages - WAVE WSMP) — [vehicle control event interface](https://www.consystec.com/pr/web/interface.htm?id=252-255)
- Interface: Other Vehicle OBEs → vehicle location and motion → Private Travelers Vehicles (US: SAE Basic Safety Messages - WAVE WSMP) — [vehicle location and motion interface](https://www.consystec.com/pr/web/interface.htm?id=252-255)
- Interface: PRHTA Connected Vehicle Equipment → intersection geometry → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [intersection geometry interface](https://www.consystec.com/pr/web/interface.htm?id=252-268)
- Interface: PRHTA Connected Vehicle Equipment → intersection safety application status → PRHTA TMC ((None-Data) - Secure Internet (ITS)) — [intersection safety application status interface](https://www.consystec.com/pr/web/interface.htm?id=154-268)
- Interface: PRHTA Connected Vehicle Equipment → intersection safety warning → Private Travelers Vehicles (US: SAE Other J2735 - WAVE WSMP) — [intersection safety warning interface](https://www.consystec.com/pr/web/interface.htm?id=252-268)
- Interface: PRHTA Connected Vehicle Equipment → intersection status → Private Travelers Personal Computing Devices (US: SAE Signal Control Messages - WAVE WSMP) — [intersection status interface](https://www.consystec.com/pr/web/interface.htm?id=187-268)
- Interface: PRHTA Connected Vehicle Equipment → intersection status → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [intersection status interface](https://www.consystec.com/pr/web/interface.htm?id=252-268)
- Interface: PRHTA Connected Vehicle Equipment → proxied personal location → Private Travelers Vehicles ((None-Data) - WAVE WSMP) — [proxied personal location interface](https://www.consystec.com/pr/web/interface.htm?id=252-268)
- Interface: PRHTA Connected Vehicle Equipment → signal service request → PRHTA ITS Field Devices (US: NTCIP Signal Priority - SNMPv3/TLS) — [signal service request interface](https://www.consystec.com/pr/web/interface.htm?id=264-268)
- Interface: PRHTA ITS Field Devices → environmental sensor data → PRHTA TMC (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor data interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA ITS Field Devices → intersection control status → PRHTA Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [intersection control status interface](https://www.consystec.com/pr/web/interface.htm?id=264-268)
- Interface: PRHTA ITS Field Devices → mixed use crossing status → PRHTA Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [mixed use crossing status interface](https://www.consystec.com/pr/web/interface.htm?id=264-268)
- Interface: PRHTA ITS Field Devices → mixed use safety warning status → PRHTA TMC (US: NTCIP Traffic Signal - SNMPv1) — [mixed use safety warning status interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA ITS Field Devices → roadway dynamic signage status → PRHTA TMC (US: NTCIP Message Sign - SNMPv1) — [roadway dynamic signage status interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA Information Services → lane closure warning_ud → Private Travelers Vehicles — [lane closure warning_ud interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: PRHTA Information Services → queue warning information_ud → Private Travelers Vehicles — [queue warning information_ud interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: PRHTA Information Services → road network environmental situation data → PRHTA TMC ((None-Data) - Secure Internet (ITS)) — [road network environmental situation data interface](https://www.consystec.com/pr/web/interface.htm?id=115-154)
- Interface: PRHTA Information Services → road weather advisories → Private Travelers Vehicles (TPEG2 - Wide Area Broadcast) — [road weather advisories interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: PRHTA Information Services → speed warning_ud → Private Travelers Vehicles — [speed warning_ud interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: PRHTA TMC → environmental sensor control → PRHTA ITS Field Devices (US: NTCIP Environmental Sensors - SNMPv1) — [environmental sensor control interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA TMC → intersection safety application info → PRHTA Connected Vehicle Equipment ((None-Data) - Secure Internet (ITS)) — [intersection safety application info interface](https://www.consystec.com/pr/web/interface.htm?id=154-268)
- Interface: PRHTA TMC → mixed use safety warning control → PRHTA ITS Field Devices (US: NTCIP Traffic Signal - SNMPv1) — [mixed use safety warning control interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA TMC → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr/web/interface.htm?id=115-154)
- Interface: PRHTA TMC → roadway dynamic signage data → PRHTA ITS Field Devices (US: NTCIP Message Sign - SNMPv1) — [roadway dynamic signage data interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: PRHTA TMC → speed monitoring control → PRHTA ITS Field Devices (US: NTCIP Warning Device - SNMPv1) — [speed monitoring control interface](https://www.consystec.com/pr/web/interface.htm?id=154-264)
- Interface: Private Third Party Information Providers → queue warning information_ud → Private Travelers Vehicles — [queue warning information_ud interface](https://www.consystec.com/pr/web/interface.htm?id=252-254)
- Interface: Private Travelers Personal Computing Devices → personal location → Municipal Connected Vehicle Equipment (US: SAE VRU Messages - WAVE WSMP) — [personal location interface](https://www.consystec.com/pr/web/interface.htm?id=187-261)
- Interface: Private Travelers Personal Computing Devices → personal location → PRHTA Connected Vehicle Equipment (US: SAE VRU Messages - WAVE WSMP) — [personal location interface](https://www.consystec.com/pr/web/interface.htm?id=187-268)
- Interface: Private Travelers Personal Computing Devices → personal signal service request → Municipal Connected Vehicle Equipment (US: SAE Other J2735 - Local Unicast Wireless (1609.2)) — [personal signal service request interface](https://www.consystec.com/pr/web/interface.htm?id=187-261)
- Interface: Private Travelers Personal Computing Devices → personal signal service request → PRHTA Connected Vehicle Equipment (US: SAE Other J2735 - Local Unicast Wireless (1609.2)) — [personal signal service request interface](https://www.consystec.com/pr/web/interface.htm?id=187-268)
- Interface: Private Travelers Vehicles → intersection infringement info → Municipal Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [intersection infringement info interface](https://www.consystec.com/pr/web/interface.htm?id=252-261)
- Interface: Private Travelers Vehicles → intersection infringement info → PRHTA Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [intersection infringement info interface](https://www.consystec.com/pr/web/interface.htm?id=252-268)
- Interface: Private Travelers Vehicles → vehicle control event → Other Vehicle OBEs (US: SAE Basic Safety Messages - WAVE WSMP) — [vehicle control event interface](https://www.consystec.com/pr/web/interface.htm?id=252-255)
- Interface: Private Travelers Vehicles → vehicle environmental data → PRHTA Information Services (US: SAE Weather Info - Secure Wireless Internet (ITS)) — [vehicle environmental data interface](https://www.consystec.com/pr/web/interface.htm?id=115-252)
- Interface: Private Travelers Vehicles → vehicle location and motion → Municipal Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [vehicle location and motion interface](https://www.consystec.com/pr/web/interface.htm?id=252-261)
- Interface: Private Travelers Vehicles → vehicle location and motion → Other Vehicle OBEs (US: SAE Basic Safety Messages - WAVE WSMP) — [vehicle location and motion interface](https://www.consystec.com/pr/web/interface.htm?id=252-255)
- Interface: Private Travelers Vehicles → vehicle location and motion → PRHTA Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [vehicle location and motion interface](https://www.consystec.com/pr/web/interface.htm?id=252-268)

## Related Functional Requirements (7 found)

- [Functional Requirements: Vehicle Intersection Warning](https://www.consystec.com/pr/web/funreq.htm?id=1)
- [Functional Requirements: Transit Center Paratransit Operations](https://www.consystec.com/pr/web/funreq.htm?id=165)
- [Functional Requirements: CV On-Board Trip Monitoring](https://www.consystec.com/pr/web/funreq.htm?id=195)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr/web/funreq.htm?id=39)
- [Functional Requirements: Transit Center Fixed-Route Operations](https://www.consystec.com/pr/web/funreq.htm?id=390)
- [Functional Requirements: Personal Pedestrian Safety](https://www.consystec.com/pr/web/funreq.htm?id=66)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr/web/funreq.htm?id=_el252)

## Deployment Guidance

When planning a deployment in Vehicle Safety:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

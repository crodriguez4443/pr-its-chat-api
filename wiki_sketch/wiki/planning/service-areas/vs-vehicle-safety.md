# Vehicle Safety (VS)

V2V safety, automated driving, platooning, collision avoidance. (also: vehicle to vehicle, V2X)

## Service Packages in This Architecture

### Vehicle Safety & Automation
*V2V, automated vehicles, platooning, collision avoidance, autonomous vehicle safety, basic safety, situational awareness, special vehicle alert, stop sign gap assist, road weather alert, restricted lane warnings, cooperative adaptive cruise control, METR, VRU clustering (also: vehicle to vehicle, V2X; also: self-driving, automated driving, ADS, ADAS, advanced driver assistance; also: winter maintenance, anti-icing, de-icing, snow removal, weather responsive management)*

- [mpSH3_VS07-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS07-01(PRHTA))
- [mpSH5_VS07-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS07-01(PRHTA))
- [mpSH3_VS08-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS08-01(PRHTA))
- [mpSH5_VS08-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS08-01(PRHTA))
- [mpSH83_VS08-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH83_VS08-01(PRHTA))
- [mpSH3_VS09-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS09-01(PRHTA))
- [mpSH5_VS09-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS09-01(PRHTA))
- [mpSH1_VS12-01(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_VS12-01(Municipal))
- [mpSH3_VS12-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS12-02(PRHTA))
- [mpSH5_VS12-01(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS12-01(Municipal))
- [mpSH5_VS12-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS12-02(PRHTA))

## Key Elements (9 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Municipal Connected Vehicle Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=261) | Planned | Municipal Traffic and Maintenance Agencies |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Other Vehicle OBEs](https://www.consystec.com/pr2026proto/web/element.htm?id=255) | Planned | Private Travelers |
| [PRHTA Connected Vehicle Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=268) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Travelers Personal Computing Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=187) | Existing | Private Travelers |
| [Private Travelers Vehicles](https://www.consystec.com/pr2026proto/web/element.htm?id=252) | Existing | Private Travelers |

## Interfaces (41 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Municipal Connected Vehicle Equipment → intersection geometry → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-261)
- Municipal Connected Vehicle Equipment → intersection safety application status → Municipal SMCs ((None-Data) - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-261)
- Municipal Connected Vehicle Equipment → intersection safety warning → Private Travelers Vehicles (US: SAE Other J2735 - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-261)
- Municipal Connected Vehicle Equipment → intersection status → Private Travelers Personal Computing Devices (US: SAE Signal Control Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-261)
- Municipal Connected Vehicle Equipment → intersection status → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-261)
- Municipal Connected Vehicle Equipment → proxied personal location → Private Travelers Vehicles ((None-Data) - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-261)
- Municipal Connected Vehicle Equipment → signal service request → Municipal ITS Field Equipment (US: NTCIP Signal Priority - SNMPv3/TLS) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-261)
- Municipal ITS Field Equipment → intersection control status → Municipal Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-261)
- Municipal ITS Field Equipment → mixed use crossing status → Municipal Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-261)
- Municipal ITS Field Equipment → mixed use safety warning status → Municipal SMCs (US: NTCIP Traffic Signal - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-51)
- Municipal SMCs → intersection safety application info → Municipal Connected Vehicle Equipment ((None-Data) - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-261)
- Municipal SMCs → mixed use safety warning control → Municipal ITS Field Equipment (US: NTCIP Traffic Signal - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-51)
- Other Vehicle OBEs → vehicle control event → Private Travelers Vehicles (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-255)
- Other Vehicle OBEs → vehicle location and motion → Private Travelers Vehicles — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-255)
- PRHTA Connected Vehicle Equipment → intersection geometry → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-268)
- PRHTA Connected Vehicle Equipment → intersection safety application status → PRHTA TMC ((None-Data) - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-268)
- PRHTA Connected Vehicle Equipment → intersection safety warning → Private Travelers Vehicles (US: SAE Other J2735 - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-268)
- PRHTA Connected Vehicle Equipment → intersection status → Private Travelers Personal Computing Devices (US: SAE Signal Control Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-268)
- PRHTA Connected Vehicle Equipment → intersection status → Private Travelers Vehicles (US: SAE Signal Control Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-268)
- PRHTA Connected Vehicle Equipment → proxied personal location → Private Travelers Vehicles ((None-Data) - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-268)
- PRHTA Connected Vehicle Equipment → signal service request → PRHTA ITS Field Devices (US: NTCIP Signal Priority - SNMPv3/TLS) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=264-268)
- PRHTA ITS Field Devices → environmental sensor data → PRHTA TMC (US: NTCIP Environmental Sensors - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA ITS Field Devices → intersection control status → PRHTA Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=264-268)
- PRHTA ITS Field Devices → mixed use crossing status → PRHTA Connected Vehicle Equipment (US: NTCIP Traffic Signal - SNMPv3/TLS) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=264-268)
- PRHTA ITS Field Devices → mixed use safety warning status → PRHTA TMC (US: NTCIP Traffic Signal - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA ITS Field Devices → roadway dynamic signage status → PRHTA TMC (US: NTCIP Message Sign - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → environmental sensor control → PRHTA ITS Field Devices (US: NTCIP Environmental Sensors - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → intersection safety application info → PRHTA Connected Vehicle Equipment ((None-Data) - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-268)
- PRHTA TMC → mixed use safety warning control → PRHTA ITS Field Devices (US: NTCIP Traffic Signal - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → roadway dynamic signage data → PRHTA ITS Field Devices (US: NTCIP Message Sign - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → speed monitoring control → PRHTA ITS Field Devices (US: NTCIP Warning Device - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- Private Travelers Personal Computing Devices → personal location → Municipal Connected Vehicle Equipment (US: SAE VRU Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-261)
- Private Travelers Personal Computing Devices → personal location → PRHTA Connected Vehicle Equipment (US: SAE VRU Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-268)
- Private Travelers Personal Computing Devices → personal signal service request → Municipal Connected Vehicle Equipment (US: SAE Other J2735 - Local Unicast Wireless (1609.2)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-261)
- Private Travelers Personal Computing Devices → personal signal service request → PRHTA Connected Vehicle Equipment (US: SAE Other J2735 - Local Unicast Wireless (1609.2)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-268)
- Private Travelers Vehicles → intersection infringement info → Municipal Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-261)
- Private Travelers Vehicles → intersection infringement info → PRHTA Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-268)
- Private Travelers Vehicles → vehicle control event → Other Vehicle OBEs (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-255)
- Private Travelers Vehicles → vehicle location and motion → Municipal Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-261)
- Private Travelers Vehicles → vehicle location and motion → Other Vehicle OBEs (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-255)
- Private Travelers Vehicles → vehicle location and motion → PRHTA Connected Vehicle Equipment (US: SAE Basic Safety Messages - WAVE WSMP) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=252-268)

## Related Functional Requirements (7 found)

- [Functional Requirements: Vehicle Intersection Warning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=1)
- [Functional Requirements: Transit Center Paratransit Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=165)
- [Functional Requirements: CV On-Board Trip Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=195)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=39)
- [Functional Requirements: Transit Center Fixed-Route Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=390)
- [Functional Requirements: Personal Pedestrian Safety](https://www.consystec.com/pr2026proto/web/funreq.htm?id=66)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el252)


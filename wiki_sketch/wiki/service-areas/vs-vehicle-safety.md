# Vehicle Safety (VS)

V2V safety, automated driving, platooning, collision avoidance. (also: vehicle to vehicle, V2X)

## Service Packages in This Architecture

### Vehicle Safety & Automation
*V2V, automated vehicles, platooning, collision avoidance (also: vehicle to vehicle, V2X; also: autonomous vehicle, self-driving, automated driving, ADS, ADAS)*

- [Service Package mpSH3_VS08-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS08-01(PRHTA))
- [Service Package mpSH5_VS08-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS08-01(PRHTA))
- [Service Package mpSH83_VS08-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH83_VS08-01(PRHTA))
- [Service Package mpSH3_VS09-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS09-01(PRHTA))
- [Service Package mpSH5_VS09-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS09-01(PRHTA))
- [Service Package mpSH1_VS12-01(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_VS12-01(Municipal))
- [Service Package mpSH3_VS12-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_VS12-02(PRHTA))
- [Service Package mpSH5_VS12-01(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_VS12-01(Municipal))

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

## Related Functional Requirements (7 found)

- [Functional Requirements: Vehicle Intersection Warning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=1)
- [Functional Requirements: Transit Center Paratransit Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=165)
- [Functional Requirements: CV On-Board Trip Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=195)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=39)
- [Functional Requirements: Transit Center Fixed-Route Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=390)
- [Functional Requirements: Personal Pedestrian Safety](https://www.consystec.com/pr2026proto/web/funreq.htm?id=66)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el252)

## Deployment Guidance

When planning a deployment in Vehicle Safety:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

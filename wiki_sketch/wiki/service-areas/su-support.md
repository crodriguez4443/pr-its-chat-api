# Support (SU)

Device management, mapping, location services, communications infrastructure.

## Service Packages in This Architecture

### Support Services
*Map management, device management, cybersecurity, communications*

- [Service Package mpSH112_SU03-02(Metropistas)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH112_SU03-02(Metropistas))
- [Service Package mpSH1_SU03-03(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_SU03-03(Municipal))
- [Service Package mpSH1_SU03-03(MunicipalTrafficDPW)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_SU03-03(MunicipalTrafficDPW))

## Key Elements (11 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Metropistas Communications Infrastructure Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=285) | Planned | Metropistas |
| [Metropistas ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=280) | Planned | Metropistas |
| [Metropistas TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Infrastructure Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=267) | Planned | Municipal Traffic and Maintenance Agencies |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Local Transit Vehicles](https://www.consystec.com/pr2026proto/web/element.htm?id=71) | Existing | Municipal Local Transit Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [PRHTA Communications Infrastructure Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=265) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |

## Related Functional Requirements (43 found)

- [Functional Requirements: Vehicle Intersection Warning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=1)
- [Functional Requirements: Emergency Routing](https://www.consystec.com/pr2026proto/web/funreq.htm?id=121)
- [Functional Requirements: Transit Vehicle Passenger Counting](https://www.consystec.com/pr2026proto/web/funreq.htm?id=127)
- [Functional Requirements: Transit Center Passenger Counting](https://www.consystec.com/pr2026proto/web/funreq.htm?id=129)
- [Functional Requirements: CV On-Board Cargo Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=145)
- [Functional Requirements: Emergency Incident Command](https://www.consystec.com/pr2026proto/web/funreq.htm?id=148)
- [Functional Requirements: Emergency Dispatch](https://www.consystec.com/pr2026proto/web/funreq.htm?id=150)
- [Functional Requirements: Transit Vehicle Schedule Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=152)
- [Functional Requirements: Parking Area Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=162)
- [Functional Requirements: Transit Vehicle On-Board Trip Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=164)
- [Functional Requirements: Vehicle Situation Data Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=179)
- [Functional Requirements: CV On-Board Trip Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=195)
- [Functional Requirements: CV On-Board Safety and Security](https://www.consystec.com/pr2026proto/web/funreq.htm?id=197)
- [Functional Requirements: MCV Winter Maintenance](https://www.consystec.com/pr2026proto/web/funreq.htm?id=215)
- [Functional Requirements: Emergency Commercial Vehicle Response](https://www.consystec.com/pr2026proto/web/funreq.htm?id=226)

*... and 28 more*

## Deployment Guidance

When planning a deployment in Support:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

# Sustainable Transport (ST)

Congestion pricing, transit incentives, emissions management. (also: road pricing, cordon pricing, value pricing, dynamic pricing, tolling for congestion)

## Service Packages in This Architecture

### Sustainable Transport
*Congestion pricing, transit incentives, alternative fuel support (also: road pricing, cordon pricing, value pricing, dynamic pricing, tolling for congestion)*

- [Service Package mpSH109_ST05-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH109_ST05-01(PRHTA))
- [Service Package mpSH109_ST05-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH109_ST05-02(PRHTA))
- [Service Package mpSH1_ST05-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_ST05-02(PRHTA))

## Key Elements (7 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Electric Vehicle Charging Stations](https://www.consystec.com/pr2026proto/web/element.htm?id=270) | Planned | Electric Vehicle Charging Organizations |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Website](https://www.consystec.com/pr2026proto/web/element.htm?id=52) | Existing | Municipal Traffic and Maintenance Agencies |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Travelers Vehicles](https://www.consystec.com/pr2026proto/web/element.htm?id=252) | Existing | Private Travelers |

## Related Functional Requirements (2 found)

- [Functional Requirements: RSE Situation Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=180)
- [Functional Requirements: TMC Traffic Network Performance Evaluation](https://www.consystec.com/pr2026proto/web/funreq.htm?id=384)

## Deployment Guidance

When planning a deployment in Sustainable Transport:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

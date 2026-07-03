# Sustainable Transport (ST)

Congestion pricing, transit incentives, emissions management. (also: road pricing, cordon pricing, value pricing, dynamic pricing, tolling for congestion)

## Service Packages in This Architecture

### Sustainable Transport
*Congestion pricing, transit incentives, alternative fuel support, eco-traffic metering, roadside lighting, eco-lanes, eco-approach at signals, low emissions zone management (also: road pricing, cordon pricing, value pricing, dynamic pricing, tolling for congestion)*

- [mpSH1_ST04-02(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_ST04-02(Municipal))
- [mpSH3_ST04-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_ST04-01(PRHTA))
- [mpSH109_ST05-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH109_ST05-01(PRHTA))
- [mpSH109_ST05-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH109_ST05-02(PRHTA))
- [mpSH1_ST05-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_ST05-02(PRHTA))
- [mpSH3_ST05-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_ST05-01(PRHTA))
- [mpSH5_ST05-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_ST05-01(PRHTA))
- [mpSH5_ST05-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_ST05-02(PRHTA))
- [mpSH83_ST05-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH83_ST05-01(PRHTA))
- [mpSH83_ST05-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH83_ST05-02(PRHTA))

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

## Interfaces (9 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Municipal ITS Field Equipment → lighting system status → Municipal SMCs (US: NTCIP Lighting - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-51)
- Municipal ITS Field Equipment → traffic detector data → Municipal SMCs (US: NTCIP Transportation Sensors - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-51)
- Municipal SMCs → lighting system control data → Municipal ITS Field Equipment (US: NTCIP Lighting - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-51)
- Municipal SMCs → traffic detector control → Municipal ITS Field Equipment (US: NTCIP Transportation Sensors - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-51)
- Municipal Website → electric charging services inventory → Private Travelers Vehicles — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-252)
- PRHTA ITS Field Devices → lighting system status → PRHTA TMC (US: NTCIP Lighting - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA ITS Field Devices → traffic detector data → PRHTA TMC (US: NTCIP Transportation Sensors - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → lighting system control data → PRHTA ITS Field Devices (US: NTCIP Lighting - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → traffic detector control → PRHTA ITS Field Devices (US: NTCIP Transportation Sensors - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)

## Applicable Standards (2)

Communication and data standards referenced by the interfaces above.

- **US: NTCIP Lighting - SNMPv1** — Specifies NTCIP 1201, NTCIP 1213, NTCIP 2301 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=72))
- **US: NTCIP Transportation Sensors - SNMPv1** — Specifies NTCIP 1201, NTCIP 1209, NTCIP 2301 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=71))

## Related Functional Requirements (2 found)

- [Functional Requirements: RSE Situation Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=180)
- [Functional Requirements: TMC Traffic Network Performance Evaluation](https://www.consystec.com/pr2026proto/web/funreq.htm?id=384)


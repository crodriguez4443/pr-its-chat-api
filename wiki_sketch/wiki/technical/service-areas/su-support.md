# Support (SU)

Device management, mapping, location services, communications infrastructure.

## Service Packages in This Architecture

### Support Services
*Map management, device management, cybersecurity, communications, object registration, device certification, center/field/vehicle/personnel maintenance, remote access, VRU device transition*

- [Service Package SU03-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/SU03-01(PRHTA))
- [Service Package SU03-02(Metropistas)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/SU03-02(Metropistas))
- [Service Package SU03-03(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/SU03-03(Municipal))
- [Service Package SU03-03(MunicipalTrafficDPW)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/SU03-03(MunicipalTrafficDPW))
- [Service Package SU03-04(MunicipalTransit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/SU03-04(MunicipalTransit))
- [Service Package SU03-04(Transit)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/SU03-04(Transit))

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

## Interfaces (16 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Interface: Metropistas Communications Infrastructure Systems → ITS information_ud → Metropistas ITS Field Devices — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=280-285)
- Interface: Metropistas Communications Infrastructure Systems → ITS information_ud → Metropistas TMC — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=278-285)
- Interface: Metropistas ITS Field Devices → ITS information_ud → Metropistas Communications Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=280-285)
- Interface: Metropistas TMC → ITS information_ud → Metropistas Communications Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=278-285)
- Interface: Municipal ITS Field Equipment → ITS information_ud → Municipal Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-267)
- Interface: Municipal Infrastructure Systems → ITS information_ud → Municipal ITS Field Equipment — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-267)
- Interface: Municipal Infrastructure Systems → ITS information_ud → Municipal Local Transit Operations Centers — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-267)
- Interface: Municipal Infrastructure Systems → ITS information_ud → Municipal Local Transit Vehicles — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=71-267)
- Interface: Municipal Infrastructure Systems → ITS information_ud → Municipal SMCs — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-267)
- Interface: Municipal Local Transit Operations Centers → ITS information_ud → Municipal Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-267)
- Interface: Municipal Local Transit Vehicles → ITS information_ud → Municipal Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=71-267)
- Interface: Municipal SMCs → ITS information_ud → Municipal Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-267)
- Interface: PRHTA Communications Infrastructure Systems → ITS information_ud → PRHTA ITS Field Devices — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=264-265)
- Interface: PRHTA Communications Infrastructure Systems → ITS information_ud → PRHTA TMC — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-265)
- Interface: PRHTA ITS Field Devices → ITS information_ud → PRHTA Communications Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=264-265)
- Interface: PRHTA TMC → ITS information_ud → PRHTA Communications Infrastructure Systems — [ITS information_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-265)

## Related Functional Requirements (57 found)

- [Functional Requirements: Vehicle Intersection Warning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=1)
- [Functional Requirements: Emergency Routing](https://www.consystec.com/pr2026proto/web/funreq.htm?id=121)
- [Functional Requirements: Transit Vehicle Passenger Counting](https://www.consystec.com/pr2026proto/web/funreq.htm?id=127)
- [Functional Requirements: Transit Center Passenger Counting](https://www.consystec.com/pr2026proto/web/funreq.htm?id=129)
- [Functional Requirements: CV On-Board Cargo Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=145)
- [Functional Requirements: Emergency Incident Command](https://www.consystec.com/pr2026proto/web/funreq.htm?id=148)
- [Functional Requirements: EV On-Board Incident Management Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=149)
- [Functional Requirements: Emergency Dispatch](https://www.consystec.com/pr2026proto/web/funreq.htm?id=150)
- [Functional Requirements: Parking Area Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=162)
- [Functional Requirements: Transit Vehicle On-Board Trip Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=164)
- [Functional Requirements: Vehicle Situation Data Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=179)
- [Functional Requirements: Fleet Administration](https://www.consystec.com/pr2026proto/web/funreq.htm?id=194)
- [Functional Requirements: CV On-Board Trip Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=195)
- [Functional Requirements: CV On-Board Safety and Security](https://www.consystec.com/pr2026proto/web/funreq.htm?id=197)
- [Functional Requirements: ITS Data Subscription Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=204)
- [Functional Requirements: MCV Winter Maintenance](https://www.consystec.com/pr2026proto/web/funreq.htm?id=215)
- [Functional Requirements: Emergency Commercial Vehicle Response](https://www.consystec.com/pr2026proto/web/funreq.htm?id=226)
- [Functional Requirements: Roadway Field Management Station Operation](https://www.consystec.com/pr2026proto/web/funreq.htm?id=310)
- [Functional Requirements: TIC Road Weather Advisories and Warnings](https://www.consystec.com/pr2026proto/web/funreq.htm?id=32)
- [Functional Requirements: MCM Vehicle Tracking](https://www.consystec.com/pr2026proto/web/funreq.htm?id=326)
- [Functional Requirements: MCV Vehicle Location Tracking](https://www.consystec.com/pr2026proto/web/funreq.htm?id=328)
- [Functional Requirements: Roadway Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=33)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=350)
- [Functional Requirements: TMC Service Patrol Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=373)
- [Functional Requirements: TMC Situation Data Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=380)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=39)
- [Functional Requirements: Transit Center Vehicle Tracking](https://www.consystec.com/pr2026proto/web/funreq.htm?id=392)
- [Functional Requirements: TMC Speed Warning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=40)
- [Functional Requirements: EV Service Patrol Vehicle Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=435)
- [Functional Requirements: Field Asset Identification](https://www.consystec.com/pr2026proto/web/funreq.htm?id=501)
- [Functional Requirements: MCM Field Asset Tracking](https://www.consystec.com/pr2026proto/web/funreq.htm?id=504)
- [Functional Requirements: MCV Work Zone Support](https://www.consystec.com/pr2026proto/web/funreq.htm?id=51)
- [Functional Requirements: MCM Remote Vehicle Control](https://www.consystec.com/pr2026proto/web/funreq.htm?id=513)
- [Functional Requirements: RSE Intersection Safety](https://www.consystec.com/pr2026proto/web/funreq.htm?id=57)
- [Functional Requirements: Roadway Signal Control](https://www.consystec.com/pr2026proto/web/funreq.htm?id=60)
- [Functional Requirements: EV On-Board En Route Support](https://www.consystec.com/pr2026proto/web/funreq.htm?id=65)
- [Functional Requirements: Personal Pedestrian Safety](https://www.consystec.com/pr2026proto/web/funreq.htm?id=66)
- [Functional Requirements: TMC In-Vehicle Signing Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=76)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=83)
- [Functional Requirements: RSE Intersection Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=90)
- [Functional Requirements: EV On-Board En Route Support](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el109)
- [Functional Requirements: EV Service Patrol Vehicle Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el126)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el153)
- [Functional Requirements: Vehicle Basic Safety Communication](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el252)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el254)
- [Functional Requirements: Field Asset Identification](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el264)
- [Functional Requirements: ITS Data Subscription Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el265)
- [Functional Requirements: RSE Intersection Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el268)
- [Functional Requirements: CV On-Board Cargo Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el41)
- [Functional Requirements: EV On-Board En Route Support](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el44)
- [Functional Requirements: ITS Data Subscription Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el45)
- [Functional Requirements: EV On-Board En Route Support](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el49)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el52)
- [Functional Requirements: Fleet Administration](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el61)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el68)
- [Functional Requirements: ITS Data Subscription Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el71)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el82)

## Deployment Guidance

When planning a deployment in Support:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

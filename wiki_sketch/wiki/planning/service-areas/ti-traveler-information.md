# Traveler Information (TI)

511 services, third-party apps, multimodal alerts, personalized traveler info. (also: traveler information system, travel info, road conditions, traffic conditions, travel advisory)

## Service Packages in This Architecture

### Traveler Information Services
*511, third-party data feeds, multimodal alerts, personalized info (also: traveler information system, travel info, road conditions, traffic conditions, travel advisory)*

- [Service Package mpSH112_TI01-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH112_TI01-01(PRHTA))
- [Service Package mpSH1_TI01-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_TI01-01(PRHTA))
- [Service Package mpSH1_TI01-03(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_TI01-03(Municipal))
- [Service Package mpSH112_TI02-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH112_TI02-01(PRHTA))
- [Service Package mpSH1_TI02-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_TI02-01(PRHTA))
- [Service Package mpSH1_TI02-03(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH1_TI02-03(Municipal))
- [Service Package mpSH3_TI07-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH3_TI07-01(PRHTA))
- [Service Package mpSH5_TI07-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/mpSH5_TI07-01(PRHTA))

## Key Elements (16 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Media](https://www.consystec.com/pr2026proto/web/element.htm?id=68) | Existing | Media |
| [Metropistas TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Public Information Office](https://www.consystec.com/pr2026proto/web/element.htm?id=46) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Website](https://www.consystec.com/pr2026proto/web/element.htm?id=52) | Existing | Municipal Traffic and Maintenance Agencies |
| [National Weather Service](https://www.consystec.com/pr2026proto/web/element.htm?id=96) | Existing | NOAA |
| [PR Police Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=106) | Existing | PR Police |
| [PR Travel and Tourism Website](https://www.consystec.com/pr2026proto/web/element.htm?id=104) | Existing | State Emergency Management Agency |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Travelers Personal Computing Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=187) | Existing | Private Travelers |
| [Private Travelers Vehicles](https://www.consystec.com/pr2026proto/web/element.htm?id=252) | Existing | Private Travelers |
| [Private Weather Support Services System](https://www.consystec.com/pr2026proto/web/element.htm?id=248) | Existing | Private Weather Information Provider |
| [State Emergency Management Agency Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=102) | Existing | State Emergency Management Agency |

## Interfaces (14 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Municipal Local Transit Operations Centers → transit and fare schedules → Municipal Public Information Office (US: TCIP - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-69)
- Municipal Local Transit Operations Centers → transit and fare schedules → PR Travel and Tourism Website (US: TCIP - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-104)
- Municipal Public Information Office → road network conditions → Municipal Website (US: TMDD - NTCIP Messaging) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-52)
- Municipal SMCs → current infrastructure restrictions → Municipal Website (US: TMDD - NTCIP Messaging) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Municipal SMCs → maint and constr work plans → Municipal Website (US: TMDD - NTCIP Messaging) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Municipal SMCs → road network conditions → Municipal Public Information Office (US: TMDD - NTCIP Messaging) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-51)
- Municipal SMCs → road network conditions → Municipal Website (US: TMDD - NTCIP Messaging) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Municipal SMCs → roadway maintenance status → Municipal Website ((None-Data) - Secure Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Municipal SMCs → traffic images → Municipal Website — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Municipal Website → road network conditions → PR Travel and Tourism Website (US: TMDD - NTCIP Messaging) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-104)
- PRHTA ITS Field Devices → roadway dynamic signage status → PRHTA TMC (US: NTCIP Message Sign - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- PRHTA TMC → roadway dynamic signage data → PRHTA ITS Field Devices (US: NTCIP Message Sign - SNMPv1) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- Private Travelers Personal Computing Devices → traveler request → Municipal Website (US: ATIS - Secure Wireless Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-187)
- Private Travelers Personal Computing Devices → user profile → Municipal Website ((None-Data) - Secure Wireless Internet (ITS)) — [interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-187)

## Related Functional Requirements (24 found)

- [Functional Requirements: Personal Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=116)
- [Functional Requirements: TIC Situation Data Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=172)
- [Functional Requirements: Personal Traveler Information Reception](https://www.consystec.com/pr2026proto/web/funreq.htm?id=175)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=177)
- [Functional Requirements: TIC Freight-Specific Travel Planning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=196)
- [Functional Requirements: Vehicle Traveler Information Reception](https://www.consystec.com/pr2026proto/web/funreq.htm?id=23)
- [Functional Requirements: Emergency Early Warning System](https://www.consystec.com/pr2026proto/web/funreq.htm?id=305)
- [Functional Requirements: TIC Operations Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=318)
- [Functional Requirements: Parking Coordination](https://www.consystec.com/pr2026proto/web/funreq.htm?id=337)
- [Functional Requirements: TIC Traveler Telephone Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=400)
- [Functional Requirements: Transit Center Park and Ride Operations](https://www.consystec.com/pr2026proto/web/funreq.htm?id=425)
- [Functional Requirements: MCM Work Zone Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=53)
- [Functional Requirements: TIC Traveler Information Broadcast](https://www.consystec.com/pr2026proto/web/funreq.htm?id=55)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=83)
- [Functional Requirements: Personal Trip Planning and Route Guidance](https://www.consystec.com/pr2026proto/web/funreq.htm?id=9)

*... and 9 more*

## Deployment Guidance

When planning a deployment in Traveler Information:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

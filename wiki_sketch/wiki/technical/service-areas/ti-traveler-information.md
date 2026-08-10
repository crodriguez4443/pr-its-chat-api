# Traveler Information (TI)

511 services, third-party apps, multimodal alerts, personalized traveler info. (also: traveler information system, travel info, road conditions, traffic conditions, travel advisory)

## Service Packages in This Architecture

### Traveler Information Services
*511, third-party data feeds, multimodal alerts, personalized info, en-route guidance, electronic payment, personal wayfinding, travel services reservation (also: traveler information system, travel info, road conditions, traffic conditions, travel advisory)*

- [Service Package TI01-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI01-01(PRHTA))
- [Service Package TI01-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI01-02(PRHTA))
- [Service Package TI01-03(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI01-03(Municipal))
- [Service Package TI01-04(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI01-04(Municipal))
- [Service Package TI02-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI02-01(PRHTA))
- [Service Package TI02-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI02-02(PRHTA))
- [Service Package TI02-03(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI02-03(Municipal))
- [Service Package TI02-04(State)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI02-04(State))
- [Service Package TI03-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI03-01(PRHTA))
- [Service Package TI07-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/TI07-01(PRHTA))

## Key Elements (21 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Media](https://www.consystec.com/pr2026proto/web/element.htm?id=68) | Existing | Media |
| [Metropistas TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Public Information Office](https://www.consystec.com/pr2026proto/web/element.htm?id=46) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal Public Works Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=47) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Website](https://www.consystec.com/pr2026proto/web/element.htm?id=52) | Existing | Municipal Traffic and Maintenance Agencies |
| [National Weather Service](https://www.consystec.com/pr2026proto/web/element.htm?id=96) | Existing | NOAA |
| [PR Police Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=106) | Existing | PR Police |
| [PR Travel and Tourism Website](https://www.consystec.com/pr2026proto/web/element.htm?id=104) | Existing | State Emergency Management Agency |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Information Services](https://www.consystec.com/pr2026proto/web/element.htm?id=115) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Maintenance and Construction Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=128) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Public Information Office](https://www.consystec.com/pr2026proto/web/element.htm?id=153) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [Private Third Party Information Providers](https://www.consystec.com/pr2026proto/web/element.htm?id=254) | Existing | Private Traffic Data Providers |
| [Private Travelers Personal Computing Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=187) | Existing | Private Travelers |
| [Private Travelers Vehicles](https://www.consystec.com/pr2026proto/web/element.htm?id=252) | Existing | Private Travelers |
| [Private Weather Support Services System](https://www.consystec.com/pr2026proto/web/element.htm?id=248) | Existing | Private Weather Information Provider |
| [State Emergency Management Agency Systems](https://www.consystec.com/pr2026proto/web/element.htm?id=102) | Existing | State Emergency Management Agency |

## Interfaces (49 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Interface: Metropistas TMC → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-278)
- Interface: Metropistas TMC → traffic images → PRHTA Information Services — [traffic images interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-278)
- Interface: Municipal Local Transit Operations Centers → transit and fare schedules → Municipal Public Information Office (US: TCIP - Secure Internet (ITS)) — [transit and fare schedules interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-69)
- Interface: Municipal Local Transit Operations Centers → transit and fare schedules → PR Travel and Tourism Website (US: TCIP - Secure Internet (ITS)) — [transit and fare schedules interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-104)
- Interface: Municipal Local Transit Operations Centers → transit and fare schedules → PRHTA Information Services (US: TCIP - Secure Internet (ITS)) — [transit and fare schedules interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-115)
- Interface: Municipal Public Information Office → road network conditions → Municipal Website (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-52)
- Interface: Municipal Public Information Office → road network conditions → Private Third Party Information Providers (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-254)
- Interface: Municipal Public Works Dispatch → current infrastructure restrictions → Municipal Public Information Office (US: TMDD - NTCIP Messaging) — [current infrastructure restrictions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-47)
- Interface: Municipal Public Works Dispatch → current infrastructure restrictions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [current infrastructure restrictions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=47-115)
- Interface: Municipal Public Works Dispatch → maint and constr work plans → Municipal Public Information Office (US: TMDD - NTCIP Messaging) — [maint and constr work plans interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-47)
- Interface: Municipal Public Works Dispatch → maint and constr work plans → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [maint and constr work plans interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=47-115)
- Interface: Municipal Public Works Dispatch → roadway maintenance status → Municipal Public Information Office ((None-Data) - Secure Internet (ITS)) — [roadway maintenance status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-47)
- Interface: Municipal Public Works Dispatch → roadway maintenance status → PRHTA Information Services ((None-Data) - Secure Internet (ITS)) — [roadway maintenance status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=47-115)
- Interface: Municipal SMCs → current infrastructure restrictions → Municipal Website (US: TMDD - NTCIP Messaging) — [current infrastructure restrictions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Interface: Municipal SMCs → maint and constr work plans → Municipal Website (US: TMDD - NTCIP Messaging) — [maint and constr work plans interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Interface: Municipal SMCs → road network conditions → Municipal Public Information Office (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=46-51)
- Interface: Municipal SMCs → road network conditions → Municipal Website (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Interface: Municipal SMCs → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-115)
- Interface: Municipal SMCs → roadway maintenance status → Municipal Website ((None-Data) - Secure Internet (ITS)) — [roadway maintenance status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Interface: Municipal SMCs → traffic images → Municipal Website — [traffic images interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-52)
- Interface: Municipal Website → road network conditions → PR Travel and Tourism Website (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-104)
- Interface: PRHTA ITS Field Devices → roadway dynamic signage status → PRHTA TMC (US: NTCIP Message Sign - SNMPv1) — [roadway dynamic signage status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- Interface: PRHTA Information Services → road network conditions → PR Travel and Tourism Website (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=104-115)
- Interface: PRHTA Information Services → road network conditions → Private Third Party Information Providers (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-254)
- Interface: PRHTA Information Services → traveler alerts → Private Travelers Personal Computing Devices (Data for Distribution (TBD) - OMG DDS over Wireless) — [traveler alerts interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-187)
- Interface: PRHTA Information Services → vehicle signage data_ud → Private Travelers Vehicles — [vehicle signage data_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-252)
- Interface: PRHTA Maintenance and Construction Systems → current infrastructure restrictions → Municipal Website (US: TMDD - NTCIP Messaging) — [current infrastructure restrictions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-128)
- Interface: PRHTA Maintenance and Construction Systems → current infrastructure restrictions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [current infrastructure restrictions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-128)
- Interface: PRHTA Maintenance and Construction Systems → maint and constr work plans → Municipal Website (US: TMDD - NTCIP Messaging) — [maint and constr work plans interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-128)
- Interface: PRHTA Maintenance and Construction Systems → maint and constr work plans → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [maint and constr work plans interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-128)
- Interface: PRHTA Maintenance and Construction Systems → roadway maintenance status → Municipal Website ((None-Data) - Secure Internet (ITS)) — [roadway maintenance status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-128)
- Interface: PRHTA Maintenance and Construction Systems → roadway maintenance status → PRHTA Information Services ((None-Data) - Secure Internet (ITS)) — [roadway maintenance status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-128)
- Interface: PRHTA TMC → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-154)
- Interface: PRHTA TMC → road network conditions → Private Third Party Information Providers (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-254)
- Interface: PRHTA TMC → roadway dynamic signage data → PRHTA ITS Field Devices (US: NTCIP Message Sign - SNMPv1) — [roadway dynamic signage data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=154-264)
- Interface: PRHTA TMC → traffic images → PRHTA Information Services — [traffic images interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-154)
- Interface: PRHTA TMC → vehicle signage messages list_ud → PRHTA Information Services — [vehicle signage messages list_ud interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-154)
- Interface: Private Third Party Information Providers → guidance updates → Private Travelers Personal Computing Devices (Data for Distribution (TBD) - OMG DDS over Wireless) — [guidance updates interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-254)
- Interface: Private Third Party Information Providers → road network conditions → PR Travel and Tourism Website (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=104-254)
- Interface: Private Third Party Information Providers → road network conditions → PRHTA Information Services (US: TMDD - NTCIP Messaging) — [road network conditions interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-254)
- Interface: Private Third Party Information Providers → traffic images → PRHTA Information Services — [traffic images interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-254)
- Interface: Private Third Party Information Providers → traveler alerts → Private Travelers Personal Computing Devices (Data for Distribution (TBD) - OMG DDS over Wireless) — [traveler alerts interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-254)
- Interface: Private Third Party Information Providers → trip plan → Private Travelers Personal Computing Devices (US: ATIS - Secure Wireless Internet (ITS)) — [trip plan interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-254)
- Interface: Private Travelers Personal Computing Devices → traveler request → Municipal Website (US: ATIS - Secure Wireless Internet (ITS)) — [traveler request interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-187)
- Interface: Private Travelers Personal Computing Devices → traveler request → PRHTA Information Services (US: ATIS - Secure Wireless Internet (ITS)) — [traveler request interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-187)
- Interface: Private Travelers Personal Computing Devices → trip request → Private Third Party Information Providers (US: ATIS - Secure Wireless Internet (ITS)) — [trip request interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-254)
- Interface: Private Travelers Personal Computing Devices → trip status → Private Third Party Information Providers ((None-Data) - Secure Wireless Internet (ITS)) — [trip status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=187-254)
- Interface: Private Travelers Personal Computing Devices → user profile → Municipal Website ((None-Data) - Secure Wireless Internet (ITS)) — [user profile interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=52-187)
- Interface: Private Travelers Personal Computing Devices → user profile → PRHTA Information Services ((None-Data) - Secure Wireless Internet (ITS)) — [user profile interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=115-187)

## Applicable Standards (7)

Communication and data standards referenced by the interfaces above.

- **(None-Data) - Secure Internet (ITS)** — A bundle of standards (RFCs) that groups the common mgmt info bases (MIBs) used to manage IP networks at the transport layer and below using SNMPv3. ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=12106))
- **(None-Data) - Secure Wireless Internet (ITS)** — A bundle of standards (RFCs) that groups the common mgmt info bases (MIBs) used to manage IP networks at the transport layer and below using SNMPv3. ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=55280))
- **Data for Distribution (TBD) - OMG DDS over Wireless** — Specifies RFC 768 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=64314))
- **US: ATIS - Secure Wireless Internet (ITS)** — Specifies SAE J2353, SAE J2354, RFC 9110, RFC 9112 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=55285))
- **US: NTCIP Message Sign - SNMPv1** — Specifies NTCIP 1201, NTCIP 1203, NTCIP 2301 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=54))
- **US: TCIP - Secure Internet (ITS)** — This std def the data concepts used by the TCIP standard. ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=58659))
- **US: TMDD - NTCIP Messaging** — Specifies RFC 9293 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=142))

## Related Functional Requirements (35 found)

- [Functional Requirements: Personal Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=116)
- [Functional Requirements: TIC Emergency Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=142)
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
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=95)
- [Functional Requirements: TIC Trip Planning](https://www.consystec.com/pr2026proto/web/funreq.htm?id=96)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el104)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el153)
- [Functional Requirements: Personal Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el187)
- [Functional Requirements: MCM Work Zone Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el247)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el254)
- [Functional Requirements: TIC Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el263)
- [Functional Requirements: Vehicle Traveler Information Reception](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el275)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el295)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el300)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el304)
- [Functional Requirements: Personal Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el305)
- [Functional Requirements: Personal Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el306)
- [Functional Requirements: Personal Interactive Traveler Information](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el311)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el46)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el52)
- [Functional Requirements: TIC Connected Vehicle Traveler Info Distribution](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el68)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el70)

## Deployment Guidance

When planning a deployment in Traveler Information:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

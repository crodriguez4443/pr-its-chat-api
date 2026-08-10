# Data Management (DM)

ITS data archiving, performance measurement, data warehousing.

## Service Packages in This Architecture

### Data Management
*ITS data archiving, performance measurement, NPMRDS (also: national performance management research data set, probe data, travel time data, speed data)*

- [Service Package DM01-01(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-01(PRHTA))
- [Service Package DM01-02(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-02(PRHTA))
- [Service Package DM01-03(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-03(PRHTA))
- [Service Package DM01-04(PRHTA)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-04(PRHTA))
- [Service Package DM01-05(Metropistas)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-05(Metropistas))
- [Service Package DM01-06(Municipal)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-06(Municipal))
- [Service Package DM01-07(MPO)](https://www.consystec.com/pr2026proto/web/spinstance.htm?id=/DM01-07(MPO))

## Key Elements (20 total)

| Element | Status | Stakeholder |
|---------|--------|-------------|
| [Archive Data Users](https://www.consystec.com/pr2026proto/web/element.htm?id=6) | Existing | Archive Data Users |
| [MPO Field Sensors](https://www.consystec.com/pr2026proto/web/element.htm?id=82) | Existing | PR Metropolitan Planning Organization |
| [MPO Transportation Data Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=83) | Existing | PR Metropolitan Planning Organization |
| [Metropistas Data Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=284) | Planned | Metropistas |
| [Metropistas ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=280) | Planned | Metropistas |
| [Metropistas TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=278) | Planned | Metropistas |
| [Municipal ITS Field Equipment](https://www.consystec.com/pr2026proto/web/element.htm?id=45) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Local Transit Operations Centers](https://www.consystec.com/pr2026proto/web/element.htm?id=69) | Existing | Municipal Local Transit Agencies |
| [Municipal Public Safety Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=89) | Existing | Municipal Public Safety Agencies |
| [Municipal SMCs](https://www.consystec.com/pr2026proto/web/element.htm?id=51) | Existing | Municipal Traffic and Maintenance Agencies |
| [Municipal Transportation Data Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=272) | Planned | Municipal Traffic and Maintenance Agencies |
| [PR Motor Carrier Database](https://www.consystec.com/pr2026proto/web/element.htm?id=54) | Existing | PR Department of Motor Vehicles |
| [PR Police Dispatch](https://www.consystec.com/pr2026proto/web/element.htm?id=106) | Existing | PR Police |
| [PRHTA Crash Information System](https://www.consystec.com/pr2026proto/web/element.htm?id=151) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Data Portal](https://www.consystec.com/pr2026proto/web/element.htm?id=118) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA ITS Field Devices](https://www.consystec.com/pr2026proto/web/element.htm?id=264) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Statewide Asset Management System](https://www.consystec.com/pr2026proto/web/element.htm?id=152) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA TMC](https://www.consystec.com/pr2026proto/web/element.htm?id=154) | Existing | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Traffic Management Performance Analysis Archive](https://www.consystec.com/pr2026proto/web/element.htm?id=269) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |
| [PRHTA Transit Database](https://www.consystec.com/pr2026proto/web/element.htm?id=155) | Planned | PRHTA - Puerto Rico Highway and Transportation Aut |

## Interfaces (69 data flows)

Real information flows between elements in this service area, in the form *Source Element → information flow → Destination Element*. Each links to its interface specification.

- Interface: Archive Data Users → archive analysis requests → PRHTA Data Portal (US: ADMS - Secure Internet (ITS)) — [archive analysis requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-118)
- Interface: Archive Data Users → archived data product requests → MPO Transportation Data Archive (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-83)
- Interface: Archive Data Users → archived data product requests → Metropistas Data Archive (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-284)
- Interface: Archive Data Users → archived data product requests → Municipal Transportation Data Archive (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-272)
- Interface: Archive Data Users → archived data product requests → PRHTA Crash Information System (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-151)
- Interface: Archive Data Users → archived data product requests → PRHTA Data Portal (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-118)
- Interface: Archive Data Users → archived data product requests → PRHTA Statewide Asset Management System (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-152)
- Interface: Archive Data Users → archived data product requests → PRHTA Transit Database (US: ADMS - Secure Internet (ITS)) — [archived data product requests interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-155)
- Interface: MPO Field Sensors → roadside archive data → MPO Transportation Data Archive (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=82-83)
- Interface: MPO Field Sensors → roadside archive data → PRHTA Statewide Asset Management System (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=82-152)
- Interface: MPO Transportation Data Archive → archive coordination → Metropistas Data Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-284)
- Interface: MPO Transportation Data Archive → archive coordination → Municipal Transportation Data Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-272)
- Interface: MPO Transportation Data Archive → archive status → Municipal Public Safety Dispatch — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-89)
- Interface: MPO Transportation Data Archive → archive status → Municipal SMCs (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-83)
- Interface: MPO Transportation Data Archive → archive status → PR Police Dispatch — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-106)
- Interface: MPO Transportation Data Archive → archive status → PRHTA TMC (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-154)
- Interface: MPO Transportation Data Archive → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-83)
- Interface: MPO Transportation Data Archive → data collection and monitoring control → MPO Field Sensors (US: NTCIP Data Collection - SNMPv1) — [data collection and monitoring control interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=82-83)
- Interface: MPO Transportation Data Archive → data collection and monitoring control → PRHTA ITS Field Devices (US: NTCIP Data Collection - SNMPv1) — [data collection and monitoring control interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-264)
- Interface: Metropistas Data Archive → archive coordination → MPO Transportation Data Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-284)
- Interface: Metropistas Data Archive → archive coordination → PRHTA Crash Information System (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=151-284)
- Interface: Metropistas Data Archive → archive status → Metropistas TMC (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=278-284)
- Interface: Metropistas Data Archive → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-284)
- Interface: Metropistas ITS Field Devices → roadside archive data → Metropistas Data Archive (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=280-284)
- Interface: Metropistas TMC → emergency archive data → Metropistas Data Archive — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=278-284)
- Interface: Municipal ITS Field Equipment → roadside archive data → Municipal Transportation Data Archive (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-272)
- Interface: Municipal ITS Field Equipment → roadside archive data → PRHTA Statewide Asset Management System (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-152)
- Interface: Municipal Local Transit Operations Centers → emergency archive data → PRHTA Crash Information System — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-151)
- Interface: Municipal Local Transit Operations Centers → transit archive data → PRHTA Transit Database (Data for Distribution (TBD) - OMG DDS) — [transit archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-155)
- Interface: Municipal Public Safety Dispatch → emergency archive data → MPO Transportation Data Archive — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-89)
- Interface: Municipal SMCs → emergency archive data → Municipal Transportation Data Archive — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-272)
- Interface: Municipal SMCs → emergency archive data → PRHTA Crash Information System — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-151)
- Interface: Municipal SMCs → traffic archive data → MPO Transportation Data Archive (Data for Distribution (TBD) - OMG DDS) — [traffic archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-83)
- Interface: Municipal Transportation Data Archive → archive coordination → MPO Transportation Data Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-272)
- Interface: Municipal Transportation Data Archive → archive coordination → PRHTA Crash Information System (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=151-272)
- Interface: Municipal Transportation Data Archive → archive status → Municipal SMCs (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-272)
- Interface: Municipal Transportation Data Archive → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-272)
- Interface: PR Motor Carrier Database → archive coordination → PRHTA Crash Information System (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=54-151)
- Interface: PR Police Dispatch → emergency archive data → MPO Transportation Data Archive — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-106)
- Interface: PR Police Dispatch → emergency archive data → PRHTA Crash Information System — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=106-151)
- Interface: PRHTA Crash Information System → archive coordination → Metropistas Data Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=151-284)
- Interface: PRHTA Crash Information System → archive coordination → Municipal Transportation Data Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=151-272)
- Interface: PRHTA Crash Information System → archive coordination → PR Motor Carrier Database (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=54-151)
- Interface: PRHTA Crash Information System → archive coordination → PRHTA Data Portal (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-151)
- Interface: PRHTA Crash Information System → archive status → Municipal Local Transit Operations Centers (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-151)
- Interface: PRHTA Crash Information System → archive status → Municipal SMCs (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=51-151)
- Interface: PRHTA Crash Information System → archive status → PR Police Dispatch — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=106-151)
- Interface: PRHTA Crash Information System → archive status → PRHTA TMC (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=151-154)
- Interface: PRHTA Crash Information System → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-151)
- Interface: PRHTA Data Portal → archive analysis results → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archive analysis results interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-118)
- Interface: PRHTA Data Portal → archive coordination → PRHTA Crash Information System (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-151)
- Interface: PRHTA Data Portal → archive coordination → PRHTA Statewide Asset Management System (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-152)
- Interface: PRHTA Data Portal → archive coordination → PRHTA Traffic Management Performance Analysis Archive (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-269)
- Interface: PRHTA Data Portal → archive coordination → PRHTA Transit Database (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-155)
- Interface: PRHTA Data Portal → archive request confirmation → Archive Data Users ((None-Data) - Secure Internet (ITS)) — [archive request confirmation interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-118)
- Interface: PRHTA Data Portal → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-118)
- Interface: PRHTA ITS Field Devices → roadside archive data → MPO Transportation Data Archive (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-264)
- Interface: PRHTA ITS Field Devices → roadside archive data → PRHTA Statewide Asset Management System (Data for Distribution (TBD) - OMG DDS) — [roadside archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=152-264)
- Interface: PRHTA Statewide Asset Management System → archive coordination → PRHTA Data Portal (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-152)
- Interface: PRHTA Statewide Asset Management System → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-152)
- Interface: PRHTA Statewide Asset Management System → data collection and monitoring control → MPO Field Sensors (US: NTCIP Data Collection - SNMPv1) — [data collection and monitoring control interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=82-152)
- Interface: PRHTA Statewide Asset Management System → data collection and monitoring control → Municipal ITS Field Equipment (US: NTCIP Data Collection - SNMPv1) — [data collection and monitoring control interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=45-152)
- Interface: PRHTA Statewide Asset Management System → data collection and monitoring control → PRHTA ITS Field Devices (US: NTCIP Data Collection - SNMPv1) — [data collection and monitoring control interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=152-264)
- Interface: PRHTA TMC → emergency archive data → PRHTA Crash Information System — [emergency archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=151-154)
- Interface: PRHTA TMC → traffic archive data → MPO Transportation Data Archive (Data for Distribution (TBD) - OMG DDS) — [traffic archive data interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=83-154)
- Interface: PRHTA Traffic Management Performance Analysis Archive → archive coordination → PRHTA Data Portal (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-269)
- Interface: PRHTA Transit Database → archive coordination → PRHTA Data Portal (US: ADMS - Guaranteed Secure Internet (ITS)) — [archive coordination interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=118-155)
- Interface: PRHTA Transit Database → archive status → Municipal Local Transit Operations Centers (US: ADMS - Secure Internet (ITS)) — [archive status interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=69-155)
- Interface: PRHTA Transit Database → archived data products → Archive Data Users (US: ADMS - Secure Internet (ITS)) — [archived data products interface](https://www.consystec.com/pr2026proto/web/interface.htm?id=6-155)

## Applicable Standards (5)

Communication and data standards referenced by the interfaces above.

- **(None-Data) - Secure Internet (ITS)** — A bundle of standards (RFCs) that groups the common mgmt info bases (MIBs) used to manage IP networks at the transport layer and below using SNMPv3. ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=12106))
- **Data for Distribution (TBD) - OMG DDS** — Specifies RFC 768 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=63682))
- **US: ADMS - Guaranteed Secure Internet (ITS)** — Specifies RFC 9293 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=71267))
- **US: ADMS - Secure Internet (ITS)** — A bundle of standards that define how to manage an archived data mgmt system interface. ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=71269))
- **US: NTCIP Data Collection - SNMPv1** — Specifies NTCIP 1201, NTCIP 1206, NTCIP 1209, NTCIP 2301 ([standard](https://www.consystec.com/pr2026proto/web/solution.htm?id=71193))

## Related Functional Requirements (25 found)

- [Functional Requirements: RSE Traffic Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=104)
- [Functional Requirements: TIC Situation Data Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=172)
- [Functional Requirements: Archive Situation Data Archival](https://www.consystec.com/pr2026proto/web/funreq.htm?id=219)
- [Functional Requirements: Emergency Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=304)
- [Functional Requirements: TIC Operations Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=318)
- [Functional Requirements: MCM Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=322)
- [Functional Requirements: Parking Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=338)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=35)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=350)
- [Functional Requirements: TMC Environmental Monitoring](https://www.consystec.com/pr2026proto/web/funreq.htm?id=36)
- [Functional Requirements: TMC Situation Data Management](https://www.consystec.com/pr2026proto/web/funreq.htm?id=380)
- [Functional Requirements: Transit Center Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=393)
- [Functional Requirements: TMC Road Weather Advisories and Warnings](https://www.consystec.com/pr2026proto/web/funreq.htm?id=428)
- [Functional Requirements: TMC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=429)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=95)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el172)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el177)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el248)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el295)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el300)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el304)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el46)
- [Functional Requirements: MCM Environmental Information Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el47)
- [Functional Requirements: TIC Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el70)
- [Functional Requirements: Roadway Data Collection](https://www.consystec.com/pr2026proto/web/funreq.htm?id=_el82)

## Deployment Guidance

When planning a deployment in Data Management:

1. **Identify the service packages** that apply to your use case from the list above.
2. **Review the elements** — these are the systems and devices you will need. Check their Status (Existing vs Planned) to understand what is already deployed.
3. **Look up the functional requirements** — these define WHAT each element must do. They map directly to RFP/RFI specification sections.
4. **Check the interfaces** — these define HOW elements communicate. Each interface specifies data flows and applicable standards.
5. **Reference the standards** — for each interface, the architecture specifies which standards (NTCIP, TMDD, SAE, IEEE, etc.) should be used.

For a DOT preparing an RFI/RFP, the functional requirements are your specification backbone. Each requirement can be traced from service package → element → functional requirement → interface → standard.

--- Halaman 1 ---
 
 
      
      
    
  
B 02 April 2026 IFD HA EO/NAR/KAR YP/SPS 
A 26 February 2026 IFR HA EO/NAR/KAR YP/SPS 
Rev Date Document Status Prepared by TTJ Checked by TTJ Approved by TTJ 
 
Company Document Number Contractor Document Number Contract Number 
AF844-AT-REP-00001 220647C-8441-RT-1532-00001 MAS/2023/0018  
 
 
 
Vendor Document Number PO/Contract number Document Class Project Code 
ET-25042-GEN-RPT-003  220647C001P1138 2 FPB 
TechnipEnergies | General | Anyone - No ProtecƟon 
 
 
 
 
  
  
 
 
INPEX Masela, Ltd. 
Abadi LNG Project 
 
 
 
 
 
RADIO COMMUNICATION COVERAGE STUDY 
 
 
  
  
 
 
  
 
Information Security Classification: 
 B: Business Information 
Mohd Nazri Abd Rahman 3 
2026.04.03 23:09:29 +08'00'
Sylviaprese
nna 
Samuelinba
raj 
2026.04.03 
23:14:28 
+08'00'
Ir. Khairil Anwar 
2026.04.03 
23:19:25 +08'00'


--- Halaman 2 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code: FPB 
 
 02-Apr-26 Information Security Classification   B: Business Information    8 of 73 
  
1. Project Background 
The Abadi Field is located in the Masela Block in the Arafura Sea, Maluku Province, which is 
located more than 12 miles from the nearest island. The Masela Block is located approximately 
750 km south of Ambon, the capital city of Ma luku Province. Water depth in the field ranges 
from 400 m to 800 m. The southern boundary of the block is adjacent to the agreed Indonesia-
Australia maritime border. The entire block is located in Indonesia side (no cross border). 
 
 
Figure 1-1: Abadi Field Location 
 
There are no existing production fa cilities in the proximity of the Abadi Field, therefore the 
development plan for the Abadi Field is planned to consist of subsea facilities (including 
subsea wellheads, drilling centers, Subsea Um bilicals Risers and Flowlines (SURF), CO 2 
injection well, and SURF for CCS facility), Floating Production Storage and Offloading (FPSO) 
facility, Gas Export Pipeline (GEP) and CO 2 pipeline, and an Onshore LNG (OLNG) plant 
including Onshore CCS facility located at  Yamdena Island in Kepulauan Tanimbar Regency 
(KKT).  
The FPSO contains 2-train gas processing facility to export dry gas to the LNG processing 
facility in onshore (OLNG) through the GEP where the throughput production in OLNG is 9.5 
MTPA consists of 2 trains of 4.75 MTPA and 150 MMSCFD gas pipe for other industries built 
by others.  
The CO2 from the Acid Gas Removal Unit (AGRU) of LNG trains is dehydrated and 
compressed. The CO2 is sent to a subsea injection well at Abadi field through the 
CCS pipeline installed parallel to the GEP. 


--- Halaman 3 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              9 of 73 
 
Information Security Classification   B: Business Information  
2. Abbreviation, Definition & Reference Document 
2.1. Abbreviation 
Table 2-1: Abbreviation 
Abbreviation Definition 
AIOC Abadi Integrated Operating Center 
AM Amplitude Modulation 
AGRU Acid Gas Removal Unit 
CCR Central Control Room 
CRS Comment Resolution Sheet 
EIRP Effective Isotropic Radiated Power 
EPCIC Engineering, Procurement, Constr uction, Installation and Commissioning 
EPIRB Emergency Position Indicating Radar Beacon 
ERB Emergency Response Base 
FEED Front End Engineering Design 
FM Frequency Modulation 
FO Fiber Optic 
FPCI FEED, Procurement, Construction and Installation 
FPSO Floating Production Storage and Offloading 
GEO Geostationary Earth Orbit 
GPS Global Positioning System 
ICC Incident Command Centre 
ICSS Integrated Control and Safety System 
IER Instrument Equipment Room 
IFD Issued for design 
IFR Issued for review 
MF/HF Medium Frequency/High Frequency 
NDB Non-Directional Beacon 
OLNG Onshore LNG 
OMU Optical Master Unit 
ORU Optical Remote Unit 
RACON Radar Beacon 
RSSI  Received Signal Strength Indicator 
SOW Scope of work 
TER Telecommunication Equipment Room 
UHF Ultra-High Frequency 
VHF Very High Frequency 

--- Halaman 4 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              10 of 73 
 
Information Security Classification   B: Business Information  
2.2. Definition 
Table 2-2: Definition 
Term Definition 
PROJECT FPCI For Floating Production Storage and Offloading Vessel (FPSO) 
(FEED Phase) 
COMPANY INPEX Masela, Ltd 
CONTRACTOR CONSORTIUM TTJ 
VENDOR The party that manufactures or supplies equipment and services to 
perform the duties specified by the CONTRACTOR. 
Shall “Shall” is used where a provision is mandatory. 
2.3. Reference Document 
2.3.1. Company Document 
Table 2-3: Company Document 
No Document Number Document Title 
1. O2120-TC-PHI-00001_03 Telecommunication Philosophy 
2. O2190-GE-SPC-00001 Specification – Engineering Units 
3. O2120-PF-LIS-00001 FPSO Applicable Codes & Standards 
4. O2120-PF-BOD-00001 FPSO FEED Basis of Design 
5. O2120-SF-PHI-00003 FPSO Safety Philosophy for FEED 
6. O2120-EL-PHI-00001 Electrical Design Philosophy 
7. O2120-IN-PHI-00001 Instrumentation and Control Philosophy 
8. O2120-SF-PHI-00005 Fire and Gas Detection Philosophy 
9. O2190-IC-BOD-00002 Integrated Basis of Design Abadi Integrated Operating Centre 
(AIOC) 
10. O2190-IC-SPC-00002 General Specification for Integrated Control and Safety 
System 
11. O2190-SC-PHI-00001 Security Philosophy 
12. O2120-MS-PHI-00002 Painting and Insulation Philosophy 
13. O2190-IF-PHI-00001 Tagging Philosophy  
14. A4300-999-IF-PHI-0001 Cyber Security for Asset Facility Philosophy 
15. Exhibit E COMPANY SUPPLIED DATA 
16. C0070-999-GE-POL-0001 COMPANY HSSE Policy 
17. C0070-999-GE-STD-0001 COMPANY Life-Saving Rules Standard 
18. C0070-999-HE-POL-0001 COMPANY Drugs and Alcohol Policy 
19. C0070-999-GE-PRC-0001 COMPANY Stop Work Authority Procedure 
20. C0070-999-SF-POV-0006 Transport Safety Management Process Overview 
21. C0100-999-SF-PRC-0001 Marine Operations Safety Manual 

--- Halaman 5 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              11 of 73 
 
Information Security Classification   B: Business Information  
No Document Number Document Title 
22.. AF901-DX-LAD-00001.001 Overall Equipment Layout Arrangement of Topsides Level 1 
23. AF901-DX-LAD-00002.001 Overall Equipment Layout Arrangement of Topsides Level 2 
24. AF901-DX-LAD-00003.001 Overall Equipment Layout Arrangement of Topsides Level 3 
and above 
25. AF780-DE-LAD-00001.002 Electrical Room Layouts for Topsides - Level 1 
26. AF780-DE-LAD-00001.003 Electrical Room Layouts for Topsides - Level 2 
27. AF780-DE-LAD-00001.004 Electrical Room Layouts for Topsides - Level 3 
28. AF780-DE-LAD-00001.005 Electrical Room Layouts for Topsides - Level 4 
29. AF780-DE-LAD-00001.006 Electrical Room La youts for Topsides - Instrument Equipment 
Building Level 4 
30. AF780-DE-LAD-00001.007 Electrical Room La youts for Topsides - Instrument Equipment 
Building Level 5 
31. AF902-DX-LAD-00011.001 Equipment Layout Drawing for AFT Machinery Space level 1 
32. AF902-DX-LAD-00012.001 Equipment Layout Drawing for AFT Machinery Space level 2 
33. AF902-DX-LAD-00013.001 Equipment Layout Drawing for AFT Machinery Space level 3 
34. AF902-DX-LAD-00014.001 Equipment Layout Drawing for AFT Machinery Space level 4 
35. AF902-DX-LAD-00018.001 Equipment Layout Drawing for Forward Machinery Space 
level 1 
36. AF902-DX-LAD-00019.001 Equipment Layout Drawing for Forward Machinery Space 
level 2 
37. AF902-DX-LAD-00020.001 Equipment Layout Drawing for Forward Machinery Space 
level 3 
38. AF902-DX-LAD-00021.001 Equipment Layout Drawing for Forward Machinery Space 
level 4 
39. AF910-DC-GAD-20700.003 General Arrangement Living Quarter Level 1 
40. AF910-DC-GAD-20700.004 General Arrangement Living Quarter Level 2 
41. AF910-DC-GAD-20700.005 General Arrangement Living Quarter Level 3 
42. AF910-DC-GAD-20700.006 General Arrangement Living Quarter Level 4 
43. AF910-DC-GAD-20700.007 General Arrangement Living Quarter Level 5 
44. AF910-DC-GAD-20700.008 General Arrangement Living Quarter Roof 
2.3.2. Project Documents 
Table 2-4: Project Documents 
No Document Number Document Title 
1. AF844-AT-SPC-00003-FPB VHF AM Aeronautical Radio System Specification 
2. AF844-AT-SPC-00005-FPB VHF FM Marine Radio System Specification 
3. AF844-AT-SPC-00004-FPB MF/HF Radio System Specification 
4. AF860-AT-SPC-00001-FPB Non-Directional Beacon System Specification 

--- Halaman 6 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              12 of 73 
 
Information Security Classification   B: Business Information  
No Document Number Document Title 
5. AF844-AT-SPC-00001-FPB UHF Two Way Radio System Specification 
6. AF840-DT-BLD-00001.001-FPB Overall Telecommunication Architecture Block Diagram 
7. AF844-AT-SPC-00004-FPB MF/HF Radio System Block Diagram 
8. AF844-DT-BLD-00001.001-FPB UHF Two Way Radio System Block Diagram 
9. AF861-DT-BLD-00002.001-FPB Marine Collision Avoidance Radar System Block 
Diagram 
2.3.3. Project Document – Applicable Laws, Codes and Standards 
Design / deliverables shall comply with the latest revision of applicable Indonesian government 
regulations, laws and decrees. Any revisions / m odifications in codes and standards shall be 
promptly raised to the attention of CONTRACTOR for further discussion with the COMPANY. 
2.3.4. Indonesian Law and Regulation 
Table 2-5: Indonesian Law and Regulation 
No Document Number Document Title 
1. Undang Undang Republik 
Indonesia No. 36 tahun 1999 
Tentang Telekomunikasi (Act of Republic of Indonesia 
number 36, year 1999) 
2. Peraturan Pemerintah Republik 
Indonesia No. 52 tahun 2000 
Tentang Penyelenggaraan Telekomunikasi (Regulation 
of Government of Republic Indonesia number 52, year 
2000) 
3. Keputusan Presiden RI No.63 
tahun 2004  
Tentang Pengamanan Obyek Vital Nasional 
(Presidential Decree no.63/2004)  
4. Peraturan Menteri Perhubungan 
Nomor KM 8 Tahun 2005 
Tentang Telekomunikasi Pelayaran 
5. Keputusan Direktur Jenderal 
Perhubungan Laut Nomor 
kp.287/DJPL/2020 
Petunjuk Teknis Standarisasi Peralatan Vessel Traffic 
Services (VTS) dan Station Radio Pantai (SROP) Pada 
Distrik Navigasi. 
6. Peraturan Menteri Perhubungan 
No 4 Tahun 2023 
Tentang Penyelenggaraan Telekomunikasi Pelayaran 
dan Pelayanan Tata Kelola Lalu Lintas Kapal di 
Perairan Indonesia 
7. Peraturan Menkominfo No. 1 
Tahun 2010 
Tentang Penyelenggaraan Jaringan Telekomunikasi 
8. Peraturan Menkominfo No.38 
Tahun 2014 
 
Perubahan atas Peraturan Menteri Komunikasi dan 
Informatika Nomor :  
01/PER/M.KOMINFO/01/2010  
9. Peraturan Menkominfo No.7 
Tahun 2015 
Perubahan Kedua atas Peraturan Menteri Komunikasi 
dan Informatika Nomor :  
01/PER/M.KOMINFO/01/2010  
10. Peraturan Menkominfo No.9 
Tahun 2018 
Tentang Tata Cara Perizinan dan Ketentuan 
Operasional Penggunaan Spektrum Frekuensi Radio 

--- Halaman 7 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              13 of 73 
 
Information Security Classification   B: Business Information  
No Document Number Document Title 
11. Peraturan Menkominfo No.1 
Tahun 2019 
Tentang Penggunaan Spektrum Frekuensi Radio 
Berdasarkan Izin Kelas 
12. Peraturan Menkominfo No.3 
Tahun 2024 
Ketentuan Operasional Sertifikasi Alat dan Perangkat 
Telekomunikasi 
13. Peraturan Menteri Perhubungan 
No 25 Tahun 2011  
Tentang Sarana Bantu Navigasi Pelayaran  
14. Peraturan Direktorat Jenderal  
Pos dan Telekomunikasi No 
266 Tahun 2005  
Tentang Persyaratan Teknis Alat dan Perangkat Radio 
Maritim  
2.3.5. International Codes and Standards 
Table 2-6: International Codes and Standards 
No Document Number Document Title 
1. CAP437 Offshore Helicopter Landing Areas 
2. EIA/TIA 568 Commercial Building Wiring Standards 
3. IALA The IALA Maritime Buoyage System for Region A 
4. ICAO annex 10 Aeronautical telecommunications vol. I 
5. IEC 60065 Audio, video and similar electronic apparatus – safety 
requirements 
6. IEC 60079 Explosive atmospheres –Part 0 to 18 
7. IEC 60092 Electrical installations in ships (Relevant parts) 
8. IEC 60092-374 Electrical installations in ships- Part 374: Shipboard 
telecommunications cables and radio-frequency cables. 
Telephone cables for nonessential communication services 
9. IEC 60092-375 Electrical installations in ships- Part 375: Shipboard 
telecommunication cables and radio-frequency cables. General 
instrumentation, control and communication cables 
10. IEC 60096 Radio frequency cables 
11. IEC 60331 Tests for electric cables under fire conditions – Circuit integrity 
12. IEC 60332 Tests on electric and optical fibre cables under fire conditions 
13. IEC 61034 Measurement of smoke density of cables burning under 
defined conditions 
14. IEC 60754 Test on gases evolved during combustion of materials from 
cables 
15. IEC 60529  Classification of degrees of protection provided by enclosures 
(IP Code) 
16. IEC 60794-1-1 Optical Fiber Cables: Part 1-1: Generic Specification – General 
17. IEC 60794-1-2 Optical Fiber Cables: Part 1-2: Generic Specification – Basic 
Optical Cable Test Procedures 
18. IEC 60849 Sound Systems for Emergency Purposes 
19. IEC 60945  Maritime navigation and radio communication equipment and 
systems 

--- Halaman 8 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              14 of 73 
 
Information Security Classification   B: Business Information  
No Document Number Document Title 
20. IEC 61000 Electroma gnetic Compatibility (EMC) 
21. IEC 61097 Global Maritime Distress and Safety System (GMDSS) 
22. IEC 61892 (Series)  Mobile and fixed offshore units 
23. IEC 62264 Enterprise-control system integration 
24. IEEE 802 Standards for local and metropolitan area networks 
25. IEEE 802.1P LAN layer #2 QoS and CoS protocol for traffic prioritization 
26. IEEE 802.3 Standard for Ethernet 
27. IEEE 802.11 Wireless LANs 
28. ISO/IEC 
27000/27001/27002 
Information Security, Cybersecurity and Privacy Protection 
29. ITU-R M.493-13 (10/09) Digital selective-calling system for use in the maritime mobile 
service 
30. ITU-R M.689-2 (09/94) International maritime VHF radiotelephone system with 
automatic facilities based on DSC signalling format 
31. ITU-R P.528-5 Propagation curves for aeronautical mobile and radio 
navigation services using the VHF, UHF and SHF bands 
32. ITU-T G.711 Pulse code modulation (PCM) of voice frequencies 
33. ITU-T G.729 Coding of speech at 8 kbps using conjugate-structure 
algebraic-code-excited linear prediction (CS-ACELP) 
34. ITU-T I.324 ISDN network architecture 
35. ITU-T Q.921 ISDN user-network interface – Data link layer specification 
36. ITU-T T.4 Standardisation of Group 3 facsimile apparatus 
37. ITU-T T.6 Standardisation of Group 4 facsimile apparatus 
38. ITU-R P.452.15 Prediction procedure for the evaluation of interference between 
stations on the surface of the Earth at frequencies above about 
0.1 GHz 
39. IMO – SOLAS ch III/6   Communication 
40. IMO – SOLAS ch XI   International Ship and Port Facility Security Code (ISPS Code) 
41. TIA-598-D Optical Fiber Cable Colour Coding 
42. BS 6656 Assessment of inadvertent ignition of flammable atmospheres 
by radio-frequency radiation Guide 
2.4. Order of Precedence 
If there is any inconsistency between any of the applicable regulations, codes and standards; 
the following order of precedence shall apply to resolve the inconsistency: 
• Indonesian Government Regulations, Laws and Decrees 
• Indonesian Codes and Standards 
• Class Society rules 
• Project Specifications and Material Requisition 
• Other documents in COMPANY SUPPLIED DATA 
• International Codes and Standards 

--- Halaman 9 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              15 of 73 
 
Information Security Classification   B: Business Information  
3. Purpose 
The purpose of this radio comm unication coverage study report is to describe and evaluate 
the coverage performance of the various co mmunication systems installed on the ABADI 
FPSO. 
4. Scope 
This document provides the Radio communication coverage study for ABADI FPSO Project. 
A set of radio coverage studies shall be performed to confirm the area of coverage of the 
radio communication systems installed on the FPSO:  
• UHF Two –Way Radio System 
• VHF-FM Marine Radio System  
• VHF-AM Aeronautical Radio System  
• MF-HF Radio System 
• Non-Directional Beacon System 
• Crane Radio (VHF-FM & UHF) 
• TEMPSC Radio (VHF-FM) 
•  Liferaft Radio System (VHF-FM) 
• Fast Rescue Craft/FRC (UHF) 
5. Simulation Software 
5.1. Simulation Modelling & Methodology 
The radio coverage study will be conducted us ing ATDI Simulation Software version 2024.3 
provided by HTZ Communication. The ATDI software will be utilized to perform radio system 
coverage calculations for the ABADI FPSO. The software can generate coverage predictions 
and heatmap reports for both indoor and outdoor environments. The UHF coverage simulation 
will be carried out using a background image of the FPSO layout. Other radio systems, 
including VHF-FM, VHF-AM, MF-HF and NDB, w ill be simulated using approximate FPSO 
coordinate data. 
The simulation modelling will be carried out in the following steps: 
1. Radio Coverage Modelling 
Radio coverage modelling in ATDI software is  performed by adding the base station and 
defining the relevant parameters, such as tr ansmit power, antenna gain or EIRP of the base 
station or handheld radio, and selecting the app ropriate antenna type for the radio source. 
The ATDI software provides an antenna databa se that includes polar plot diagrams and 
antenna directivity information. 
2. Background Layout 
The background image used for the simulation is the FPSO layout. 
3. Radio Site Creation 

--- Halaman 10 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              16 of 73 
 
Information Security Classification   B: Business Information  
For simulations using a background image, after creating objects such as walls and structures, 
the radio site object will be added at a location with sufficient availability of the signal. 
For simulations using coordinates, radio sites will be added at the specified coordinate points. 
The radio site is defined as the base station or handheld radio, and the parameters will be set 
according to the equipment datasheet. T hese parameters include such as Frequency, 
Transmit power (dBm), Antenna gain (dBi), Syst em losses (dB), Antenna installation height, 
Tx/Rx bandwidth. 
4. Object Creation. 
After completing the background layout, objects such as walls and structures that may impact 
the radio coverage study will be created. Appropriate attenuation values will then be assigned 
to each object. 
5. Coverage Heat-Map Report 
A coverage heat-map report will be produced as part of the study results. There are two 
categories of coverage reports: 
• Downlink coverage – coverage from base station to handheld radio  (VHF-FM/UHF) 
• Uplink coverage – coverage from handheld radio to base station (VHF-FM/UHF) 
• Downlink coverage - coverage from helicopter to base station (VHF-AM) 
• Uplink coverage – coverage from base station to helicopter (VHF-AM) 
6. Run The Simulation. 
After all parameters and objects are creat ed, the calculation can be initiated. 
The software calculates the signal strength based on the base station location, antenna height, 
and EIRP. The results are presented as a heat  map with different colours representing 
different levels of received signal strength indication (RSSI). 
5.2. Simulation Parameters 
Parameters to be used on the software modelling for radio coverage study are shown in below 
table. 
Table 5-1: Software Parameters 
Parameter Description Parameter Value 
Propagation Method ITU-R-528-5 
Diffraction Geometry Delta Bullington 
Sub-path attenuation Delta Bullington 
Coordinate of FPSO E: 130.455399, N: -9.170600 
Outdoor Rx Antenna Height Deck Level 1 – 43.5m 
Deck Level 2 – 52.5m   
Deck Level 3 – 61.5m 
Frequency Range* UHF Radio  : 403 MHz - 470 MHz 

--- Halaman 11 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              17 of 73 
 
Information Security Classification   B: Business Information  
Parameter Description Parameter Value 
VHF - FM Radio : 156 MHz - 164 MHz 
VHF - AM Radio :  118 MHz - 137 MHz 
MF-HF Radio : 150 kHz - 30 MHz 
 
Below figure shows the propagation method us ed for the software simulation of outdoor 
coverage study. 
 
Figure 5-1: Propagation Method for Outdoor Coverage Study 
5.3. Manual Calculation for Diffraction Loss 
To perform diffraction analysis, several key par ameters must first be defined. These include 
the operating frequency (f), from which the wavelength (λ) is derived using the relation λ = c/f, 
where c is the speed of light. The geometry of the path is described by the total link distance 
(d), as well as the distances from  the transmitter to the obstruction (d ₁) and from the 
obstruction to the receiver (d₂),  
where d = d₁ + d₂. 
Additionally, antenna heights at the transmitter (h ₜ) and receiver (hᵣ), along with the height of 
any intervening obstacle (hₒ), are required. For long-distance links, Earth curvature correction 
may also be considered. 
A critical step in the analysis is determining the effective height of the obstruction relative to 
the LOS path. This is calculated as the difference between the obstacle height and the height 
of the straight LOS line(h). 
ℎൌ  ℎ௢ −ℎ ௅ைௌ 
If this value is positive, the obstacle obstructs the LOS and causes diffraction loss. 
The diffraction effect is quantified using the Fresnel–Kirchhoff diffraction parameter (v), which 
depends on the geometry of the path, wavelength, and obstruction height. Based on the value 
of this parameter, the knife-edge diffraction loss can be calculated using an empirical formula, 
providing the additional signal attenuation in decibels (dB). 


--- Halaman 12 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              18 of 73 
 
Information Security Classification   B: Business Information  
𝑳𝒅 = 𝟔. 𝟗 + 𝟐𝟎𝐥𝐨𝐠 𝟏𝟎 ቀඥሺ𝒗−𝟎 . 𝟏)𝟐 + 𝟏 + 𝒗−𝟎 . 𝟏ቁ                    Equation 1 
Where Ld is the diffraction loss 
For more realistic terrain profiles involving multiple obstacles, the Bullington method is widely 
used. This approach simplifies the terrain in to an equivalent single dominant obstacle by 
identifying the point with the maximum slope relati ve to the transmitter. This point is then 
treated as a knife edge, and the diffraction loss is calculated accordingly. 
Coverage Study – UHF Two-Way Radio System 
6.1. Radio Coverage Study 
The objective of the UHF radio coverage study is to provide a radio coverage analysis for UHF 
radio communication throughout the entire ABADI FPSO. 
A UHF two-way radio system shall be installed on the FPSO to enable communication 
between hand-portable radios, base stations and Fixed radio at FRC. The system will support 
operational, maintenance, and safety communicat ions within the FPSO and shall allow radio 
communication to and from any location, including the Top side, Living Quarters (LQ), Machine 
Control Room, and Hull during operations. 
Indoor FPSO locations, such as the LQ, Electr ical Equipment Building, and hull decks, shall 
be covered by a distributed antenna system (DAS) incorporating UHF indoor repeaters. 
6.2. Assumption and Consideration 
UHF Radio Coverage study shall consider below assumption and consideration: 
1. All outer walls are considered as metal with 15dB attenuation. 
2. A fade margin of 15 dB is considered to accommodate signal fluctuations in the outdoor 
environment, while a fade margin of 10 dB is considered for indoor conditions 
3. 10dB floor attenuation considered to get coverage to deck without antenna from the 
neighbouring decks. 
4. For indoor coverage transmitter height is assumed to be height of the ceiling with 
respect to each level and Receiver antenna height is considered to be 1.5m (a man 
holding the radio) with body loss 6 dB. 
6.3. Antenna Distribution Diagram 
This DAS layout shows a dual-system (TER A and TER B) architecture designed to provide 
reliable indoor and outdoor radio coverage with redundancy. Each system consists of 
repeaters connected to a combiner/duplexer and an outdoor antenna (mounted on a telecom 
mast or flare tower) to deliver wide-area cove rage. Both systems are interconnected through 
a LAN network. Optical Remote Unit (ORU) shal l be distributed across to achieve maximum 
coverage for all the locations such as Living Quarters, AFT Machinery Deck, LER and Forward 
Machinery Deck. 

--- Halaman 13 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              19 of 73 
 
Information Security Classification   B: Business Information  
ORU unit power output is limited to 30dBm for the simulation, and to be distributed to the 
Indoor antennas The transmitted power to indivi dual antenna will be calculated based on the  
power output from the OMU, and will be reduced by the coaxial cable attenuation, 6-way 
splitters and connectors and to be amplified by the antenna gain. 
During normal operation, traffic is shared between systems A and B to optimize performance, 
while in case one system fails, the other can take over completely, ensuring uninterrupted 
communication. In this design, outdoor coverage is provided by both systems, whereas indoor 
coverage is primarily handled by system A, making the setup both efficient and fault tolerant. 
The UHF antenna distribution for TER-1 and TER-2 is shown on the below figure and will be 
the main reference for the link budget calculation for each individual outdoor and indoor 
antenna. 
 
 
Figure 6-1: UHF Antenna distribution diagram for TER - 1 


--- Halaman 14 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              20 of 73 
 
Information Security Classification   B: Business Information  
 
 
Figure 6-2: UHF Antenna distribution diagram for TER - 2 
The EIRP for individual will be calculated for the simulation parameters, which is shown in the 
next sub-chapter. 
The indoor antennas will be distributed to different floors and Levels at the Living Quarter (LQ), 
LER, AFT Machinery Deck and FWD Machinery Deck. 
6.4. Simulation Parameters 
1. UHF RADIO REPEATER PARAMETERS 
UHF Radio repeaters parameters are as follow:  
Parameter Description Parameter Value 
Transmit Power  25W / 43.98 dBm 
Receiving Sensitivity (12dB SINAD) 0.3 uV (-117 dBm) 
Frequency 40 3 - 470 MHz 


--- Halaman 15 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              21 of 73 
 
Information Security Classification   B: Business Information  
2. HANDHELD RADIO PARAMETERS 
Handheld Radio parameters are as follow: 
Parameter Description Parameter Value 
Transmit Power  1W / 30dBm 
Receiving Sensitivity (12dB SINAD) 0.16 uV (-123 dBm) 
Frequency 403-527 MHz 
OUTDOOR ANTENNA PARAMETERS 
Outdoor antenna parameters are as follow: 
Parameter Description Parameter Value 
Antenna Type Whip Antenna 
Radiational Pattern Omnidirectional 
Gain 6.5 dBi (4.35 dBd) 
4. INDOOR ANTENNA PARAMETERS 
Indoor antenna parameters are as follow: 
Parameter Description Parameter Value 
Antenna Type Ceiling Antenna 
Radiational Pattern Omnidirectional 
Gain 2.5 dBi (0.35 dBd) 
6.5. Link budget Calculation 
6.5.1. Effective Isotropic Radiated Power (EIRP) Calculation 
Radio coverage study for UHF radio system will be modelled from the Radio Repeater antenna 
to the handheld Radio. The coverage method will be provided for downlink coverage from the 
Radio Repeater to the handheld radio, since the EIRP of Handheld radio is lower than the 
Radio Repeater. 
EIRP (Effective Isotropic Radiated Power) is a calculation used to estimate the radiated output 
power of an isotropic antenna (a theoretical half wave dipole antenna that radiates perfectly 
in all directions). This formula will in clude the transmitter output power, and antenna gain. 
EIRP for the Radio Repeater can be calculated with below formula:   
      EIRP = Transmit Power – Losses + Antenna Gain.  
EIRP for Radio Repeater with Omni antenna and handheld radio are shown in below sub-
chapter. 
6.5.2. Calculation of Received Signal Strength Indicator (RSSI) Threshold 
RSSI stands for Received Signal Strength Indica tor. It is an estimated measure of the power 
level which is received by handheld radio. The further the distances, the weaker the received 
Signal. RSSI for the handheld Radio can be derived from below formula:  

--- Halaman 16 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              22 of 73 
 
Information Security Classification   B: Business Information  
    RSSI (handheld) = Radio Repeater EIRP – Propagation Loss  
Propagation Loss consists of Free Space Loss (FSL), Diffraction Los and Body Loss. 
There is a minimum RSSI required by the handheld radio to receive adequate signal level, to 
maintain the two-way communications from Radio Repeater to handheld (downlink). Higher 
received power will provide better two-way communication.  
RSSI threshold for Radio Repeater and handheld will be different and depends on the total 
loss and gain on the system, receiver sens itivity and Fade margin parameters for outdoor 
environment. The RSSI threshold can be derived from below formula:  
  RSSI Threshold = Receiver Sensitivity – (all Losses + Antenna Gain) + Fade Margin 
A. RSSI THRESHOLD FOR UHF RADIO REPEATER 
Parameter Description Parameter Value 
Receiver Sensitivity -117 dBm 
Antenna Gain 6.5 dBi 
Combiner/Duplexer + cable Loss - 17.33 dB 
Fade Margin 1 5 dB 
RSSI Minimum threshold - 91.17 dBm 
B. RSSI THRESHOLD FOR HANDHELD RADIO 
Parameter Description Parameter Value 
Receiver Sensitivity -123 dBm 
Antenna Gain 2.15 dBi 
Body Loss -6 dB 
Fade Margin 1 5 dB 
RSSI Minimum threshold -10 4.15 dBm 
6.5.3. System Margin 
Link budget calculation will be carried out to show the design margin availability from the radio 
system design. Downlink link bu dget calculation refers to the radio link calculation from the 
base station to the handheld radio. 
All losses / attenuations, gains and free spac e loss will be considered into link budget 
calculation, to get the predicted RSSI signal at handheld radio.  The RSSI signal level will be 
compared with the RSSI threshold, to calculate the system margin. The bigger the margin, the 
better the quality of two-ways communication, and vice versa.  
Effective Isotropic Radiated Power (EIRP)  for each individual indoor antenna can be 
summarized in the below table.  Initial coverage study will consider approximate cable length, 
and to be finalized during detailed engineering design. 
  

--- Halaman 17 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              23 of 73 
 
Information Security Classification   B: Business Information  
DOWNLINK CALCULATION 
Repeaters   Value  Unit L (m) 
Repeater Tx Power (Watt) 25.00 Watt   
Repeater Tx Power (dBm) 43.98 dBm   
Combiner/Duplexer Loss -7.80 dB   
Connector Loss -1.20 dB  
Cable Loss (Repeater – Combiner – Duplexer) -0. 36 dB 4 
EIRP (dBm) 34.62 dBm   
Location: TELECOM MAST 
Link 1   Value  Unit L (m) 
Branch #01 (Antenna 01)       
Transmit Power (Tx) 34.62 dBm   
Lightning Arrestor (Connector loss) -0. 10 dB   
Connector Loss -1.20 dB  
Cable Loss (Duplexer to Antenna) -6.68 dB 75 
Antenna Gain 6.50 dBi   
Antenna EIRP 33.14 dBm   
OPTICAL REMOTE UNIT #1 
Location: LIVING QUARTERS 
Link 2   Value  Unit L (m) 
ORU - 1       
Tx Power from ORU 30.00 dBm   
Connector loss -0.30 dB   
Cable Loss (Amplifier to Splitter) 0.89 dB 10 
Splitter loss -9.20 dB   
EIRP (dBm) 19.61 dBm   
Location: LQ – LEVEL 5 
Antenna Link 02-01   Value  Unit L (m) 
Transmit power Tx 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -1.34 dB 15 
Antenna Gain 2.50 dBi   
Antenna EIRP 20.48 dBm   
Location: LQ – LEVEL 4  
Antenna Link 02-02   Value  Unit L (m) 
Transmit power Tx 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -2.23 dB 25 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.59 dBm   

--- Halaman 18 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              24 of 73 
 
Information Security Classification   B: Business Information  
Location: LQ - LEVEL 2 
Antenna Link 02-03   Value  Unit L (m) 
Transmit power Tx 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -4.01 dB 45 
Antenna Gain 2.50 dBi   
Antenna EIRP 17.81 dBm   
Location: LQ - LEVEL 1 
Antenna Link 02-04   Value  Unit L (m) 
Transmit power Tx 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -4.90 dB 55 
Antenna Gain 2.50 dBi   
Antenna EIRP 16.92 dBm   
Location: LQ – TOPSIDE DECK - CCR 
Antenna Link 02-05   Value  Unit L (m) 
Transmit power Tx 19.61  dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -5.79  dB 65 
Antenna Gain 2.50  dBi   
Antenna EIRP 16.03  dBm   
Location: LQ – TOPSIDE DECK – OPEN SPACE 
Antenna Link 02-06   Value  Unit L (m) 
Transmit power Tx 19.61  dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -5.96  dB 67 
Antenna Gain 2.50  dBi   
Antenna EIRP 15.85  dBm   
 
  

--- Halaman 19 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              25 of 73 
 
Information Security Classification   B: Business Information  
OPTICAL REMOTE UNIT #2 
Location: AFT MACHINERY SPACE - LEVEL B - INSTRUMENT ROOM 
Link 3   Value  Unit L (m) 
ORU - 2       
Tx Power from ORU 30.00  dBm   
Connector loss -0.30  dB   
Cable Loss (Amplifier to Splitter) 0.89  dB 10 
Splitter loss -9.20  dB   
EIRP (dBm) 19.61  dBm   
Location: AFT MACHINERY SPACE - LEVEL B  
Antenna Link 03-01   Value  Unit L (m) 
Transmit Power (Tx) 19.61  dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -1.34  dB 15 
Antenna Gain 2.50  dBi   
Antenna EIRP 20.48  dBm   
Location: AFT MACHINERY SPACE - LEVEL B  
Antenna Link 03-02   Value  Unit L (m) 
Transmit Power (Tx) 19.61  dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -1.51  dB 17 
Antenna Gain 2.50  dBi   
Antenna EIRP 20.30 dBm   
Location: AFT MACHINERY SPACE - LEVEL A 
Antenna Link 03-03   Value  Unit L (m) 
Transmit Power (Tx) 19.61  dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -1.20  dB 25 
Antenna Gain 2.50  dBi   
Antenna EIRP 20.61  dBm   
Location: AFT MACHINERY SPACE - LEVEL A 
Antenna Link 03-04   Value  Unit L (m) 
Transmit Power (Tx) 19.61  dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -1.30  dB 27 
Antenna Gain 2.50  dBi   
Antenna EIRP 20.51  dBm   
 
  

--- Halaman 20 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              26 of 73 
 
Information Security Classification   B: Business Information  
OPTICAL REMOTE UNIT #3 
Location: AFT MACHINERY SPACE - LEVEL B - INSTRUMENT ROOM 
Link 4   Value  Unit L (m) 
ORU - 3       
Tx Power from ORU 30.00 dBm   
Connector loss -0.30 dB   
Cable Loss (Amplifier to Splitter) 0.89 dB 10 
Splitter loss -9.20 dB   
EIRP (dBm) 19.61 dBm   
Location: AFT MACHINERY SPACE - LEVEL C 
Antenna Link 03-01   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -2.23 dB 25 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.59 dBm   
Location: AFT MACHINERY SPACE - LEVEL C 
Antenna Link 03-02   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -2.40 dB 27 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.41 dBm   
Location: AFT MACHINERY SPACE - LEVEL D 
Antenna Link 03-03   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -2.23 dB 25 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.59 dBm   
Location: AFT MACHINERY SPACE - LEVEL D 
Antenna Link 03-04   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Slitter to Splitter) -2.4 dB 27 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.41 dBm   
 
  

--- Halaman 21 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              27 of 73 
 
Information Security Classification   B: Business Information  
OPTICAL REMOTE UNIT #4 
Location: ELECTRICAL EQUIPMENT BUILDING - LABORATORY ROOM  
Link 5   Value  Unit L (m) 
ORU - 4      
Tx Power from ORU       30.00  dBm   
Connector loss -0. 30 dB   
Cable Loss (Amplifier to Splitter) -0. 89 dB 10 
Splitter loss - 9.20 dB   
EIRP (dBm) 19.61 dBm   
 Location: ELECTRICAL EQUIPMENT BUILDING - 1ST FLOOR  
Antenna Link 04-01   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -1.34 dB 15 
Antenna Gain 2.50 dBi   
Antenna EIRP 20.48 dBm   
Location: ELECTRICAL EQUIPMENT BUILDING - 2ND FLOOR  
Antenna Link 04-02   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -2.23 dB 25 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.59 dBm   
Location: ELECTRICAL EQUIPMENT BUILDING - 3RD FLOOR 
Antenna Link 04-03   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -3.12 dB 35 
Antenna Gain 2.50 dBi   
Antenna EIRP 18.70 dBm   
Location: ELECTRICAL EQUIPMENT BUILDING - 4TH FLOOR 
Antenna Link 04-04   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -4.01 dB 45 
Antenna Gain 2.50 dBi   
Antenna EIRP 17.81 dBm   

--- Halaman 22 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              28 of 73 
 
Information Security Classification   B: Business Information  
OPTICAL REMOTE UNIT #5 
Location: FWD MACHINERY SPACE – LEVEL C (TER - B) 
Link 6   Value  Unit L (m) 
ORU - 5       
Tx Power from power Amplifier 30.00 dBm   
Connector loss -0. 30 dB   
Cable Loss (Amplifier to Splitter) -0. 89 dB 10 
Splitter loss - 9.2 dB   
EIRP (dBm) 19.61 dBm   
Location: FWD MACHINERY SPACE – LEVEL C  
Branch #05-01 (Antenna 05-01)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -1.34 dB 15 
Antenna Gain 2.50 dBi   
Antenna EIRP 20.48 dBm   
Location: FWD MACHINERY SPACE – LEVEL C  
Branch #05-02 (Antenna 05-02)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -1.51 dB 17 
Antenna Gain 2.50 dBi   
Antenna EIRP 20.30 dBm   
Location: FWD MACHINERY SPACE – LEVEL D 
Branch #05-03 (Antenna 05-03)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -2.23 dB 25 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.59 dBm   
Location: FWD MACHINERY SPACE – LEVEL D 
Branch #05-04 (Antenna 05-04)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -2.40 dB 27 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.41 dBm   
 

--- Halaman 23 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              29 of 73 
 
Information Security Classification   B: Business Information  
OPTICAL REMOTE UNIT #6 
Location: FWD MACHINERY SPACE – LEVEL C (TER - B) 
Link 7   Value  Unit L (m) 
ORU - 6       
Tx Power from power Amplifier 30.00 dBm   
Connector loss -0.30 dB   
Cable Loss (Amplifier to Splitter) -0.89 dB 10 
Splitter loss -9.2 dB   
EIRP (dBm) 19.61 dBm   
Location: FWD MACHINERY SPACE – LEVEL A 
Branch #05-01 (Antenna 05-01)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -3.12 dB 35 
Antenna Gain 2.50 dBi   
Antenna EIRP 18.70 dBm   
Location: FWD MACHINERY SPACE – LEVEL A 
Branch #05-02 (Antenna 05-02)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -3.29 dB 37 
Antenna Gain 2.50 dBi   
Antenna EIRP 18.52 dBm   
Location: FWD MACHINERY SPACE – LEVEL B 
Branch #05-03 (Antenna 05-03)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -2.23 dB 25 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.59 dBm   
Location: FWD MACHINERY SPACE – LEVEL B 
Branch #05-04 (Antenna 05-04)   Value  Unit L (m) 
Transmit Power (Tx) 19.61 dBm   
Connector loss -0.30 dB   
Cable Loss (Splitter to Antenna) -2.40 dB 27 
Antenna Gain 2.50 dBi   
Antenna EIRP 19.41 dBm   
 

--- Halaman 24 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              30 of 73 
 
Information Security Classification   B: Business Information  
6.6. Coverage Study Result 
The coverage heatmap report will be provided for Downlink map, from the Radio Repeater to 
the Handheld radio for the Indoor and Outdoor 
6.6.1. LQ – Topside Deck 
   
Figure 6-3: Downlink Coverage for LQ - Topside Deck 
6.6.2.  LQ – Level 1 
   
Figure 6-4: Downlink Coverage for LQ – Level 1 


--- Halaman 25 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              31 of 73 
 
Information Security Classification   B: Business Information  
6.6.3. LQ – Level 2 
 
   
Figure 6-5: Downlink Coverage for LQ – Level 2 
6.6.4. LQ – Level 3 
 
 
Figure 6-6: Downlink Coverage for LQ – Level 3 


--- Halaman 26 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              32 of 73 
 
Information Security Classification   B: Business Information  
6.6.5. LQ – Level 4 
    
Figure 6-7: Downlink Coverage for LQ – Level 4 
6.6.6. LQ – Level 5 
 
 
 Figure 6-8: Downlink Coverage for LQ – Level 5 
6.6.7. LQ – Hull Deck 
 
  
 Figure 6-9: Downlink Coverage for LQ - Hull Deck 


--- Halaman 27 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              33 of 73 
 
Information Security Classification   B: Business Information  
6.6.8. AFT Machinery Room Level A 
    
Figure 6-10: Downlink Coverage for AFT Machinery Room Level A 
6.6.9. AFT Machinery Room Level B 
    
Figure 6-11: Downlink Coverage for AFT Machinery Room Level B 


--- Halaman 28 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              34 of 73 
 
Information Security Classification   B: Business Information  
6.6.10. AFT Machinery Room Level C 
    
Figure 6-12: Downlink Coverage for AFT Machinery Room Level C 
6.6.11. AFT Machinery Room Level D 
 
 
 
 
Figure 6-13: Downlink Coverage for AFT Machinery Room Level D 


--- Halaman 29 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              35 of 73 
 
Information Security Classification   B: Business Information  
6.6.12. Electrical Equipment Building Level 1 
 
Figure 6-14: Downlink Coverage for Electrical Equipment Building Level – 1 
6.6.13. Electrical Equipment Building Level 2 
   
Figure 6-15: Downlink Coverage for Electrical Equipment Building Level – 2 


--- Halaman 30 ---
RADIO COMMUNICATION COVERAGE 
STUDY 
Company Doc No:  AF844-AT-REP-00001 
Revision:  B 
Project Code:  FPB 
 
02-Apr-26              36 of 73 
 
Information Security Classification   B: Business Information  
6.6.14. Electrical Equipment Building Level 3 
 
  
Figure 6-16: Downlink Coverage for Electrical Equipment Building Level – 3 
6.6.15. Electrical Equipment Building Level 4 
   
Figure 6-17: Downlink Coverage for Electrical Equipment Building Level – 4 

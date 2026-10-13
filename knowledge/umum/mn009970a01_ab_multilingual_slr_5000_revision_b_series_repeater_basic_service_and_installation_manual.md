--- Halaman 1 ---
SLR 5000 Revision B Series
Repeater Basic Service and
Installation Manual
System Release M2022.03
MOTOTRBO™ REPEATER
PROFESSIONAL DIGITAL TWO-WAY RADIO SYSTEM
OCTOBER 2023
© 2023 Motorola Solutions, Inc. All Rights Reserved.
*MN009970A01*
MN009970A01-AB

--- Halaman 2 ---
Intellectual Property and Regulatory
Notices
Copyrights
The Motorola Solutions products described in this document may include copyrighted Motorola Solutions
computer programs. Laws in the United States and other countries preserve for Motorola Solutions
certain exclusive rights for copyrighted computer programs. Accordingly, any copyrighted Motorola Solutions
computer programs contained in the Motorola Solutions products described in this document may not be
copied or reproduced in any manner without the express written permission of Motorola Solutions.
No part of this document may be reproduced, transmitted, stored in a retrieval system, or translated into
any language or computer language, in any form or by any means, without the prior written permission of
Motorola Solutions, Inc.
Trademarks
MOTOROLA, MOTO, MOTOROLA SOLUTIONS, and the Stylized M Logo are trademarks or registered
trademarks of Motorola Trademark Holdings, LLC and are used under license. All other trademarks are the
property of their respective owners.
License Rights
The purchase of Motorola Solutions products shall not be deemed to grant either directly or by implication,
estoppel or otherwise, any license under the copyrights, patents or patent applications of Motorola Solutions,
except for the normal non-exclusive, royalty-free license to use that arises by operation of law in the sale of a
product.
Open Source Content
This product may contain Open Source software used under license. Refer to the product installation media
for full Open Source Legal Notices and Attribution content.
European Union (EU) and United Kingdom (UK) Waste of Electrical and Electronic
Equipment (WEEE) Directive
 The European Union's WEEE directive and the UK's WEEE regulation require that products sold into
EU countries and the UK must have the crossed-out wheelie bin label on the product (or the package in some
cases). As defined by the WEEE directive, this crossed-out wheelie bin label means that customers and
end-users in EU and UK countries should not dispose of electronic and electrical equipment or accessories in
household waste.
Customers or end-users in EU and UK countries should contact their local equipment supplier representative
or service centre for information about the waste collection system in their country.
Disclaimer
Please note that certain features, facilities, and capabilities described in this document may not be applicable
to or licensed for use on a specific system, or may be dependent upon the characteristics of a specific mobile
subscriber unit or configuration of certain parameters. Please refer to your Motorola Solutions contact for
further information.
© 2023 Motorola Solutions, Inc. All Rights Reserved
MN009970A01-AB
Intellectual Property and Regulatory Notices
2

--- Halaman 3 ---
Contact Us
The Centralized Managed Support Operations (CMSO) is the primary contact for technical support included
in your organization's service agreement with Motorola Solutions.
Service agreement customers should be sure to call the CMSO in all situations listed under Customer
Responsibilities in their agreement, such as:
● To confirm troubleshooting results and analysis before taking action
Your organization received support phone numbers and other contact information appropriate for your
geographic region and service agreement. Use that contact information for the most efficient response.
However, if needed, you can also find general support contact information on the Motorola Solutions website,
by following these steps:
1. Enter motorolasolutions.com in your browser.
2. Ensure that your organization's country or region is displayed on the page. Clicking or tapping the name
of the region provides a way to change it.
3. Select "Support" on the motorolasolutions.com page.
Comments
Send questions and comments regarding user documentation to documentation@motorolasolutions.com.
Provide the following information when reporting a documentation error:
● The document title and part number
● The page number or title of the section with the error
● A description of the error
Motorola Solutions offers various courses designed to assist in learning about the system. For information, go
to https://learning.motorolasolutions.com to view the current course offerings and technology paths.
MN009970A01-AB
Contact Us
3

--- Halaman 4 ---
Foreword
This manual includes all the information necessary to maintain peak product performance and maximum
working time, using levels 1 and 2 maintenance procedures. These levels of service go down to software
issues or replacement of an accessory, commonly performed by local service centers, Motorola Solutions
Authorized Dealers, self-maintained customers, and distributors.
This manual applies to the following models. For other models, see MN001438A01.
PMUE4392BAANAA
PMUD3327BAANAA
PMUE4522BAANAA
PMUE4392BAAEAA
PMUD3327BAAEAA
PMUE4522BAAEAA
PMUE4392BAALAA
PMUD3327BAALAA
PMUE4522BAALAA
PMUE4392BAAAAA
PMUD3327BAAAAA
PMUE4522BAAAAA
PMUE4392BAAAEA
PMUD3327BAAAEA
CAUTION: These servicing instructions are for use by qualified personnel only. To reduce the risk of
electric shock, do not perform any servicing other than what is contained in the Operating Instructions
unless you are qualified to do so. Refer all servicing to qualified service personnel.
Disclaimer
The information in this document is carefully examined, and is believed to be entirely reliable.
However, no responsibility is assumed for inaccuracies. Furthermore, Motorola Solutions reserves the right
to make changes to any products herein to improve readability, function, or design. Motorola Solutions does
not assume any liability arising out of the applications or use of any product or circuit described herein; nor
does it cover any license under its patent rights nor the rights of others. Controlled copies of this document
are available through Motorola Solutions On-Line (MOL).
Trademarks
MOTOROLA, MOTO, MOTOROLA SOLUTIONS and the Stylized M logo are trademarks or registered
trademarks of Motorola Trademark Holdings, LLC and are used under license. All other trademarks are
the property of their respective owners.
© 2023 Motorola Solutions, Inc.
All rights reserved.
MN009970A01-AB
Foreword
4

--- Halaman 5 ---
General Safety and Installation
Standards and Guidelines
WARNING:
● For safe installation, operation, service and repair of this equipment, follow the safety precautions
and instructions described below, as well as any additional safety information in Motorola Solutions
product service and installation manuals and the Motorola Solutions R56 Standards and Guidelines
for Communications Sites manual (which can be obtained by ordering CDROM 9880384V83). To
obtain copies of these materials, please contact Motorola Solutions as directed at the end of this
section. After installation, these instructions should be retained and readily available for any person
operating or servicing this repeater or working near it.
● Failure to follow these safety precautions and instructions could result in serious injury or property
damage.
● The installation process requires preparation and knowledge of the site before installation begins.
Review installation procedures and precautions in the Motorola Solutions R56 manual before
performing any site or component installation. Personnel must use safe work practices and good
judgment, and always follow applicable safety procedures, such as requirements of the
Occupational Safety and Health Administration (OSHA), the National Electrical Code (NEC), and
local codes.
The following are additional general safety precautions that must be observed:
● To continue compliance with any applicable regulations and maintain the safety of this equipment, do not
install substitute parts or perform any unauthorized modifications.
● All equipment must be serviced by Motorola Solutions trained personnel.
● If troubleshooting the equipment while the power is on, be aware of live circuits which could contain
hazardous voltage.
● Do not operate the radio transmitters unless all RF connectors are secure and all connectors are properly
terminated.
● All equipment must be properly grounded in accordance with the Motorola Solutions R56 and specified
installation instructions for safe operation.
● Slots and openings in the cabinet are provided for ventilation. Do not block or cover openings that protect
the devices from overheating.
●
 BURN HAZARD: Some equipment components can become extremely hot during operation. Turn
off all power to the equipment and wait until sufficiently cool before touching.
● Maintain emergency first aid kits at the site.
● Never store combustible materials in or near equipment racks. The combination of combustible material,
heat and electrical energy increases the risk of a fire hazard.
Equipment shall be installed in a site that meets the requirements of a
"restricted access location", per (UL60950-1 & EN60950-1), which is defined as follows: "Access can only
be gained by service persons or by users who have been instructed about the reasons for the restrictions
applied to the location and about any precautions that shall be taken; and access is through the use of
a tool or lock and key, or other means of security, and is controlled by the authority responsible for the
location."
●
 BURN HAZARD: The metal housing of the product may become extremely hot. Use caution when
working around the equipment.
MN009970A01-AB
General Safety and Installation
Standards and Guidelines
5

--- Halaman 6 ---
●
 BURN HAZARD: RF energy. Disconnect power in the cabinet to prevent injury before disconnecting
and connecting antennas.
● Shock hazard. The outer shields of all Tx and Rx RF cables outer shields must be grounded per Motorola
Solutions R56 manual.
● Shock hazard. DC input voltage shall be no higher than 60 VDC. This maximum voltage shall include
consideration of the battery charging "float voltage" associated with the intended supply system,
regardless of the marked power rating of the equipment.
● All Tx and Rx RF cables shall be connected to a surge protection device according to Motorola Solutions
R56 manual. Do not connect Tx and Rx RF cables directly to an outside antenna.
●
Attention  Compliance with National and International standards and guidelines for human exposure to
Electromagnetic Energy (EME) at Transmitter Antenna sites generally requires that persons having
access to a site shall be aware of the potential for exposure to EME and can exercise control of exposure
by appropriate means, such as adhering to warning sign instructions. See this installation manual and
Appendix A of Motorola Solutions R56.
This product complies with the requirements set forth by the European R&TTE regulations and applicable
CENELEC standards concerning human exposure to Electromagnetic Energy (EME) at Transmitter Antenna
sites. MOTOTRBO Repeater – EME ASSESSMENT on page 153 in this manual includes an EME exposure
analysis of a typical system configuration for this product.
For a different system configuration than the typical configuration, compliance with applicable EME exposure
standards (current versions of the EN50384 and EN50385 standards for occupational and general public
exposure, respectively) can be evaluated by either employing the method illustrated in the typical system
configuration EME exposure analysis included in MOTOTRBO Repeater – EME ASSESSMENT on page 153
in this manual, or employing another suitable method among those described in the current version of the
EN50383 standard.
Once the occupational and general public compliance boundaries are determined, means to ensure that
workers and people are outside the respective boundaries, for instance using appropriate signage or
restricted access, should be implemented; if this is not possible or practically achievable for the specific
system configuration, the configuration should be modified in order to make it possible. The R56 Standards
and Guidelines for Communications Sites manual (which can be obtained by ordering CDROM 9880384V83)
provides examples of signage that can be used to identify the occupational or general public compliance
boundaries.
Refer to product specific manuals for detailed safety and installation instructions. Manuals can be obtained
with product orders, downloaded from https://businessonline.motorolasolutions.com, or purchased through
the Motorola Solutions Aftermarket & Accessory Department.
WARNING: This is a class A product. In a domestic environment, this product may cause radio
interference in which case the user may be required to take adequate measures.
MN009970A01-AB
General Safety and Installation
Standards and Guidelines
6

--- Halaman 7 ---
MOTOTRBO SLR 5000 Series Repeater
Supplemental Safety and Installation
Requirements
IMPORTANT:
● The MOTOTRBO SLR 5000 Series Repeater must be installed in a suitable, in-building enclosure.
A restricted access location is required when installing this equipment into the end system.
● The repeater contains a Class 1 built-in power supply component. It is equipped with an appliance
inlet for connecting to an AC input, as well as DC input terminals which meet SELV DC circuit
requirements.
● When installing the equipment, all requirements of relevant standards and local electrical codes
must be fulfilled.
● The maximum operating ambient temperature of this equipment is 60 °C. The maximum operating
altitude is 2000 meters above sea level.
● The 13.6 VDC output from the power supply to the PA is at an energy hazard level (exceeds 240
VA). When installing into the end system, care must be taken so as not to touch the output wires.
● When the SLR 5000 Series Repeater is used in a DC reverting system, the DC power supply must
be located in the same building as the MOTOTRBO SLR 5000 Series Repeater, and it must meet
the requirements of a SELV circuit.
MN009970A01-AB
MOTOTRBO SLR 5000 Series Repeater
Supplemental Safety and Installation Requirements
7

--- Halaman 8 ---
Environmental Information
Material Content
This is to declare that Motorola Solutions products comply with the EU Directive 2011/65/EU (Restriction
of Hazardous Substance or RoHS-2) and India RoHS, including applicable exemptions, concerning the
following substances:
● Lead (Pb) < 0.1% by weight (1000 ppm)
● Mercury (Hg) < 0.1% by weight (1000 ppm)
● Cadmium (Cd) < 0.01% by weight (100 ppm)
● Hexavalent Chromium (Cr6+) < 0.1% by weight (1000 ppm)
● Polybrominated Biphenyls (PBB) < 0.1% by weight (1000 ppm)
● Polybrominated Diphenyl Ethers (PBDE) < 0.1% by weight (1000 ppm)
NOTE:
● The Motorola Solutions MOTOTRBO SLR 5000 Series Repeater system and its subsystems have
been created in compliance with the environmental goals of the European Union's Restriction of
Hazardous Substances (RoHS 2) Directive 2011/65/EU and the Waste Electrical and Electronic
Equipment (WEEE) Directive 2012/19/EU as well as Motorola Solutions corporate goals to minimize
environmental impact of its products.
● This Motorola Solutions policy is reflected throughout the entire design, procurement, assembly, and
packaging process.
● In support of these efforts to provide environmentally-responsible products, comply with the
information in the following sections regarding product disposal for systems being replaced.
Disposal of your Electronic and Electric
Equipment
Do not dispose of electronic and electric equipment or electronic and electric accessories with your
household waste.
In some countries or regions, collection systems have been set up to handle waste of electrical and electronic
equipment.
In European Union countries, contact your local equipment supplier representative or service center for
information about the waste collection system in your country.
Disposal Guideline
The European Union's WEEE directive symbol on a Motorola Solutions product indicates that the product
should not be disposed of with household waste.
MN009970A01-AB
Environmental Information
8

--- Halaman 9 ---
Document History
Edition Description Date
MN009970A01-AA Original release of the SLR 5000 Ser-
ies Repeater Basic Service & Installa-
tion Manual.
March 2023
MN009970A01-AB The title of the manual has been up-
dated to SLR 5000 Revision B Series
Repeater Basic Service and Installa-
tion Manual.
Updated sections:
● Specifications on page 36
● Cables on page 132
● Site Environmental Conditions on
page 117
Deleted sections:
● 350 Band High Power Model
Chart
All mentions of 300 Band and 350
Band have been removed.
October 2023
MN009970A01-AB
Document History
9

--- Halaman 10 ---
Contents
Intellectual Property and Regulatory Notices...................................................................2
Contact Us............................................................................................................................3
Document History................................................................................................................9
List of Figures....................................................................................................................17
List of Tables......................................................................................................................20
List of Procedures............................................................................................................. 21
Glossary of Terms and Acronyms................................................................................... 22
Related Publications......................................................................................................... 26
Summary of Bands Available........................................................................................... 27
Limited Commercial Warranty..........................................................................................28
Chapter 1: SLR 5000 Series Repeater.............................................................................. 31
1.1 Notations Used in This Manual........................................................................................................ 31
1.2 Description.......................................................................................................................................31
1.3 Operating Features..........................................................................................................................34
1.4 Frequency Ranges and Power Levels............................................................................................. 36
1.5 Specifications...................................................................................................................................36
1.6 Theory of Operation......................................................................................................................... 38
1.7 Basic Repeater Level Troubleshooting – RDAC and LEDs............................................................. 40
1.8 Repeater Model Numbering Scheme...............................................................................................42
1.9 Model Chart..................................................................................................................................... 43
1.9.1 VHF High Power Model Chart............................................................................................43
1.9.2 VHF Low Power Model Chart.............................................................................................43
1.9.3 UHF R1 High Power Model Chart...................................................................................... 44
1.9.4 UHF R1 Low Power Model Chart.......................................................................................44
1.9.5 UHF R2 High Power Model Chart...................................................................................... 45
1.9.6 UHF R2 Low Power Model Chart.......................................................................................45
Chapter 2: SLR 5000 Series Satellite Receiver................................................................46
2.1 Satellite Receiver Description.......................................................................................................... 46
2.2 Operating Features..........................................................................................................................46
2.3 Frequency Ranges...........................................................................................................................46
2.4 Specifications...................................................................................................................................46
2.5 Configuration....................................................................................................................................47
2.6 Basic Station Level Troubleshooting – RDAC and LEDs.................................................................47
2.7 Model Chart..................................................................................................................................... 47
MN009970A01-AB
Contents
10

--- Halaman 11 ---
Chapter 3: SLR 5000 Series Modem.................................................................................48
3.1 General Description......................................................................................................................... 48
3.2 Input and Output Connections......................................................................................................... 49
3.3 Frequency Bands.............................................................................................................................50
3.4 Receiver Subsystem........................................................................................................................ 50
3.4.1 Specifications..................................................................................................................... 50
3.5 Transmitter Exciter Subsystem........................................................................................................ 51
3.5.1 Specifications..................................................................................................................... 52
3.6 Station Control Subsystem.............................................................................................................. 52
3.6.1 High Stability Reference Block...........................................................................................53
3.6.2 Audio..................................................................................................................................53
3.7 Station Control Interface.................................................................................................................. 54
3.7.1 Front Panel Interface Connector........................................................................................ 54
3.7.2 Rear Panel Connections.................................................................................................... 54
3.7.3 Power Amplifier Interface Connector................................................................................. 54
3.7.4 Power Supply Interface Connector.................................................................................... 54
3.7.5 Chassis ID Interface Connector......................................................................................... 55
Chapter 4: SLR 5000 Series Power Amplifier.................................................................. 56
4.1 General Description......................................................................................................................... 56
4.2 Input and Output Connections......................................................................................................... 56
4.3 Frequency Ranges...........................................................................................................................57
4.4 Specifications...................................................................................................................................58
4.5 Modem Interface.............................................................................................................................. 58
Chapter 5: SLR 5000 Series Power Supply......................................................................59
5.1 General Description......................................................................................................................... 59
5.2 Specifications...................................................................................................................................60
5.3 Power Section Interface Overview...................................................................................................61
Chapter 6: SLR 5000 Series Front Panel..........................................................................63
6.1 Description.......................................................................................................................................63
6.1.1 General Description........................................................................................................... 63
6.2 Input and Output Connections......................................................................................................... 63
6.3 Modem Interface.............................................................................................................................. 64
6.4 USB Interface...................................................................................................................................64
6.5 LED Indicators................................................................................................................................. 64
Chapter 7: SLR 5000 Series Back Panel.......................................................................... 65
7.1 Description.......................................................................................................................................65
7.1.1 General Description........................................................................................................... 65
7.2 Back Panel Interfaces...................................................................................................................... 66
MN009970A01-AB
Contents
11

--- Halaman 12 ---
7.2.1 AC Power Inlet................................................................................................................... 66
7.2.2 DC Power Inlet/DC Charger Outlet.................................................................................... 67
7.2.3 Ethernet 1...........................................................................................................................67
7.2.4 Ethernet 2...........................................................................................................................68
7.2.5 Auxiliary (Aux).................................................................................................................... 68
7.2.6 Frequency Reference.........................................................................................................71
7.2.7 Receiver RF....................................................................................................................... 72
7.2.8 Transmitter RF................................................................................................................... 72
7.2.9 Bonding Ground Connection..............................................................................................73
Chapter 8: SLR 5000 Series Test Equipment And Service Aids.................................... 74
8.1 Recommended Test Equipment.......................................................................................................74
8.2 Service Aids.....................................................................................................................................74
Chapter 9: SLR 5000 Series Performance Check or Testing..........................................76
9.1 Performance Check or Testing General Description........................................................................76
9.2 Transmitter Testing...........................................................................................................................76
9.2.1 Introduction........................................................................................................................ 76
9.2.2 Required Transmitter Test Equipment................................................................................76
9.2.3 Verifying Transmitter Circuitry............................................................................................ 77
9.3 Receiver Testing.............................................................................................................................. 78
9.3.1 Introduction........................................................................................................................ 78
9.3.2 Required Receiver Test Equipment....................................................................................79
9.3.3 Verifying Receiver Circuitry................................................................................................ 79
9.4 Auto Test and Tune Support............................................................................................................ 80
Chapter 10: SLR 5000 Series Programming and Tuning................................................ 81
10.1 Programming and Tuning Introduction...........................................................................................81
10.2 Customer Programming Software Setup....................................................................................... 81
10.3 Tuning the Reference Oscillator Alignment....................................................................................82
10.4 Repeater Tuning Setup..................................................................................................................83
10.5 Tuning the Rx Audio Level Set.......................................................................................................83
10.6 Tuning the Tx Audio Level Set.......................................................................................................84
10.7 Modulation Limit Alignment............................................................................................................85
10.7.1 Tuning the Modulation Limit (with no Tx Data and no PL)............................................... 85
10.7.2 Verifying the Modulation Limit (with no Tx Data and no PL)............................................ 86
10.7.3 Tuning the Modulation Limit (with Tx Data or PL)............................................................ 87
10.7.4 Verifying the Modulation Limit (with Tx Data or PL)......................................................... 88
Chapter 11: SLR 5000 Series Maintenance and Disassembly/Reassembly..................89
11.1 Introduction.....................................................................................................................................89
11.2 Routine Maintenance..................................................................................................................... 89
MN009970A01-AB
Contents
12

--- Halaman 13 ---
11.3 Preventive Maintenance.................................................................................................................90
11.3.1 Inspection......................................................................................................................... 90
11.3.2 Cleaning Procedures........................................................................................................90
11.4 Safe Handling of CMOS and LDMOS Devices.............................................................................. 90
11.5 Disassembling................................................................................................................................91
11.5.1 Disassembling the Protective Cover.................................................................................92
11.5.2 Disassembling Front Housing...........................................................................................92
11.5.3 Disassembling Cables......................................................................................................92
11.5.4 Disassembling Fans......................................................................................................... 94
11.5.5 Disassembling the Front Panel.........................................................................................94
11.5.6 Removing the Power Supply............................................................................................ 95
11.5.7 Removing the Modem...................................................................................................... 95
11.5.8 Removing the Power Amplifier Module............................................................................ 96
11.5.9 Removing the Back Panel................................................................................................ 97
11.6 Assembly........................................................................................................................................99
11.6.1 Installing the Back Panel.................................................................................................. 99
11.6.2 Installing Input Cables.................................................................................................... 101
11.6.3 Installing the Power Amplifier Module............................................................................ 102
11.6.4 Installing Modem............................................................................................................ 103
11.6.5 Installing the Power Supply............................................................................................ 106
11.6.6 Installing Fans................................................................................................................ 108
11.6.7 Installing the Front Panel................................................................................................108
11.6.8 Installing Cables............................................................................................................. 109
11.6.9 Installing Front Housing.................................................................................................. 111
11.6.10 Installing the Protective Cover......................................................................................113
11.7 Exploded Mechanical View...........................................................................................................114
11.8 Parts List.......................................................................................................................................114
11.9 Torque Charts...............................................................................................................................115
Chapter 12: SLR 5000 Series Installation.......................................................................117
12.1 Pre-Installation Considerations.................................................................................................... 117
12.1.1 Installation Overview...................................................................................................... 117
12.1.2 Site Environmental Conditions....................................................................................... 117
12.1.3 Equipment Ventilation.....................................................................................................118
12.1.3.1 Mounting in a Cabinet.......................................................................................118
12.1.3.2 Mounting in a Rack...........................................................................................119
12.1.4 AC and DC Input Power Requirements..........................................................................119
12.1.4.1 AC Input Power Requirements......................................................................... 119
12.1.4.2 DC Input Power Requirements.........................................................................119
12.1.4.3 Ground Connection...........................................................................................119
MN009970A01-AB
Contents
13

--- Halaman 14 ---
12.1.4.4 Battery Connection...........................................................................................120
12.1.4.5 RF Antenna Connections................................................................................. 120
12.1.4.6 System Cable Connections.............................................................................. 120
12.1.5 Equipment Mounting Methods....................................................................................... 120
12.1.5.1 Floor-Mounted Cabinet.....................................................................................120
12.1.5.2 Modular Racks................................................................................................. 121
12.1.5.3 Desk Mount...................................................................................................... 122
12.1.6 Site Grounding and Lightning Protection....................................................................... 123
12.1.6.1 Electrical Ground..............................................................................................123
12.1.6.2 RF Ground........................................................................................................123
12.1.6.3 Lightning Ground..............................................................................................123
12.1.6.4 Equipment Grounding...................................................................................... 123
12.1.7 Recommended Tools and Equipment............................................................................ 124
12.1.8 Equipment Unpacking and Inspection............................................................................124
12.2 Mechanical Installation.................................................................................................................125
12.2.1 Mounting Procedures..................................................................................................... 125
12.2.1.1 Transferring Equipment from Shipping Container to Rack or Cabinet............. 125
12.2.1.2 Installing Racks................................................................................................ 125
12.2.1.3 Cabinet Installation...........................................................................................126
12.2.1.4 Mounting Desk................................................................................................. 126
12.3 Electrical Connections................................................................................................................. 127
12.3.1 AC Input Power Connection...........................................................................................128
12.3.2 DC Input Power Connection/DC Charger Connection................................................... 128
12.3.3 Ground Connection........................................................................................................ 129
12.3.4 Battery Connection.........................................................................................................129
12.3.5 RF Antenna Connections............................................................................................... 129
12.3.6 System Cable Connections............................................................................................129
12.4 Post-Installation Checklist............................................................................................................130
12.4.1 Apply Power................................................................................................................... 130
12.4.2 Verify Proper Operation..................................................................................................130
12.4.3 Front Panel LEDs...........................................................................................................130
12.4.4 Repeater Codeplug Data Backup.................................................................................. 131
12.5 Installing Repeater Hardware Options......................................................................................... 131
12.5.1 General Bonding and Grounding Requirements............................................................ 131
12.5.2 General Cabling Requirements......................................................................................131
Appendix A:  Accessories...............................................................................................132
A.1 Introduction....................................................................................................................................132
A.1.1 Antennas..........................................................................................................................132
A.1.2 Cables..............................................................................................................................132
MN009970A01-AB
Contents
14

--- Halaman 15 ---
A.1.3 Documentation.................................................................................................................133
A.1.4 Duplexers.........................................................................................................................133
A.1.5 Mounting.......................................................................................................................... 133
A.1.6 Preselectors.....................................................................................................................134
A.1.7 Service Tools................................................................................................................... 134
Appendix B:  SLR 5000 Series Third-Party Controllers................................................135
B.1 Overview........................................................................................................................................135
B.2 Community Repeater Panel.......................................................................................................... 136
B.2.1 Compatibility.................................................................................................................... 136
B.2.2 Hardware Connections.................................................................................................... 136
B.2.3 CPS Configuration........................................................................................................... 137
B.2.4 Community Repeater Panel Settings...............................................................................139
B.2.4.1 Discriminator...................................................................................................... 139
B.2.4.2 Tx Audio.............................................................................................................140
B.2.4.3 Continuous Tone-Controlled Squelch Systems (CTCSS) Out........................... 140
B.2.4.4 Tx Audio Pre-Emphasis..................................................................................... 140
B.2.4.5 Carrier Operated Relay (COR).......................................................................... 140
B.3 Phone Patch..................................................................................................................................140
B.3.1 Compatibility.................................................................................................................... 141
B.3.2 Hardware Connections.................................................................................................... 141
B.3.3 CPS Configuration........................................................................................................... 141
B.3.4 Phone Patch Level Settings.............................................................................................143
B.4 Tone Remote Adapter....................................................................................................................143
B.4.1 Tone Remote Adapter Compatibility................................................................................ 144
B.4.2 Hardware Connections.................................................................................................... 144
B.4.3 CPS Configuration (For a 15-Channel Remote Control)................................................. 145
B.4.4 Tone Remote Adapter Settings........................................................................................147
B.4.4.1 Radio Rx............................................................................................................ 147
B.4.4.2 Radio Tx.............................................................................................................147
B.4.4.3 Channel Steering............................................................................................... 147
B.4.4.4 Monitoring.......................................................................................................... 147
B.4.4.5 PTT.................................................................................................................... 147
B.4.4.6 Wildcard 1 (optional).......................................................................................... 147
B.5 Trunking Controllers...................................................................................................................... 147
B.5.1 Compatibility.................................................................................................................... 149
B.5.2 Hardware Connections.................................................................................................... 149
B.5.3 CPS Configuration........................................................................................................... 151
B.5.4 Trunking Controller Settings............................................................................................ 152
B.5.4.1 Discriminator...................................................................................................... 152
MN009970A01-AB
Contents
15

--- Halaman 16 ---
B.5.4.2 Tx Audio.............................................................................................................152
B.5.4.3 Tx Data.............................................................................................................. 152
Appendix C:  MOTOTRBO Repeater – EME ASSESSMENT......................................... 153
C.1 Executive Summary...................................................................................................................... 153
C.2 Outdoor Exposure Prediction Model............................................................................................. 154
C.2.1 Exposure in Front of the Antenna....................................................................................154
C.2.2 Exposure at Ground Level...............................................................................................155
C.3 Typical System Configuration........................................................................................................156
C.4 Exposure Limits.............................................................................................................................156
C.5 EME Exposure Evaluation.............................................................................................................157
C.5.1 Exposure in Front of the Antenna....................................................................................157
C.5.2 Exposure at Ground Level...............................................................................................157
C.6 Compliance Boundary Description................................................................................................ 157
C.7 Product Put In Service...................................................................................................................158
C.8 References....................................................................................................................................158
MN009970A01-AB
Contents
16

--- Halaman 17 ---
List of Figures
Figure 1: Front view of the SLR 5000 Series Repeater.................................................................................... 32
Figure 2: Rear view of the SLR 5000 Series Repeater.....................................................................................32
Figure 3: Front view (without top cover) of the SLR 5000 Series Repeater..................................................... 33
Figure 4: Front view (without top and bottom covers and front panel) of the SLR 5000 Series Repeater........34
Figure 5: RDAC Diagnostic Screen.................................................................................................................. 40
Figure 6: Repeater Model Numbering Scheme................................................................................................ 42
Figure 7: Operation Mode Configuration for the Satellite Receiver Functionality............................................. 47
Figure 8: Modem Module Connector Locations................................................................................................49
Figure 9: High Stability Reference Circuit.........................................................................................................53
Figure 10: Audio Block Diagram.......................................................................................................................53
Figure 11: Power Amplifier Interface Connector Pin Locations........................................................................ 54
Figure 12: Power Supply Interface Connector Pin Locations........................................................................... 54
Figure 13: Chassis ID Interface Connector Pin Locations................................................................................ 55
Figure 14: Input and Output Connections.........................................................................................................57
Figure 15: Modem Interface Connector Pin Locations..................................................................................... 58
Figure 16: Top View of SLR 5000 Series Power Supply Section......................................................................60
Figure 17: Power Section Interfaces.................................................................................................................61
Figure 18: Front Panel Input and Output Connections..................................................................................... 63
Figure 19: Back Panel Connector Names and Locations................................................................................. 65
Figure 20: AC Power Inlet Connector .............................................................................................................. 66
Figure 21: Repeater Power Switch...................................................................................................................66
Figure 22: DC Power Inlet/DC Charger Outlet Connector................................................................................ 67
Figure 23: Ethernet 1 Connector...................................................................................................................... 67
Figure 24: Ethernet 2 Connector...................................................................................................................... 68
Figure 25: Auxiliary Connector......................................................................................................................... 69
Figure 26: Frequency Reference Connector.................................................................................................... 71
Figure 27: Receiver RF Connector................................................................................................................... 72
Figure 28: Transmitter RF Connector............................................................................................................... 72
Figure 29: Bonding Ground Connection........................................................................................................... 73
Figure 30: Test Equipment Setup for Verifying Transmitter Circuitry................................................................ 78
Figure 31: Test Equipment Setup for Verifying Receiver Circuitry.................................................................... 80
Figure 32: Customer Programming Software Setup.........................................................................................81
Figure 33: Front View of the SLR 5000 Series Repeater................................................................................. 82
Figure 34: Rear View of the SLR 5000 Series Repeater.................................................................................. 82
Figure 35: Tx Menu Tree (Ref. Oscillator)........................................................................................................ 83
Figure 36: SLR 5000 Series Repeater Tuning Equipment Setup..................................................................... 83
MN009970A01-AB
List of Figures
17

--- Halaman 18 ---
Figure 37: Rx Menu tree (Rx Rated Volume)....................................................................................................84
Figure 38: Auxiliary Connector......................................................................................................................... 84
Figure 39: Tx Menu Tree (Tx Audio Level)....................................................................................................... 85
Figure 40: TX Menu Tree (Tuning Procedure with No Tx Data)....................................................................... 86
Figure 41: Example of Maximum Deviation Limit Calculation...........................................................................88
Figure 42: Removal of the Front Housing from Repeater.................................................................................92
Figure 43: Removal of Cables.......................................................................................................................... 93
Figure 44: Removal of the Fan......................................................................................................................... 94
Figure 45: Removal of the Front Panel.............................................................................................................94
Figure 46: Removal of the Power Supply and Peripheral Board...................................................................... 95
Figure 47: Removal of the Modem................................................................................................................... 96
Figure 48: Removal of the Power Amplifier Module......................................................................................... 97
Figure 49: Removal of the Rx and REF BNC Cables....................................................................................... 98
Figure 50: Removing Ground Screw................................................................................................................ 99
Figure 51: Installation of the M3 Screws.........................................................................................................100
Figure 52: Installation of the M6 Screw.......................................................................................................... 100
Figure 53: Installation of the Rx and Reference Cables................................................................................. 101
Figure 54: Assembly of the Lock Washers onto Connectors..........................................................................101
Figure 55: Installation of Power Cables..........................................................................................................102
Figure 56: Installation of the Power Amplifier Module into the Repeater........................................................102
Figure 57: Securing the Power Amplifier Module to the Repeater Chassis....................................................103
Figure 58: Securing Modem to the Repeater Frame...................................................................................... 104
Figure 59: Securing Rx and Reference Cable Connectors.............................................................................105
Figure 60: Modem FRU Product Label........................................................................................................... 106
Figure 61: Installation of the Power Supply and Peripheral Board................................................................. 106
Figure 62: Installation of the Power Supply and Peripheral Screws............................................................... 107
Figure 63: Installation of the Fan Cable..........................................................................................................107
Figure 64: Installation of the Fan.................................................................................................................... 108
Figure 65: Installation of the Front Panel........................................................................................................109
Figure 66: Installing DC Wires........................................................................................................................ 110
Figure 67: Installing Cables.............................................................................................................................111
Figure 68: Securing Front Housing................................................................................................................. 112
Figure 69: Installation of the M3 Screws.........................................................................................................113
Figure 70: SLR 5000 Series Assembly Exploded View.................................................................................. 114
Figure 71: Floor Mount Cabinet......................................................................................................................121
Figure 72: Modular Rack................................................................................................................................ 122
Figure 73: Desk Mount Installation................................................................................................................. 126
Figure 74: Back Panel Connector Names and Locations............................................................................... 127
Figure 75: Location of USB Connector...........................................................................................................128
MN009970A01-AB
List of Figures
18

--- Halaman 19 ---
Figure 76: CPS Settings to Configure SLR 5000 Series Repeater for Analog Mode..................................... 135
Figure 77: Model Zetron 38 Repeater Panel.................................................................................................. 136
Figure 78: Signal Connections between SLR 5000 Series Repeater and Community Repeater Panel.........137
Figure 79: CPS Configuration for Community Repeater Panel (1 of 2).......................................................... 138
Figure 80: CPS Configuration for Community Repeater Panel (2 of 2).......................................................... 139
Figure 81: Zetron Model 30 Phone Patch.......................................................................................................140
Figure 82: Signal Connections between SLR 5000 Series Repeater and Zetron Model 30 Phone Patch
(Analog Phone Patch Cable & Digital Phone Patch Cable).......................................................................141
Figure 83: CPS Configuration for Phone Patch (1 of 2)..................................................................................142
Figure 84: CPS Configuration for Phone Patch (2 of 2)..................................................................................143
Figure 85: Model L3276 Tone Remote Adapter..............................................................................................144
Figure 86: Signal Connections between SLR 5000 Series Repeater and Motorola Solutions L3276 25-
Pin connector for a 15-Channel Remote Control.......................................................................................145
Figure 87: CPS Configuration for L3276 Tone Remote Adapter
(For a 15-Channel Remote Control).......................................................................................................... 146
Figure 88: Model Trident’s Marauder..............................................................................................................148
Figure 89: Model Trident’s Raider...................................................................................................................148
Figure 90: Model Trident’s NTS......................................................................................................................148
Figure 91: Signal Connections Between the SLR 5000 Series Repeater, Trident Model Raider,
Marauder, and NTS................................................................................................................................... 150
Figure 92: CPS Configuration for Trident Model Raider, Marauder and NTS.................................................151
Figure 93: Reference Frame for the Point of Interest (POI) Cylindrical Coordinates......................................154
Figure 94: Schematic of the Ground-Level Exposure Model Adopted for the Assessment............................156
Figure 95: Compliance Boundary for General Public (GP) and Ocupational (OCC) Exposure...................... 158
MN009970A01-AB
List of Figures
19

--- Halaman 20 ---
List of Tables
Table 1: SLR 5000 Series Frequency Ranges and Power Levels.................................................................... 36
Table 2: SLR 5000 Series Repeater General Specifications (All Bands)..........................................................36
Table 3: SLR 5000 Series Repeater Specifications..........................................................................................36
Table 4: SLR 5000 Series Repeater Front Panel LED Indicators..................................................................... 40
Table 5: SLR 5000 Series Front Panel LED Definitions....................................................................................41
Table 6: VHF High Power Model Chart.............................................................................................................43
Table 7: VHF Low Power Model Chart..............................................................................................................43
Table 8: UHF R1 High Power Model Chart....................................................................................................... 44
Table 9: UHF R1 Low Power Model Chart........................................................................................................44
Table 10: UHF R2 High Power Model Chart..................................................................................................... 45
Table 11: Specifications of Receiver Subsystem.............................................................................................. 50
Table 12: Specifications of Transmitter Exciter Subsystem.............................................................................. 52
Table 13: Specifications of Power Amplifier......................................................................................................58
Table 14: Power Supply AC Performance Specifications................................................................................. 60
Table 15: Power Supply DC Performance Specifications................................................................................. 61
Table 16: Recommended Test Equipment........................................................................................................74
Table 17: Service Aids...................................................................................................................................... 74
Table 18: Modulation Limit (with no Tx Data and no PL).................................................................................. 86
Table 19: Modulation Limits.............................................................................................................................. 87
Table 20: SLR 5000 Series Exploded View Parts List.....................................................................................114
Table 21: FRU Part Number by Band..............................................................................................................115
Table 22: Torque Specifications for Nuts and Screws.....................................................................................116
Table 23: Cabinet Models............................................................................................................................... 121
Table 24: Cabinet Slide...................................................................................................................................121
Table 25: Rack Models................................................................................................................................... 122
Table 26: Antennas.........................................................................................................................................132
Table 27: Cables.............................................................................................................................................132
Table 28: Documentation................................................................................................................................133
Table 29: Duplexers........................................................................................................................................133
Table 30: Mounting......................................................................................................................................... 133
Table 31: Preselectors.................................................................................................................................... 134
Table 32: Service Tools...................................................................................................................................134
Table 33: EME Compliance Distances Based on Example UHF Evaluation.................................................. 153
MN009970A01-AB
List of Tables
20

--- Halaman 21 ---
List of Procedures
Verifying Transmitter Circuitry ..........................................................................................................................77
Verifying Receiver Circuitry ..............................................................................................................................79
Tuning the Reference Oscillator Alignment ..................................................................................................... 82
Tuning the Rx Audio Level Set ........................................................................................................................ 83
Tuning the Tx Audio Level Set .........................................................................................................................84
Tuning the Modulation Limit (with no Tx Data and no PL) ...............................................................................85
Verifying the Modulation Limit (with no Tx Data and no PL) ............................................................................ 86
Tuning the Modulation Limit (with Tx Data or PL) ............................................................................................87
Disassembling ................................................................................................................................................. 91
Disassembling the Protective Cover ................................................................................................................92
Disassembling Front Housing ..........................................................................................................................92
Disassembling Cables ..................................................................................................................................... 92
Disassembling Fans ........................................................................................................................................ 94
Disassembling the Front Panel ........................................................................................................................94
Removing the Power Supply ........................................................................................................................... 95
Removing the Modem ......................................................................................................................................95
Removing the Power Amplifier Module ............................................................................................................96
Removing the Back Panel ............................................................................................................................... 97
Installing the Back Panel ................................................................................................................................. 99
Installing Input Cables ................................................................................................................................... 101
Installing the Power Amplifier Module ............................................................................................................102
Installing Modem ............................................................................................................................................103
Installing the Power Supply ........................................................................................................................... 106
Installing Fans ................................................................................................................................................108
Installing the Front Panel ...............................................................................................................................108
Installing Cables ............................................................................................................................................ 109
Installing Front Housing ..................................................................................................................................111
Installing the Protective Cover ....................................................................................................................... 113
Installing Racks ..............................................................................................................................................125
Mounting Desk ...............................................................................................................................................126
MN009970A01-AB
List of Procedures
21

--- Halaman 22 ---
Glossary of Terms and Acronyms
This glossary contains an alphabetical listing of terms and their definitions that are applicable to repeater
products. All terms do not necessarily apply to all radios, and some terms are merely generic in nature.
Alert tone
Audio signal produced by the station, providing feedback to the user.
Analog
Refers to a continuously variable signal or a circuit or device designed to handle such signals.
ASIC
Application Specific Integrated Circuit
AUX
Auxiliary
Band
Frequencies allowed for a specific purpose.
CTCSS
Continuous Tone-Controlled Squelch Systems (PL)
Clear
Channel modulation type in which voice information is transmitted over the channel using analog
modulation.
Conventional
Term used for standard non-trunked radio system (usually using TRC/DC console).
CPS
Customer Programming Software: Software with a graphical user interface containing the feature set of a
radio.
Default
A pre-defined set of parameters.
Digital
Refers to data that is stored or transmitted as a sequence of discrete symbols from a finite set; most
commonly this means binary data represented using electronic or electromagnetic signals.
DPL
Digital Private-Line: A type of digital communications that utilizes privacy call, as well as memory channel
and busy channel lock out to enhance communication efficiency.
DSP
Digital Signal Processor, microprocessor specifically designed to perform digital signal processing
algorithms.
EIA
Electronic Industries Association
ESD
Electro Static Discharge
EU
European Union
FCC
Federal Communications Commission
FM
Frequency Modulation
MN009970A01-AB
Glossary of Terms and Acronyms
22

--- Halaman 23 ---
Frequency
Number of times a complete electromagnetic-wave cycle occurs in a fixed unit of time (usually one
second).
FRU
Field Replaceable Unit
FSK
Frequency Shift Keying
GNSS
Global Navigation Satellite System
GPIO
General Purpose Input/Output
IC
Integrated Circuit: An assembly of interconnected components on a small semiconductor chip, usually
made of silicon. One chip can contain millions of microscopic components and perform many functions.
IF
Intermediate frequency
I/O
Input or Output
kHz
kilohertz: One thousand cycles per second. Used especially as a radio-frequency unit
LCD
Liquid-Crystal Display: An LCD uses two sheets of polarizing material with a liquid-crystal solution
between them. An electric current passed through the liquid causes the crystals to align so that light
cannot pass through them.
LED
Light Emitting Diode: An electronic device that lights up when electricity is passed through it.
MDC
Motorola Data Communications. 1200 or 4800 baud data signalling scheme.
MHz
Megahertz: One million cycles per second. Used especially as a radio-frequency unit.
PA
Power Amplifier that transmits final RF signal to transmit antenna.
PC Board
Printed Circuit Board. Also referred to as a PCB.
PFC
Power Factor Correction
PL
Private-Line Tone Squelch: A continuous sub-audible tone that is transmitted along with the carrier.
Programming Cable
A cable that allows the CPS to communicate directly with the radio using RS232.
PTT
Push-to-talk; the switch located on the left side of the radio which, when pressed causes the radio to
transmit.
Receiver
Electronic device that amplifies RF signals. A Receiver separates the audio signal from the RF carrier,
amplifies it, and converts it back to the original sound waves.
MN009970A01-AB
Glossary of Terms and Acronyms
23

--- Halaman 24 ---
Repeater
Remote transmit/receive facility that retransmits received signals in order to improve communications
range and coverage.
RF
Radio Frequency: The portion of the electromagnetic spectrum between audio sound and infrared light
(approximately 10 kHz to 10 GHz).
RSSI
Received Signal Strength Indicator; a dc voltage proportional to the received RF signal strength.
Rx
Receive
SCM
Station Control Module; station controller.
SELV
Separated Extra Low Voltage
Signal
An electrically transmitted electromagnetic wave.
SINAD
Acronym for the ratio of signal plus noise plus distortion and noise plus distortion.
SLR
Refers to Digital Professional Repeater model names in the MOTOTRBO Professional Digital Two-Way
Radio System.
Spectrum
Frequency range within which radiation has specific characteristics.
SPI
Serial Peripheral Interface (clock and data lines); simple synchronous serial interface for data transfer
between processors and peripheral ICs.
Squelch
Muting of audio circuits when received signal levels fall below a pre-determined value. With carrier
squelch, all channel activity that exceeds the radio’s preset squelch level can be heard.
TOT
Time-out Timer: A timer that limits the length of a transmission.
TPL
Tone Private Line
Transceiver
Transmitter-Receiver. A device that both transmits and receives analog or digital signals. Also abbreviated
as XCVR.
Transmitter
Electronic equipment that generates and amplifies an RF carrier signal, modulates the signal, and then
radiates it into space.
Trunking
Radio control system which permits efficient frequency utilization and enhanced control features.
Tx
Transmit
UHF
Ultra High Frequency
USB
Universal Serial Bus: An external bus standard that supports data transfer rates of 12 Mbps.
MN009970A01-AB
Glossary of Terms and Acronyms
24

--- Halaman 25 ---
VCO
Voltage-Controlled Oscillator; an oscillator whereby the frequency of oscillation can be varied by changing
a control voltage.
VCTCXO
Voltage Controlled Temperature Compensated Crystal Oscillator
VHF
Very High Frequency
VIP
Vehicle Interface Port
VSWR
Voltage Standing Wave Ratio
WLAN
Wireless Local Area Network
MN009970A01-AB
Glossary of Terms and Acronyms
25

--- Halaman 26 ---
Related Publications
Related Publications Part No.
MOTOTRBO SLR 5000 Series Quick Start Guide MN001441A01
MN009970A01-AB
Related Publications
26

--- Halaman 27 ---
Summary of Bands Available
Table below lists the SLR 5000 Series Repeater bands available in this manual. For details, see Model
Charts section.
Frequency Band Bandwidth Power Level
VHF 136–174 MHz 1–25 W
1–50 W
UHF R1 400–470 MHz 1–25 W
1–50 W
UHF R2 450–527 MHz 1–50 W
1–25 W
MN009970A01-AB
Summary of Bands Available
27

--- Halaman 28 ---
Limited Commercial Warranty
MOTOROLA COMMUNICATION PRODUCTS
I. What This Warranty Covers And For How Long
MOTOROLA SOLUTIONS SINGAPORE PTE. LTD. ("MOTOROLA") warrants the MOTOROLA manufactured
TWO-WAY RADIO Products listed below ("Product") against defects in material and performance under
normal use and service for a period of time from the date of purchase as scheduled below:
Repeater Two (2) Years
Product Accessories One (1) Year
Motorola, at its option, will at no charge either repair the Product (with new or reconditioned parts), replace
it (with a new or reconditioned Product), or refund the purchase price of the Product during the WARRANTY
PERIOD provided it is returned in accordance with the terms of this warranty. Replaced parts or boards are
warranted for the balance of the original applicable WARRANTY PERIOD. All replaced parts of Product shall
become the property of MOTOROLA.
This express limited warranty is extended by MOTOROLA to the original end user purchaser only and is not
assignable or transferable to any other party. This is the complete warranty for the Product manufactured by
MOTOROLA. MOTOROLA assumes no obligations or liability for additions or modifications to this warranty
unless made in writing and signed by an officer of MOTOROLA. Unless made in a separate agreement
between MOTOROLA and the original end user purchaser, MOTOROLA does not warrant the installation,
maintenance or service of the Product.
MOTOROLA cannot be responsible in any way for any ancillary equipment not furnished by MOTOROLA
which is attached to or used in connection with the Product, or for operation of the Product with any ancillary
equipment, and all such equipment is expressly excluded from this warranty. Because each system which
may use the Product is unique, MOTOROLA disclaims liability for range, coverage, or operation of the system
as a whole under this warranty.
II. General Provisions
This warranty sets forth the full extent of MOTOROLA's responsibilities regarding the Product. Repair,
replacement or refund of the purchase price, at MOTOROLA's option, is the end user purchasers’ exclusive
remedy. THIS WARRANTY IS GIVEN IN LIEU OF ALL OTHER EXPRESS WARRANTIES. IMPLIED
WARRANTIES, INCLUDING WITHOUT LIMITATION, IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE, ARE LIMITED TO THE DURATION OF THIS
LIMITED WARRANTY. IN NO EVENT SHALL MOTOROLA BE LIABLE FOR DAMAGES IN EXCESS
OF THE PURCHASE PRICE OF THE PRODUCT, FOR ANY LOSS OF USE, LOSS OF TIME,
INCONVENIENCE, COMMERCIAL LOSS, LOST PROFITS OR SAVINGS OR OTHER INCIDENTAL,
SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE SUCH
PRODUCT, TO THE FULL EXTENT SUCH MAY BE DISCLAIMED BY LAW.
III. What This Warranty Does Not Cover
Defects or damage resulting from use of the MOTOROLA Product in other than its normal and customary
manner.
Defects or damage occurring from misuse, abuse, accident, corrosion, fire, liquid intrusion, or neglect.
Defects or damage from improper or unauthorized testing, operation, maintenance, service, repair,
installation, alteration, modification, or adjustment.
Breakage or damage to antennas unless caused directly by defects in material or performance.
MN009970A01-AB
Limited Commercial Warranty
28

--- Halaman 29 ---
MOTOROLA Product that has not been operated in accordance with the procedures described in the
operating instructions.
MOTOROLA Product that has been subjected to unauthorized modifications, tampering, disassembly, use
of non- genuine accessories or batteries or repairs (including the addition to the MOTOROLA Product of
non-MOTOROLA supplied equipment if not authorized by MOTOROLA) which adversely affect performance
of the MOTOROLA Product or interfere with MOTOROLA's normal warranty inspection and testing of the
MOTOROLA Product to verify any warranty claim.
MOTOROLA Product which has had the serial number removed or made illegible.
MOTOROLA Product that has its seal(s) on non-user serviceable components or modules broken.
Freight costs to the repair depot.
MOTOROLA Product that has been subjected to illegal or unauthorized alteration of the software/firmware in
the MOTOROLA Product.
Scratches or other cosmetic damage to MOTOROLA Product surfaces that does not affect the operation of
the MOTOROLA Product.
Normal and customary wear and tear.
Memory modules not programmed by MOTOROLA’s Aftermarket Products Group.
Warranty claims not made within the Warranty Period.
IV. Patent And Software Provisions
MOTOROLA will have no liability with respect to any claim of patent infringement which is based upon the
combination of the Product or parts furnished hereunder with software, apparatus or devices not furnished
by MOTOROLA, nor will MOTOROLA have any liability for the use of ancillary equipment or software not
furnished by MOTOROLA which is attached to or used in connection with the Product. The foregoing states
the entire liability of MOTOROLA with respect to infringement of patents by the Product or any parts thereof.
Laws in the United States and other countries preserve for MOTOROLA certain exclusive rights for
copyrighted MOTOROLA software such as the exclusive rights to reproduce in copies and distribute copies
of such MOTOROLA software. MOTOROLA software may be used in only the Product in which the software
was originally embodied and such software in such Product may not be replaced, copied, distributed,
modified in any way, or used to produce any derivative thereof. No other use including, without limitation,
alteration, modification, reproduction, distribution, or reverse engineering of such MOTOROLA software or
exercise of rights in such MOTOROLA software is permitted. No license is granted by implication, estoppel or
otherwise under MOTOROLA patent rights or copyrights.
V. How To Get Warranty Service
You must provide proof of purchase (bearing the date of purchase and Product item serial number) in order
to receive warranty service and, also, deliver or send the Product item, transportation and insurance prepaid,
to an authorized warranty service location. Warranty service will be provided by MOTOROLA through one of
its authorized warranty service locations. If you first contact the company which sold you the Product (e.g.,
dealer or communication service provider), it can facilitate your obtaining warranty service, repair service and
technical support.
VI. For Australia Only
This warranty is given by Motorola Solutions Australia Pty Limited (ABN 16 004 742 312) of
Tally Ho Business Park, 10 Wesley Court, Burwood East, Victoria. Our goods come with guarantees that
cannot be excluded under the Australia Consumer Law. You are entitled to a replacement or refund for a
major failure and compensation for any other reasonably foreseeable loss or damage. You are also entitled
to have the goods repaired or replaced if the goods fail to be of acceptable quality and the failure does not
amount to a major failure.
Motorola Solutions Australia’s limited warranty above is in addition to any rights and remedies you may have
under the Australian Consumer Law. If you have any queries, please call
MN009970A01-AB
Limited Commercial Warranty
29

--- Halaman 30 ---
Motorola Solutions Australia at 1800154730 (AU Toll Free) or 508362421 (NZ Toll Free).
You may also visit our website: https://asiaonline.motorolasolutions.com for the most updated warranty terms.
MN009970A01-AB
Limited Commercial Warranty
30
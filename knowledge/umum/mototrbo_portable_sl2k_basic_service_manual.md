--- Halaman 1 ---
MOTOTRBO™ PORTABLE
SL2K BASIC SERVICE
MANUAL
MOTOTRBO™ PORTABLE
PROFESSIONAL DIGITAL TWO-WAY RADIO
*MN002194A01*
MN002194A01-AC
SEPTEMBER 2018
© 2018 Motorola Solutions, Inc. All rights reserved

--- Halaman 2 ---
Contents
List of Figures..............................................................................................................5
List of Tables............................................................................................................... 7
Foreword......................................................................................................................8
Product Safety and RF Exposure Compliance.............................................................................. 8
Computer Software Copyrights......................................................................................................8
Document Copyrights.................................................................................................................... 8
Disclaimer...................................................................................................................................... 8
Trademarks....................................................................................................................................9
Document History..................................................................................................... 10
Related Publication...................................................................................................11
Notations Used in This Manual................................................................................12
Warranty and Service Support.................................................................................13
Chapter 1: Introduction.............................................................................................14
1.1 Radio Description.................................................................................................................. 14
1.1.1 Radio Overview........................................................................................................15
1.2 Portable Radio Model Numbering Scheme........................................................................... 16
1.3 Model Charts......................................................................................................................... 17
1.3.1 UHF Model Chart..................................................................................................... 17
1.3.2 UHF2 Model Chart................................................................................................... 19
1.3.3 800 MHz Model Chart.............................................................................................. 19
1.4 Specifications.........................................................................................................................20
Chapter 2: Test Equipment and Service Aids........................................................ 24
2.1 Recommended Test Equipment............................................................................................ 24
2.2 Service Aids...........................................................................................................................25
Chapter 3: Transceiver Performance Testing........................................................ 26
3.1 Setup..................................................................................................................................... 26
3.2 Test Mode..............................................................................................................................29
3.2.1 Entering Display Radio Test Mode.......................................................................... 29
3.2.2 RF Test Mode.......................................................................................................... 30
3.2.2.1 Testing RF Channel Selections..................................................................30
3.2.3 Flicker Test Mode.................................................................................................... 32
3.2.4 Display Test Mode................................................................................................... 32
3.2.5 Photosensor Test Mode...........................................................................................33
3.2.6 Accelerometer Test Mode........................................................................................34
3.2.7 Vibrator Test Mode.................................................................................................. 34
MN002194A01-AC
Contents
2  

--- Halaman 3 ---
3.2.8 LED Test Mode........................................................................................................ 35
3.2.9 Backlight Test Mode................................................................................................ 35
3.2.10 Speaker Tone Test Mode...................................................................................... 35
3.2.11 Earpiece Tone Test Mode......................................................................................35
3.2.12 Audio Loopback Earpiece Test Mode.................................................................... 36
3.2.13 Battery Check Test Mode...................................................................................... 36
3.2.14 Button/Knob/PTT Test Mode................................................................................. 36
Chapter 4: Radio Programming and Tuning...........................................................40
4.1 Customer Programming Software Setup............................................................................... 40
4.2 AirTracer Application Tool..................................................................................................... 40
4.3 Radio Tuning Setup...............................................................................................................41
Chapter 5: Disassembly/Reassembly Procedures.................................................42
5.1 Preventive Maintenance........................................................................................................ 42
5.2 Safe Handling of CMOS and LDMOS Devices......................................................................43
5.3 General Repair Procedures and Techniques........................................................................ 43
5.4 Disassembling and Reassembling the Radio........................................................................ 45
5.5 Detailed Radio Disassembly..................................................................................................45
5.5.1 Holster Removal...................................................................................................... 45
5.5.2 External Antenna Disassembly................................................................................ 46
5.5.3 Back Housing Disassembly..................................................................................... 49
5.5.4 Internal Antenna Disassembly................................................................................. 51
5.5.5 PCB Disassembly.................................................................................................... 51
5.5.6 Audio Jack Flex and Keypad Flex Disassembly...................................................... 52
5.5.7 LCD Display Disassembly........................................................................................53
5.6 Detailed Radio Reassembly.................................................................................................. 55
5.6.1 LCD Display Reassembly........................................................................................ 55
5.6.2 Audio Jack Flex Reassembly...................................................................................57
5.6.3 Interface Board Reassembly....................................................................................58
5.6.4 Internal Antenna Reassembly..................................................................................59
5.6.5 Back Housing Reassembly...................................................................................... 59
5.6.6 Holster Reattachment.............................................................................................. 62
5.7 Radio Exploded Mechanical View and Parts List.................................................................. 64
5.7.1 Non-GOB Model Exploded View and Parts List.......................................................64
5.7.2 GOB Model Exploded View and Parts List.............................................................. 66
5.8 Torque Chart..........................................................................................................................68
Chapter 6: Basic Troubleshooting...........................................................................69
6.1 Power-Up Error Codes.......................................................................................................... 69
6.2 Operational Error Codes........................................................................................................71
Chapter 7: Authorized Accessories List................................................................. 72
MN002194A01-AC
Contents
  3

--- Halaman 4 ---
Appendix A: Replacement Parts and Kits.............................................................. 74
Appendix B: Replacement Parts Ordering............................................................. 75
B.1 Additional Service Kits Information........................................................................................75
B.1.1 UHF1 Super Tanapa............................................................................................... 75
B.1.2 UHF2 Super Tanapa............................................................................................... 76
B.1.3 800 MHz Super Tanapa.......................................................................................... 76
Glossary.....................................................................................................................77
MN002194A01-AC
Contents
4  

--- Halaman 5 ---
List of Figures
Figure 1: Display Model..........................................................................................................................15
Figure 2: DMR Radio Transmitter and Receiver Testing Setup............................................................. 26
Figure 3: Name plate label..................................................................................................................... 27
Figure 4: RF plug....................................................................................................................................28
Figure 5: Connect RF Antenna adaptor to radio RF input/output port....................................................29
Figure 6: Battery Check Test Mode Display........................................................................................... 36
Figure 7: CPS Programming Setup........................................................................................................ 40
Figure 8: Radio Tuning Equipment Setup.............................................................................................. 41
Figure 9: Holster removal....................................................................................................................... 46
Figure 10: Radio Switched Off................................................................................................................46
Figure 11: Antenna plug removal with fingers........................................................................................ 47
Figure 12: Escutcheon cover removal with tweezer............................................................................... 47
Figure 13: Antenna screw removal.........................................................................................................48
Figure 14: Antenna removal................................................................................................................... 49
Figure 15: Unlatching battery door......................................................................................................... 49
Figure 16: Battery door removal............................................................................................................. 50
Figure 17: Battery removal..................................................................................................................... 50
Figure 18: Corner screws and middle screws removal...........................................................................50
Figure 19: Back housing removal...........................................................................................................51
Figure 20: Internal antenna removal.......................................................................................................51
Figure 21: Coax cable connector disassembly.......................................................................................51
Figure 22: Flex cable connector disassembly........................................................................................ 52
Figure 23: Interface board removal........................................................................................................ 52
Figure 24: Keypad flex disassembly.......................................................................................................52
Figure 25: Audio jack flex disassembly.................................................................................................. 52
Figure 26: Audio jack flex removal......................................................................................................... 53
Figure 27: LCD display disassembly...................................................................................................... 53
Figure 28: Lifting of PCB........................................................................................................................ 53
Figure 29: PCB removal......................................................................................................................... 54
Figure 30: Speaker seal removal............................................................................................................54
Figure 31: Display retainer lock removal................................................................................................ 54
Figure 32: Display retainer disassembly.................................................................................................55
Figure 33: LCD display removal............................................................................................................. 55
Figure 34: LCD Display Reassembly......................................................................................................56
Figure 35: Flex Connector Tab Reassembly.......................................................................................... 56
Figure 36: PCB Reassembly.................................................................................................................. 56
MN002194A01-AC
List of Figures
  5

--- Halaman 6 ---
Figure 37: Display Flex Flattening.......................................................................................................... 56
Figure 38: Display Retainer Reassembly............................................................................................... 57
Figure 39: Securing the Display Retainer...............................................................................................57
Figure 40: Speaker Seal Reassembly.................................................................................................... 57
Figure 41: Audio Jack Flex Connector Reassembly...............................................................................57
Figure 42: Audio Jack Flex Connector and Keypad Connector Reassembly.........................................58
Figure 43: Interface Board Reassembly................................................................................................. 58
Figure 44: Board-to-board Flex Cable Reassembly............................................................................... 58
Figure 45: Coax Cable Connector Reassembly..................................................................................... 58
Figure 46: Internal Antenna Reassembly............................................................................................... 59
Figure 47: Back Housing Reassembly................................................................................................... 59
Figure 48: Screws Reassembly..............................................................................................................60
Figure 49: Screws Reassembly Completed........................................................................................... 60
Figure 50: Battery Reassembly.............................................................................................................. 60
Figure 51: Battery Door Reassembly..................................................................................................... 61
Figure 52: Latching Battery Door............................................................................................................61
Figure 53: Antenna Reassembly............................................................................................................ 61
Figure 54: Antenna Screw Reassembly................................................................................................. 61
Figure 55: Antenna Plug Reassembly....................................................................................................62
Figure 56: New Escutcheon Cover Reassembly.................................................................................... 62
Figure 57: Holster Reattachment............................................................................................................63
Figure 58: Non-GOB Model Exploded View........................................................................................... 64
Figure 59: GOB Model Exploded View...................................................................................................66
MN002194A01-AC
List of Figures
6  

--- Halaman 7 ---
List of Tables
Table 1: Radio Frequency Ranges and Power Levels........................................................................... 14
Table 2: Portable Radio Model Numbering Scheme.............................................................................. 16
Table 3: Sales Models – Description of Symbols................................................................................... 16
Table 4: SL2K, UHF1, 403–470 MHz, 3 W, GOB Enabled Model Chart................................................17
Table 5: SL2K, Limited UHF1, 403 – 438 MHz, 3 W, GOB Enabled Model Chart................................. 17
Table 6: SL2K, Limited UHF1, 403 – 470 MHz, 3 W, Non-GOB Enabled Model Chart......................... 18
Table 7: SL2K, UHF1, 403–470 MHz, 3 W, Non-GOB Enabled Model Chart........................................ 18
Table 8: SL2K, UHF2, 450–527 MHz, 3 W, GOB Enabled Model Chart................................................19
Table 9: SL2K, 800 MHz, 806–870 MHz, 2 W, GOB Enabled Model Chart...........................................19
Table 10: Self-Quieter Frequencies........................................................................................................22
Table 11: Military Standards...................................................................................................................23
Table 12: Environmental Specifications................................................................................................. 23
Table 13: Recommended Test Equipment............................................................................................. 24
Table 14: Service Aids Part Number and Part Description.....................................................................25
Table 15: Front Panel Access Test Mode Displays................................................................................29
Table 16: Test Frequencies for UHF...................................................................................................... 30
Table 17: Test Frequencies for 800MHz................................................................................................ 31
Table 18: Transmitter Performance Checks...........................................................................................31
Table 19: Receiver Performance Checks...............................................................................................32
Table 20: Button/Knob/PTT Checks....................................................................................................... 36
Table 21: Keypad Checks...................................................................................................................... 37
Table 22: Software Installation Kits Radio Tuning Setup....................................................................... 40
Table 23: Lead Free Solder Wire Part Number List............................................................................... 44
Table 24: Lead Free Solder Paste Part Number List..............................................................................44
Table 25: Non-GOB Model Exploded View Parts List............................................................................ 64
Table 26: GOB Model Exploded View Parts List.................................................................................... 66
Table 27: Torque Specifications for Screws........................................................................................... 68
Table 28: Types of Error Code............................................................................................................... 69
Table 29: Types of Error Code............................................................................................................... 71
Table 30: UHF1 3W Non-GOB Enabled (403 – 470 MHz) Super Tanapa............................................. 75
Table 31: UHF1 3W GOB/NOB Enabled (403 – 470 MHz) Super Tanapa............................................ 76
Table 32: UHF2 3W GOB Enabled (450 – 527 MHz) Super Tanapa..................................................... 76
Table 33: 800 MHz, 2W GOB Enabled (806 – 870 MHz) Super Tanapa............................................... 76
MN002194A01-AC
List of Tables
  7

--- Halaman 8 ---
Foreword
This manual includes all the information necessary to maintain peak product performance and
maximum working time, using levels 1 and 2 maintenance procedures.
This level of service goes down to the board replacement level and is typical of some local service
centers, Motorola Solutions authorized dealers, self-maintained customers, and distributors.
CAUTION: These servicing instructions are for the use of qualified personnel only. To reduce
the risk of electric shock, do not perform any servicing other than that contained in the
Operating Instructions unless you are qualified to do so. Refer all servicing to qualified service
personnel.
Product Safety and RF Exposure Compliance
CAUTION: Before using this product, read the Product Safety and RF Exposure booklet
enclosed with your radio which contains important operating instructions for safe usage and RF
energy awareness and control for Compliance with applicable Standards and Regulations.
For a list of Motorola Solutions-approved antennas, batteries, and other accessories, visit the following 
web site:http://www.motorolasolutions.com
Computer Software Copyrights
The Motorola Solutions products described in this manual may include copyrighted Motorola Solutions
computer programs stored in semiconductor memories or other media. Laws in the United States and
other countries preserve for Motorola Solutions certain exclusive rights for copyrighted computer
programs, including, but not limited to, the exclusive right to copy or reproduce in any form the
copyrighted computer program. Accordingly, any copyrighted Motorola Solutions computer programs
contained in the Motorola Solutions products described in this manual may not be copied, reproduced,
modified, reverse-engineered, or distributed in any manner without the express written permission of
Motorola Solutions. Furthermore, the purchase of Motorola Solutions products shall not be deemed to
grant either directly or by implication, estoppel, or otherwise, any license under the copyrights, patents
or patent applications of Motorola Solutions, except for the normal non-exclusive license to use that
arises by operation of law in the sale of a product.
Document Copyrights
No duplication or distribution of this document or any portion thereof shall take place without the
express written permission of Motorola Solutions. No part of this manual may be reproduced,
distributed, or transmitted in any form or by any means, electronic or mechanical, for any purpose
without the express written permission of Motorola Solutions.
Disclaimer
The information in this document is carefully examined, and is believed to be entirely reliable.
However, no responsibility is assumed for inaccuracies. Furthermore, Motorola Solutions reserves the
right to make changes to any products herein to improve readability, function, or design. Motorola
Solutions does not assume any liability arising out of the applications or use of any product or circuit
described herein; nor does it cover any license under its patent rights nor the rights of others.
MN002194A01-AC
Foreword
8  

--- Halaman 9 ---
Trademarks
MOTOROLA, MOTO, MOTOROLA SOLUTIONS and the Stylized M logo are trademarks or registered
trademarks of Motorola Trademark Holdings, LLC and are used under license. All other trademarks are
the property of their respective owners.
© 2018 Motorola Solutions, Inc. All rights reserved.
MN002194A01-AC
Foreword
  9

--- Halaman 10 ---
Document History
The following major changes have been implemented in this manual since the previous edition:
Edition Description Date
MN002194A01-AA Initial release. January 2016
MN002194A01-AB Updated Self Quieter Fre-
quencies in Specification sec-
tion.
Added new part number for
LCD Module in Non-GOB and
GOB Exploded View and
Parts List section.
Updated the part number for
Board-to-Board Flex in Non-
GOB and GOB Exploded View
and Parts List section.
December 2017
MN002194A01-AC Replaced LCD display part
number 72013002001 with
DM000115A01 in Non-GOB
and GOB Exploded View and
Parts List sections.
September 2018
MN002194A01-AC
Document History
10  

--- Halaman 11 ---
Related Publication
The following list contains part numbers and titles of related publications.
• 6804110J47, Product Safety and RF Energy Exposure Booklet for Portable Two-Way Radios
• 6866552D01, Multi-Unit Charger User Guide
• 68009553001, Quick Reference Guide/Product Safety and RF Exposure
• 68012004088, MOTOTRBO SL Series SL2K Portables User Guide
• 68012004085, MOTOTRBO SL Series Portables Quick Reference Guide
MN002194A01-AC
Related Publication
  11

--- Halaman 12 ---
Notations Used in This Manual
Throughout the text in this publication, you will notice the use of warning, caution, and notice notations.
These notations are used to emphasize that safety hazards exist, and due care must be taken and
observed.
WARNING: WARNING indicates a potentially hazardous situation which, if not avoided, could
result in death or injury.
CAUTION: CAUTION indicates a potentially hazardous situation which, if not avoided, might
result in equipment damage.
NOTICE: NOTICE indicates an operational procedure, practice, or condition that is essential to
emphasize.
MN002194A01-AC
Notations Used in This Manual
12  

--- Halaman 13 ---
Warranty and Service Support
Motorola Solutions offers long-term support for its products. This support includes full exchange and/or
repair of the product during the warranty period, and service/repair or spare parts support out of
warranty.
Warranty Period and Return Instructions
The terms and conditions of warranty are defined fully in the Motorola Solutions Dealer, Distributor, or
Reseller contract. These conditions may change from time to time and the following notes are for
guidance purposes only. In instances where the product is covered under a "return for replacement" or
"return for repair" warranty, a check of the product should be performed prior to shipping the unit back
to Motorola Solutions. This is to ensure that the product has been correctly programmed or has not
been subjected to damage outside the terms of the warranty.
Prior to shipping any radio back to the appropriate Motorola Solutions warranty depot, please contact
Customer Resources or your Motorola Solutions dealer, distributor, or reseller. All returns must be
accompanied by a Warranty Claim Form, available from your Customer Service representative or
Motorola Online (MOL) or your Motorola Solutions dealer, distributor, or reseller. Products should be
shipped back in the original packaging, or correctly packaged to ensure no damage occurs in transit.
After Warranty Period
After the Warranty period, Motorola Solutions continues to support its products in two ways:
• Motorola Solutions Managed Technical Services (MTS) offers a repair service to both end users
and dealers at competitive prices.
• MTS supplies individual parts and modules that can be purchased by dealers who are technically
capable of performing fault analysis and repair.
MN002194A01-AC
Warranty and Service Support
  13

--- Halaman 14 ---
Chapter 1
Introduction
1.1
Radio Description
These portable radios are available in the following frequency ranges and power levels.
Table 1: Radio Frequency Ranges and Power Levels
Frequency Band Bandwidth Power Level
UHF1 403–470 MHz 1 W (Low Power)
2 W (BT70)
3 W (BT90 and BT100x)
UHF2 450–527 MHz 1 W (Low Power)
2 W (BT70)
3 W (BT90 and BT100x)
800 MHz 806–825 MHz (Tx only)
851–870 MHz (Tx and Rx)
1 W (Low Power)
2 W (High Power)
These digital radios are among the most sophisticated two-way radios available. They have a robust
design for radio users who need high performance, quality, and reliability in their daily communications.
This architecture provides the capability of supporting a multitude of legacy and advanced features
resulting in a more cost-effective two-way radio communications solution.
MN002194A01-AC
Chapter 1:  Introduction
14  

--- Halaman 15 ---
1.1.1
Radio Overview
Figure 1: Display Model
1
2
3
4
5
6
7
8
9
10
11
12
13
14
Label Item Description
1 LED indicators Red, green, and orange light-emitting diodes in-
dicate operating status.
2 Push-to-talk (PTT) Button Press to execute voice operations (For example:
Group call and Private Call).
3 Microphone Allows voice to be sent when PTT or voice oper-
ations are activated.
4 and 12 Front Button These buttons are field programmable using the
CPS.
5 Volume Button To adjust speaker volume.
6 Emergency Button Turns on and off the programmable Emergency
Operations.
7 Audio Jack Interface point for audio accessories to be used
with the radio.
8 Micro USB Port Programs the radio through the computer and
charges the radio through a wall charger.
NOTICE: Charging the radio through
the computer is not supported.
9 Keypad Twelve keys that allow the user to input charac-
ters for various text based operations.
MN002194A01-AC
Chapter 1:  Introduction
  15

--- Halaman 16 ---
Label Item Description
10 Navigation Button To provide menu navigation.
11 Menu/OK Button To select the interface.
13 Liquid Crystal Display (LCD) 320 x 240 Liquid Crystal Display provides visual
information about many radio features.
14 Antenna Provides the needed RF radiation when transmit-
ting or receiving.
1.2
Portable Radio Model Numbering Scheme
Table 2: Portable Radio Model Numbering Scheme
Position 1 2 3 4 5 6 7 8 9 10 11 12 13
Typical Model
Number
AZ H 8 1 Q C N 9 T A 2 A N
Table 3: Sales Models – Description of Symbols
Position Description Value
1 Region AA = North America
AZ = Asia
LA = Latin America
MD = Europe/Middle East/Africa
2 Type of Unit H = Portable
3 Model Series 81 = SL Series
4
5 Band Q = 403 MHz–470 MHz
T = 450 MHz–512 MHz
X = 450 MHz–527 MHz
V = 806 MHz–870 MHz
6 Power Level C = 3 W
7 Physical Packages N = Color Display FKP
8 Channel Information 9 = Variable/Programmable Channel Spacing
9 Primary Operation T = WLAN and Bluetooth Only with embedded GOB
S = WLAN and Bluetooth Only
10 Primary System
Type
A = Conventional
11 Feature Level 2 = Non-FM
12 Version Letter N/A
13 Unique Variation N = Standard Package
MN002194A01-AC
Chapter 1:  Introduction
16  

--- Halaman 17 ---
1.3
Model Charts
NOTICE:
"X" = Part is compatible with checked model.
"_" = The latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
1.3.1
UHF Model Chart
Table 4: SL2K, UHF1, 403–470 MHz, 3 W, GOB Enabled Model Chart
Model/Item Description
AZH81QCN9TA2AN SL2K, 403–470 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, GOB Enabled
PMUE3877_ MOTOTRBO Display Portable (GOB Enabled)
PMAE4078_ Antenna Kit - Band 1 (403–425 MHz)
PMAE4076_ Antenna Kit - Band 2 (420–445 MHz)
PMAE4077_ Antenna Kit - Band 3 (438–470 MHz)
PMHN4332_ Front Housing Assembly with English Keypad
PMHN4330_ Back Housing Assembly
PMHN4333_ Front Housing Assembly with Korean keypad
PMHN4334_ Front Housing Assembly with Stroke keypad
PMHN4335_ Front Housing Assembly with BoPoMoFo keypad
PMLE5083_S Interface Board Assembly Service Kit
PMLE5082_S Main Board Assembly Service Kit for English Keypad Portable
68012004085 MOTOTRBO SL Series SL2K Digital Portable Radios Quick Ref-
erence Guide
68012004088 MOTOTRBO SL2K Portables User Guide
Table 5: SL2K, Limited UHF1, 403 – 438 MHz, 3 W, GOB Enabled Model Chart
Model/Item Description
AZH81QCN9TA2AN SL2K, 403–438 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, GOB Enabled
PMUE3877_ MOTOTRBO Display Portable (GOB Enabled)
PMAE4078_ Antenna Kit - Band 1 (403–425 MHz)
PMAE4076_ Antenna Kit - Band 2 (420–445 MHz)
PMHN4332_ Front Housing Assembly with English Keypad
PMHN4330_ Back Housing Assembly
PMHN4333_ Front Housing Assembly with Korean keypad
PMHN4334_ Front Housing Assembly with Stroke keypad
MN002194A01-AC
Chapter 1:  Introduction
  17

--- Halaman 18 ---
Model/Item Description
AZH81QCN9TA2AN SL2K, 403–438 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, GOB Enabled
PMHN4335_ Front Housing Assembly with BoPoMoFo keypad
PMLE5083_S Interface Board Assembly Service Kit
PMLE5082_S Main Board Assembly Service Kit for English Keypad Portable
68012004085 MOTOTRBO SL Series SL2K Digital Portable Radios Quick Ref-
erence Guide
68012004088 MOTOTRBO SL2K Portables User Guide
Table 6: SL2K, Limited UHF1, 403 – 470 MHz, 3 W, Non-GOB Enabled Model Chart
Model/Item Description
AZH81QCN9SA2AN SL2K, 403–438 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, Non-GOB Enabled
PMUE3876_ MOTOTRBO™ Display Portable (Non-GOB Enabled)
PMAE4078_ Antenna Kit - Band 1 (403–425 MHz)
PMAE4076_ Antenna Kit - Band 2 (420–445 MHz)
PMHN4332_ Front Housing Assembly with English Keypad
PMHN4330_ Back Housing Assembly
PMHN4333_ Front Housing Assembly with Korean keypad
PMHN4334_ Front Housing Assembly with Stroke keypad
PMHN4335_ Front Housing Assembly with BoPoMoFo keypad
PMLE5083_S Interface Board Assembly Service Kit
PMLE5104_S Main Board Assembly Service Kit for English Keypad Portable
68012004085 MOTOTRBO SL Series SL2K Digital Portable Radios Quick Ref-
erence Guide
68012004088 MOTOTRBO SL2K Portables User Guide
Table 7: SL2K, UHF1, 403–470 MHz, 3 W, Non-GOB Enabled Model Chart
Model/Item Description
AZH81QCN9SA2AN SL2K, 403–470 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, Non-GOB Enabled
PMUE3876_ MOTOTRBO™ Display Portable (Non-GOB Enabled)
PMAE4078_ Antenna Kit - Band 1 (403–425 MHz)
PMAE4076_ Antenna Kit - Band 2 (420–445 MHz)
PMAE4077_ Antenna Kit - Band 3 (438–470 MHz)
PMHN4332_ Front Housing Assembly with English Keypad
PMHN4330_ Back Housing Assembly
PMHN4333_ Front Housing Assembly with Korean keypad
MN002194A01-AC
Chapter 1:  Introduction
18  

--- Halaman 19 ---
Model/Item Description
AZH81QCN9SA2AN SL2K, 403–470 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, Non-GOB Enabled
PMHN4334_ Front Housing Assembly with Stroke keypad
PMHN4335_ Front Housing Assembly with BoPoMoFo keypad
PMLE5083_S Interface Board Assembly Service Kit
PMLE5104_S Main Board Assembly Service Kit for English Keypad Portable
68012004085 MOTOTRBO SL Series SL2K Digital Portable Radios Quick Ref-
erence Guide
68012004088 MOTOTRBO SL2K Portables User Guide
1.3.2
UHF2 Model Chart
Table 8: SL2K, UHF2, 450–527 MHz, 3 W, GOB Enabled Model Chart
Model/Item Description
AZH81XCN9TA2AN SL2K, 450–527 MHz, 3 W, Full Keypad Alphanumeric Display
Portable, WIFI, GOB Enabled
PMUE4402_ MOTOTRBO Display Portable (GOB Enabled)
PMAE4091_ Antenna Kit - Band 4 (450–490 MHz)
PMAE4092_ Antenna Kit - Band 5 (480–527 MHz)
PMHN4332_ Front Housing Assembly with English Keypad
PMHN4330_ Back Housing Assembly
PMLE5102_S Interface Board Assembly Service Kit
PMLE5101_S Main Board Assembly Service Kit
68012004085 MOTOTRBO SL Series SL2K Digital Portable Radios Quick Ref-
erence Guide
68012004088 MOTOTRBO SL2K Portables User Guide
1.3.3
800 MHz Model Chart
Table 9: SL2K, 800 MHz, 806–870 MHz, 2 W, GOB Enabled Model Chart
Model/Item Description
AZH81VCN9TB2AN SL2K, 806–870 MHz, 2 W, Full Keypad Alphanumeric Display
Portable, WIFI, GOB Enabled
PMUF1630_ MOTOTRBO Display Portable (GOB Enabled)
PMAF4017_ Antenna 800 MHz (806–870 MHz)
PMHN4332_ Front Housing Assembly with English Keypad
PMHN4330_ Back Housing Assembly
MN002194A01-AC
Chapter 1:  Introduction
  19

--- Halaman 20 ---
Model/Item Description
AZH81VCN9TB2AN SL2K, 806–870 MHz, 2 W, Full Keypad Alphanumeric Display
Portable, WIFI, GOB Enabled
PMLF4170_S Interface Board Service Kit, 800 MHz
PMLF4169_S Main Board Service Kit, 800 MHz
68012004085 MOTOTRBO SL Series SL2K Digital Portable Radios Quick Ref-
erence Guide
68012004088 MOTOTRBO SL2K Portables User Guide
1.4
Specifications
General Value
Channel Capacity 1000
Frequency • UHF1: 403–470 MHz
• UHF2: 450–527 MHz
• 800 MHz:
806–825 MHz (Tx Only)
851–870 MHz (Rx and Tx)
Dimensions (HxWxT):
• with BT70 battery
• with BT90 battery
• with BT100x battery
• 121 x 55 x 17.4 mm
• 121 x 55 x 19.8 mm
• 121 x 55 x 22.9 mm
Weight:
• with BT70 battery
• with BT90 battery
• with BT100x battery
• 154 g
• 164 g
• 174 g
Power Supply 3.7 V nominal
FCC Description • UHF1: AZ489FT7072
• UHF2: AZ489FT7073
• 800 MHz: AZ489FT7074
IC Description • UHF1: 109U-89FT7072
• UHF2: 109U-89FT7073
• 800 MHz: 109U-89FT7074
Average battery life at 5/5/90 duty cycle with battery saver enabled
BT70 1370 mAh battery UHF1/ UHF2: N/A
BT90 1800 mAh battery • UHF1/ UHF2: 11.3 hrs
• 800 MHz: 11.3 hrs
MN002194A01-AC
Chapter 1:  Introduction
20  

--- Halaman 21 ---
General Value
BT100x 2300 mAh battery • UHF1/ UHF2: 14.3 hrs
• 800 MHz: 13.5 hrs
Receiver Value
Frequencies • UHF1: 403–470 MHz
• UHF2: 450–527 MHz
• 800 MHz: 851–870 MHz
Channel Spacing 12.5 kHz
Frequency Stability (-30 °C to +60 °C) +/-1.5 ppm
Digital Sensitivity 5 % BER: 0.3 µV
Intermodulation (ETSI-EN300 113-1) 65 dB
Adjacent Channel Selectivity (ETSI-EN300
113-1)
60 dB @ 12.5 kHz
Spurious Rejection (ETSI-EN300 113-1) 70 dB
Rated Audio 500 mW
Audio Distortion @ Rated Audio 3 % (typical)
Digital Hum and Noise -40 dB @ 12.5 kHz
Conducted Spurious Emission (ETSI-EN300
113-1)
-57 dBm
Transmitter Value
Frequencies • UHF1: 403–470 MHz
• UHF2: 450–527 MHz
• 800 MHz: 806–870 MHz
Frequency Stability (-30 °C to +60 °C) +/-1.5 ppm
Power Output (Low Power) 1 W
Power Output (High Power) • UHF1/ UHF2: 3 Watt
• 800 MHz: 2 Watt
Digital Hum and Noise -40 dB @ 12.5 kHz
Conducted / Radiated Emission • -36 dBm < 1 GHz
• -30 dBm > 1 GHz
Digital Adjacent Channel Power 60 dB @ 12.5 kHz
Audio Response +1, -3 dBm
Audio Distortion 3 %
4FSK Digital Modulation • 12.5 kHz Data: 7K60F1D and 7K60FXD
MN002194A01-AC
Chapter 1:  Introduction
  21

--- Halaman 22 ---
Transmitter Value
• 12.5 kHz Voice: 7K60F1E and 7K60FXE
• Combination of 12.5 kHz Data and Voice:
7K60F1W
Digital Vocoder Type AMBE+2
Digital Protocol ETSI TS 102 361 -1,-2,-3
Table 10: Self-Quieter Frequencies
UHF1 UHF2 800 MHz
403.200 MHz ± 5 kHz 451.200 MHz ± 5kHz 852.000 MHz ± 5kHz
405.600 MHz ± 5 kHz 453.600 MHz ± 5kHz 853.335 MHz ± 5kHz
408.000 MHz ± 5 kHz 455.000 MHz ± 5kHz 854.320 MHz ± 5kHz
410.400 MHz ± 5 kHz 456.000 MHz ± 5kHz 854.400 MHz ± 5kHz
412.800 MHz ± 5 kHz 459.800 MHz ± 5kHz 854.480 MHz ± 5kHz
415.200 MHz ± 5 kHz 460.800 MHz ± 5kHz 856.800 MHz ± 5kHz
417.600 MHz + ± 5 kHz 465.600 MHz ± 5kHz 859.200 MHz ± 5kHz
420.000 MHz ± 5 kHz 467.840 MHz ± 40kHz 862.000 MHz ± 5kHz
422.400 MHz ± 5 kHz 468.040 MHz ± 40kHz 863.960 MHz ± 5kHz
424.800 MHz ± 5 kHz 468.160 MHz ± 40kHz 864.040 MHz ± 40kHz
427.200 MHz ± 5 kHz 470.400 MHz ± 5kHz 866.400 MHz ± 5kHz
429.600 MHz ± 5 kHz 472.800 MHz ± 5kHz 868.800 MHz ± 5kHz
431.960 MHz ± 40 kHz 475.200 MHz ± 5kHz -
432.040 MHz ± 40 kHz 477.600 MHz ± 5kHz -
434.400 MHz ± 5 kHz 480.000 MHz ± 5kHz -
436.800 MHz ± 5 kHz 484.800 MHz ± 5kHz -
439.200 MHz± 5 kHz 487.200 MHz ± 5kHz -
440.000 MHz ± 5 kHz 489.600 MHz ± 5kHz -
441.600 MHz ± 5 kHz 492.000 MHz ± 5kHz -
444.000 MHz ± 5 kHz 494.400 MHz ± 5kHz -
446.400 MHz ± 5 kHz 499.200 MHz ± 5kHz -
448.800 MHz ± 5 kHz 501.600 MHz ± 5kHz -
451.200 MHz ± 5 kHz 504.000 MHz ± 40kHz -
456.000 MHz ± 5 kHz 506.400 MHz ± 5kHz -
460.800 MHz ± 5 kHz 508.800 MHz ± 5kHz -
465.600 MHz ± 5 kHz 511.200 MHz ± 5kHz -
467.960 MHz ± 40 kHz 513.600 MHz ± 5kHz -
468.040 MHz ± 40 kHz 517.400 MHz± 5kHz -
MN002194A01-AC
Chapter 1:  Introduction
22  

--- Halaman 23 ---
UHF1 UHF2 800 MHz
- 518.400 MHz± 5kHz -
- 520.000 MHz± 5kHz -
- 523.200 MHz± 5kHz -
Table 11: Military Standards
Parameter Military Standards
Applicable MIL–STD MIL 810F Methods/ Proce-
dures
MIL 810G Methods/ Proce-
dures
Low Pressure 500.4/ Procedure II 500.5/ Procedure II
High Temperature 501.4/ Procedure I/Hot, Proce-
dure II/Hot
501.5/ Procedure I/ A1, Proce-
dure II/A1
Low Temperature 502.4/ Procedure I/ C1, Proce-
dure II/ C1
502.5/ Procedure I/ C1, Proce-
dure II/ C1
Temperature Shock 503.4/ Procedure I 503.5/ Procedure I/C
Solar Radiation 505.4/ Procedure I 505.5/ Procedure I/ A1
Rain 506.4/ Procedure I 506.5/ Procedure I
Dust 510.4/ Procedure I 510.5/ Procedure I
Vibration 514.5/ Procedure I/24 514.6/ Procedure I/24
Shock 516.5/ Procedure IV 516.6/ Procedure IV, VI
Table 12: Environmental Specifications
Parameter Value
Operating Temperature1 -10 °C to +60 °C
Storage Temperature -30 °C to +70 °C
ESD IEC 61000-4-2
Water & Dust Intrusion IP54
Humidity 8 hour soak @ +50 °C and 95 % RH
Salt Fog 8 hours exposure to 5 % saline solution Sodium
Chloride (NaCI) at 35 °C, 16 hours standing pe-
riod
1 Operating temperature specification for a Non Lithium-Ion (Li-Ion) battery is -20 °C to +60 °C.
MN002194A01-AC
Chapter 1:  Introduction
  23

--- Halaman 24 ---
Chapter 2
Test Equipment and Service Aids
This chapter lists the recommended test equipment and service aids, as well as information on field
programming equipment that can be used in servicing and programming Motorola Solutions radios.
2.1
Recommended Test Equipment
The list of equipment contained in Table 13: Recommended Test Equipment on page 24 includes
most of the standard test equipment required for servicing Motorola Solutions portable radios.
Table 13: Recommended Test Equipment
Equipment Characteristics Example Application
Service
Monitor
Can be used as a sub-
stitute.
Aeroflex Digital Radio Test
Set Model 3920 with DMR
option.
Frequency/deviation meter
and signal generator for
wide-range troubleshooting
and alignment.
Digital RMS
Multimeter 2
100 µV to 300 V Fluke 179 (www.fluke.com) or
equivalent.
AC/DC voltage and 
current measurements. Au-
dio voltage measurements.5 Hz to 1 MHz
10 ㏁ Impedance
RF Signal 
Generator 2
100 MHz to 1 GHz Agilent 443X, R&S Signal
Generator
Receiver measurements
-130 dBm to +10 dBm
FM Modulation: 0 kHz
to 10 kHz
Audio Frequency: 100
Hz to 10 kHz
Oscillo-
scope2
2 Channel Leader LS8050 
(www.leaderusa.com), 
Tektronix TDS1001b
(www.tektronix.com),
or equivalent.
Waveform measurements
50 MHz Bandwidth
5 mV/div to 20 V/div
Power Meter
and Sensor 2
5% Accuracy Bird 43 Thruline Watt Meter
(www.bird-electronic.com) or
equivalent.
Transmitter power output 
measurements100 MHz to 500 MHz
50 Watts
RF Millivolt
Meter
100 mV to 3 V RF Boonton 92EA 
(www.boonton.com) or equiv-
alent.
RF level measurements
10 kHz to 1 GHz
Power Sup-
ply
0 V to 32 V B&K Precision 1790 
(www.bkprecision.com) 
or equivalent.
Voltage supply
0 A to 20 A
2 Service Monitor can be used as a substitute .
MN002194A01-AC
Chapter 2:  Test Equipment and Service Aids
24  

--- Halaman 25 ---
2.2
Service Aids
The following table lists the service aids recommended for working on the radio. While all of these
items are available from Motorola Solutions, most are standard workshop equipment items, and any
equivalent item capable of the same performance may be substituted for the item listed.
Table 14: Service Aids Part Number and Part Description
Motorola Solutions Part No. Description Application
CB000262A01 Micro USB Programming Ca-
ble
This cable connects the radio
to a USB port for radio pro-
gramming and data applica-
tions.
TL000068A01 RF Antenna Adaptor (SMA
Female)
Adapts radio antenna port to
test equipment.
PMNN4429_ Battery Eliminator Connects to radio through bat-
tery eliminator cable.
EN000099A01 RF Antenna Adaptor Holder Holds the RF antenna adaptor
PMVN4130_ Customer Programming 
Software and AirTracer on 
CD-ROM
CPS allows Dealers/Distribu-
tors to program radio parame-
ters. AirTracer allows the cap-
turing of radio traffic into logs
for analysis by Motorola Solu-
tions.
PMVN4131_ MOTOTRBO Tuner CD Radio Tuning. Only Motorola
Solutions Service Centers or
Authorized Motorola Solutions
Service Dealers can perform
this function.
MN002194A01-AC
Chapter 2:  Test Equipment and Service Aids
  25

--- Halaman 26 ---
Chapter 3
Transceiver Performance Testing
These radios meet published specifications through their manufacturing process by utilizing high-
accuracy laboratory-quality test equipment.
The recommended field service equipment approaches the accuracy of the manufacturing equipment
with few exceptions. This accuracy must be maintained in compliance with the calibration schedule
recommended by the manufacturer.
Although these radios function in digital and analog modes, all testing is done in analog mode.
3.1
Setup
Supply voltage is provided using a 3.7 VDC power supply. The equipment required for alignment
procedures is connected as shown in the Radio Tuning Equipment Setup Diagram.
WARNING: Do NOT use any form of connector, for example wires, crocodile clips, and probes,
to supply voltage to the radio, other than the Motorola Solutions approved battery eliminator.
Set up the DMR Transmitter and Receiver Test as per the following figure:
1 Connect the Micro USB Programming cable to the radio and to the computer.
2 Remove the radio name plate label and the blue RF plug as shown in Figure 3: Name plate label on
page 27 and Figure 4: RF plug on page 28.
3 Connect the RF antenna adapter to the 50 Ω RF Input/Output port of the radio using the RF
antenna adapter holder as shown in Figure 5: Connect RF Antenna adaptor to radio RF input/output
port on page 29.
4 Connect the other end of the RF antenna adapter to the T/R port of the Radio Test Set 3920 using
the RF cable shown in Figure 2: DMR Radio Transmitter and Receiver Testing Setup on page 26.
Figure 2: DMR Radio Transmitter and Receiver Testing Setup
T/R Port
Power Supply
Ant. Input / Output
Modulated RF Test
Signal / Tx
modulated RF Signal
CB000262A01
Battery Eliminator
Micro USB
Programming Cable
MN002194A01-AC
Chapter 3:  Transceiver Performance Testing
26  

--- Halaman 27 ---
Figure 3: Name plate label
1
Label Description
1 Name Plate Label
MN002194A01-AC
Chapter 3:  Transceiver Performance Testing
  27

--- Halaman 28 ---
Figure 4: RF plug
1
Label Description
1 RF Plug
MN002194A01-AC
Chapter 3:  Transceiver Performance Testing
28  

--- Halaman 29 ---
Figure 5: Connect RF Antenna adaptor to radio RF input/output port
1
2
Label Description
1 RF Antenna Adaptor Holder (EN000099A01)
2 RF Antenna Adaptor (TL000068A01)
3.2
Test Mode
3.2.1
Entering Display Radio Test Mode
Procedure:
1 Turn the radio on.
2 Within 10 seconds after Self-Test is completed, press the P2 button five times in succession.
The radio beeps and shows a series of displays regarding various version numbers and
subscriber-specific information. The displays are described in the following table.
Table 15: Front Panel Access Test Mode Displays
Name of Display Description Appears
Service Mode The literal string indicates the radio has entered test
mode.
Always
Host Version The version of host firmware. Always
DSP Version The version of DSP firmware. Always
MN002194A01-AC
Chapter 3:  Transceiver Performance Testing
  29

--- Halaman 30 ---
Name of Display Description Appears
Model Number The radio model number as programmed in the codeplug. Always
MSN The radio serial number as programmed in the codeplug. Always
FLASHCODE The FLASH codes as programmed in the codeplug. Always
RF Band The radio band. Always
NOTICE: The radio stops at each display for 2 seconds before moving to the next
information display. If the information cannot fit into one line, the radio display scrolls
automatically character by character after 1 second to view the whole information. If the
Left button is pressed before the last information is displayed, the radio suspends the
information display until the user presses the Right button to resume the information
display. The last display shows RF Test Mode .
3.2.2
RF Test Mode
When the radio is operating in its normal environment, the radio microcontroller controls the RF
channel selection, transmitter key-up, and receiver muting, according to the customer codeplug
configuration.
However, when the unit is on the bench for testing, alignment, or repair, it must be removed from its
normal environment with a special routine, called Test Mode.
3.2.2.1
Testing RF Channel Selections
In RF Test Mode, the display upon the first line is RF Test . The display upon the second line is the
test environment, the channel number, and channel spacing.
Prerequisites:
NOTICE: The default test environment is DIG.
Procedure:
1 Press of channel selector button cycle through the test channel 1->2->3->4->5->6->7->8->9-
>10->11->12->13->14->15->16->1 as described in the following Test Frequencies. The radio
beeps in each position. Frequency units in the table below is in MHz.
NOTICE: DIG is digital mode.
Table 16: Test Frequencies for UHF
Frequency UHF1 RX UHF1 TX UHF2 RX UHF2 TX
F1 & F9 403.075 403.075 450.05 450.05
F2 & F10 414.075 414.075 462.55 462.55
F3 & F11 425.075 425.075 474.95 474.95
F4 & F12 436.075 436.075 487.35 487.35
F5 & F13 447.075 447.075 499.75 499.75
MN002194A01-AC
Chapter 3:  Transceiver Performance Testing
30  
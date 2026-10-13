--- Halaman 1 ---
tTitle Page
SL1M Portable Radio
Basic Service Manual
MN000916A01-AA
tttt
Final Draft

--- Halaman 2 ---
Final Draft

--- Halaman 3 ---
iii
Foreword
This manual covers all models of the SL1M Portable Radios, unless otherwise specified. It includes all the information 
necessary to maintain peak product performance and maximum working time, using levels 1 and 2 maintenance 
procedures. This level of service goes down to the board replacement level and is typical of some local service centers, 
self-maintained customers, and distributors.
Product Safety and RF Exposure Compliance
For a list of Motorola-approved antennas, batteries, and other accessories, visit the following web site: 
http://www.motorolasolutions.com
Computer Software Copyrights
The Motorola products described in this manual may include copyrighted Motorola computer programs stored in 
semiconductor memories or other media. Laws in the United States and other countries preserve for Motorola certain 
exclusive rights for copyrighted computer programs, including, but not limited to, the exclusive right to copy or reproduce in 
any form the copyrighted computer program. Accordingly, any copyrighted Motorola computer programs contained in the 
Motorola products described in this manual may not be copied, reproduced, modified, reverse-engineered, or distributed in 
any manner without the express written permission of Motorola. Furthermore, the purchase of Motorola products shall not 
be deemed to grant either directly or by implication, estoppel, or otherwise, any license under the copyrights, patents or 
patent applications of Motorola, except for the normal non-exclusive license to use that arises by operation of law in the 
sale of a product.
Document Copyrights
No duplication or distribution of this document or any portion thereof shall take place without the express written permission 
of Motorola. No part of this manual may be reproduced, distributed, or transmitted in any form or by any means, electronic 
or mechanical, for any purpose without the express written permission of Motorola.
Disclaimer
The information in this document is carefully examined, and is believed to be entirely reliable. However, no responsibility is 
assumed for inaccuracies. Furthermore, Motorola reserves the right to make changes to any products herein to improve 
readability, function, or design. Motorola does not assume any liability arising out of the applications or use of any product 
or circuit described herein; nor does it cover any license under its patent rights nor the rights of others.
Trademarks
MOTOROLA, MOTO, MOTOROLA SOLUTIONS and the Stylized M logo are trademarks or registered trademarks of 
Motorola Trademark Holdings, LLC and are used under license. All other trademarks are the property of their respective 
owners.
© 2014 Motorola Solutions, Inc.
All rights reserved.
ATTENTION! Before using this radio, read the guide enclosed with your 
radio which contains important operating instructions for 
safe usage and RF energy awareness and control for 
compliance with applicable standards and regulations.
Final Draft

--- Halaman 4 ---
Notes
Final Draft

--- Halaman 5 ---
v
Document History
The following major changes have been implemented in this manual since the previous edition:
Edition Description Date
MN000916A01-AA Initial Release Sept. 2014
Final Draft

--- Halaman 6 ---
vi
Notes
Final Draft

--- Halaman 7 ---
Table of Contents vii
Table of Contents
Foreword........................................................................................................iii
Product Safety and RF Exposure Compliance...................................................................................... .....iii
Computer Software Copyrights .................................................................................................................. iii
Document Copyrights............................................................................................................ ..................... iii
Disclaimer................................................................................................................................................... iii
Trademarks ................................................................................................................................................ iii
Document History ......................................................................................... v
Commercial Warranty ................................................................................xvii
Limited Warranty ..................................................................................................................................... xvii
MOTOROLA COMMUNICATION PRODUCTS........................................................................... xvii
I. What This Warranty Covers And For How Long .................................................................. xvii
II. General Provisions......................................................................................................... ..... xvii
III. State Law Rights ......................................................................................................... ..... xviii
IV. How To Get Warranty Service .......................................................................................... xviii
V. What This Warranty Does Not Cover................................................................................. xviii
VI. Patent And Software Provisions ......................................................................................... xix
VII. Governing Law............................................................................................................. ...... xix
Battery and Charger Warranty ....................................................................xx
Workmanship Warranty........................................................................................................... ..................xx
Capacity Warranty.............................................................................................................. .......................xx
Chapter 1 Introduction ........... .............................................................. 1-1
1.1 Notations Used in This Manual............................................................................................... ..... 1-1
1.2 Radio Description ........................................................................................................... ............. 1-1
1.2.1 Radio Overview ............................................................................................................ ... 1-2
1.3 Portable Radio Model Numbering Scheme ................................................................................. 1-3
1.4 Model Charts ................................................................................................................ ............... 1-4
1.4.1 VHF (136–174 MHz) 2–3W Model Chart...... ................................................................... 1-4
1.4.2 UHF (403–470 MHz) 2–3W Model Chart ..... ................................................................... 1-5
1.5 Specifications............................................................................................................................... 1-6
Chapter 2 Test Equipment and Service Aids ..................................... 2-1
2.1 Recommended Test Equipment ........................ .......................................................................... 2-1
2.2 Service Aids................................................................................................................ ................. 2-2
2.3 Portable Programming Cable .................................................................................................. .... 2-3
2.4 Micro USB Programming Cable......................... .......................................................................... 2-4
2.5 Audio Test Cable ............................................................................................................ ............. 2-5
Final Draft

--- Halaman 8 ---
viii Table of Contents
Chapter 3 Transceiver Performance Testing ........ ............................. 3-1
3.1 General ........................................................................................................................................ 3-1
3.2 Setup............................................................................................................................................ 3-1
3.3 Test Mode ................................................................................................................... ................. 3-2
3.3.1 Power Up Test Mode....................................................................................................... 3 -2
3.3.1.1 Display Model ................................................................................................... 3-2
3.3.2 Front Panel AccessTest Mode......................................................................................... 3-2
3.3.2.1 Display Model ................................................................................................... 3-2
3.3.3 RF Test Mode.............................................................................................................. .... 3-2
3.3.3.1 Display Model ................................................................................................... 3-2
3.3.4 LED Status Test Mode..................................................................................................... 3 -8
3.3.4.1 Display Model ................................................................................................... 3-8
3.3.5 LED Display Matrix Test Mode ........................................................................................ 3-8
3.3.5.1 Display Model ................................................................................................... 3-8
3.3.6 Speaker Tone Test Mode ................................................................................................ 3-8
3.3.6.1 Display Model ................................................................................................... 3-8
3.3.7 Earpiece Tone Test Mode ............................................................................................... 3-8
3.3.7.1 Display Model ................................................................................................... 3-8
3.3.8 Audio Loopback Earpiece Test..................... ................................................................... 3-8
3.3.8.1 Display Model ................................................................................................... 3-8
3.3.9 Battery Check Test Mode ................................................................................................ 3-9
3.3.9.1 Display Model ................................................................................................... 3-9
3.3.10 Button Test Mode ......................................................................................................... ... 3-9
3.3.10.1 Display Model ................................................................................................... 3-9
Chapter 4 Radio Programming and Tuning ....................................... 4-1
4.1 Introduction .................................................................................................................................. 4-1
4.2 Customer Programming Software Setup ............... ...................................................................... 4-1
4.3 AirTracer Application Tool.................................................................................................. .......... 4-3
4.4 Radio Tuning Setup .......................................................................................................... ........... 4-3
Chapter 5 Disassembly And Reassembly Procedures ..................... 5-1
5.1 Introduction .................................................................................................................................. 5-1
5.2 Preventive Maintenance ...................................................................................................... ........ 5-1
5.2.1 Inspection ................................................................................................................ ........ 5-2
5.2.2 Cleaning Procedures ....................................................................................................... 5-2
5.3 Safe Handling of CMOS and LDMOS Devices ............................................................................ 5-3
5.4 Repair Procedures and Techniqu es – General............................................................................ 5-4
5.5 Disassembling and Reassembling the Radio – Gene ral.............................................................. 5-5
5.6 Radio Disassembly – Detailed ................................................................................................ ..... 5-6
5.6.1 Holster Disassembly....................................................................................................... .5 - 6
5.6.2 External Antenna Disassembly........................................................................................ 5-6
5.6.3 Back Housing Disassembly ............................................................................................. 5-7
5.6.4 Main PCB Disassembly ................................................................................................. 5-11
5.6.5 Audio Jack Flex, Micro USB Flex, Microp hone (MIC), Speaker Flex, LCD Display, and 
Internal Antenna Disassembly....................................................................................... 5-13
5.6.6 Dust Cover Disassembly ............................................................................................... 5-15
5.7 Radio Reassembly – Detailed................................................................................................. ... 5-16
5.7.1 Dust Cover Reassembly................................................................................................ 5-16
Final Draft

--- Halaman 9 ---
Table of Contents ix
5.7.2 Internal Antenna Reassembly ....................................................................................... 5-17
5.7.3 LCD Display Reassembly................................ .............................................................. 5-18
5.7.4 Audio Jack Flex, Micro USB Flex, Micr ophone (MIC), Speaker Flex, LCD Display, and 
Internal Antenna Reassembly ....................................................................................... 5-18
5.7.5 Internal Frame Reassembly .......................................................................................... 5-19
5.7.6 Main PCB Reassembly.................................................................................................. 5-20
5.7.7 Back Housing Reassembly........................... ................................................................. 5-21
5.7.8 External Antenna Reassembly ..................... ................................................................. 5-24
5.7.9 Holster Reassembly ...................................................................................................... 5- 24
5.8 Radio Exploded Mechanical Views and Parts Lists................................................................... 5-25
5.9 Torque Chart................................................................................................................ .............. 5-27
Chapter 6 Basic Troubleshoot ing ....................................................... 6-1
6.1 Introduction ................................................................................................................ .................. 6-1
6.2 Power-Up Error Codes ........................................................................................................ ........ 6-1
6.3 Operational Error Codes.... .......................................................................................................... 6-3
Appendix A EMEA Regional Warranty,  Service and Technical Support ..
..............................................................................................A-1
A.1 Warranty and Service Support................................................................................................ .....A-1
A.1.1 Warranty Period and Return  Instructions ........................................................................A-1
A.1.2 After Warranty Period..................................................................................................... .A-1
A.2 European Radio Support Centre (ERSC) ....................................................................................A-2
A.3 Piece Parts ................................................................................................................. .................A-2
A.4 Technical Support........................................................................................................... .............A-3
A.5 Further Assistance From Motorola ............................................................................................ ..A-3
Glossary.........................................................................................Glossary-1
Final Draft

--- Halaman 10 ---
x Table of Contents
Notes
Final Draft

--- Halaman 11 ---
List of Figures xi
List of Figures
Figure 1-1. Display Model ............................... ....................................................................................... 1-2
Figure 1-2. Portable Radio Model Numbering Scheme.......................................................................... 1-3
Figure 2-1. Portable Programming Cable with TTR (P MKN4128_)........................................................ 2-3
Figure 2-2. Micro USB Programming Cable (CB000262 A01) ................................................................ 2-4
Figure 2-3. Audio Test Cable (CB000233A01) ...................................................................................... .2 - 5
Figure 3-1. Power-Up Screen Icon..................... .................................................................................... 3-2
Figure 3-2. Channel Profile Scre en Icon ................................................................................................ 3-3
Figure 4-1. CPS Programming Setup............................................................................................... ...... 4-1
Figure 4-2. Connecting RF Antenna Adaptor To Radio RF Input/Output Port........................................ 4-2
Figure 4-3. RF Plug ............................................................................................................. ................... 4-2
Figure 4-4. Radio Tuning Equipment Setup ........... ................................................................................ 4-3
Figure 5-1. Holster Removal ..... ............................................................................................................. 5-6
Figure 5-2. External Antenna Removal ............................................................................................ ...... 5-6
Figure 5-3. Screw Plug Removal........................ .................................................................................... 5-7
Figure 5-4. RF Plug Removal..................................................................................................... ............ 5-7
Figure 5-5. Unlock The Battery Door.................. .................................................................................... 5-8
Figure 5-6. Battery Door Remova l................................................................................................ .......... 5-8
Figure 5-7. Battery Removal .............................. .................................................................................... 5-9
Figure 5-8. Screw Removal....................................................................................................... ............. 5-9
Figure 5-9. Back Housing Removal........................ .............................................................................. 5-10
Figure 5-10. Back Housing Removal........................ .............................................................................. 5-10
Figure 5-11. PCB Catch Disassemb ly.............................................................................................. ...... 5-11
Figure 5-12. Uplifting Of The Main PCB.......................................................................................... ....... 5-11
Figure 5-13. Audio Jack, Speaker, Micro USB, Microp hone Flex, and Display Flex Disassembly......... 5-12
Figure 5-14. Internal Fram e Screws Disassembly.................................................................................. 5-13
Figure 5-15. Internal Frame Disassembly ................ .............................................................................. 5-13
Figure 5-16. Speaker Disassembly ........................................................................................................ 5-14
Figure 5-17. Display Module Disassembly ............... .............................................................................. 5-14
Figure 5-18. Internal An tenna Disassembly ........................................................................................... 5-15
Figure 5-19. Dust Cover Head Re moval ................................................................................................ 5-15
Figure 5-20. Dust Cover Removal. ......................................................................................................... 5-16
Figure 5-21. Dust Cover Tail Insertion.......................................................................................... .......... 5-16
Figure 5-22. Dust Cover Tail Full In sertion Into Housing........................................................................ 5-17
Figure 5-23. Internal An tenna Reassembly........................................................................................ .... 5-17
Figure 5-24. Display Module Reas sembly.......................................................................................... .... 5-18
Figure 5-25. Speaker Reassembly . ........................................................................................................ 5-18
Figure 5-26. Internal Fr ame Reassembly.......................................................................................... ..... 5-19
Figure 5-27. Internal Fram e Screws Reassembly .................................................................................. 5-19
Fig
ure 5-28. Audio Jack, Speaker, Micro USB, Microp hone Flex, and Display Flex Reassembly ......... 5-20
Figure 5-29. Main PCB Reassembly ........................ .............................................................................. 5-21
Figure 5-30. Back Housing Reassembly .................. .............................................................................. 5-21
Figure 5-31. Screw Reassembly .......................... .................................................................................. 5-22
Figure 5-32. Battery Reas sembly................................................................................................. .......... 5-22
Figure 5-33. Lock The Battery Door .............................................................................................. ......... 5-23
Figure 5-34. Attaching One RF Plug And Two Screw Pl ugs .................................................................. 5-23
Figure 5-35. External Antenna Reassembly............. .............................................................................. 5-24
Figure 5-36. External Antenna Reassembly............. .............................................................................. 5-24
Figure 5-37. SL1600Exploded View................................................................................................ ....... 5-25
Final Draft

--- Halaman 12 ---
xii List of Figures
Notes
Final Draft

--- Halaman 13 ---
List of Tables xiii
List of Tables
Table 1-1. Radio Frequency Ranges and Power Levels.......................... ............................................. 1-1
Table 2-1. Recommended Test Equipment........................................................................................... 2-1
Table 2-2. Service Aids ......................................................................................................... ................ 2-2
Table 2-3. Pin Configuration of Portable Programming Cable with TTR............................................... 2-3
Table 2-4. Pin Configuration of Micro USB Programming Cable .......................................................... 2-4
Table 2-5. Pin Configuration of Audio Test Cable ................................................................................ .2 - 5
Table 3-1. Initial Equipment Control Settings................................................................................... ..... 3-1
Table 3-2. Test Environments.................................................................................................... ............ 3-3
Table 3-3. Test Frequencies..................................................................................................... ............. 3-4
Table 3-4. Transmitter Performance Checks ....................................................................................... .3 - 5
Table 3-5. Receiver Performance Checks .......................................................................................... .. 3-7
Table 4-1. Software Installation Kits Radio Tuning Se tup ..................................................................... 4-1
Table 5-1. Lead Free Solder Wire Part Number List............................................................................. 5-4
Table 5-2. Lead Free Solder Paste Part Number List ........................................................................... 5-4
Table 5-3.  SL1600 Exploded View Parts List ..................................................................................... 5-26
Table 5-4. Torque Specifications for Screws ..................................................................................... .. 5-27
Table 6-1. Power-Up Error Codes................................................................................................. ........ 6-1
Table 6-2. Operational Error Code s ...................................................................................................... 6-3
Final Draft

--- Halaman 14 ---
xiv List of Tables
Notes
Final Draft

--- Halaman 15 ---
Related Publications xv
Related Publications
Product Safety and RF Exposure ................................................................................................. 6804110J47
Multi-Unit Charger User Guide ....................................................................................................6866552D01
Quick Reference Guide/Product Safety and RF Exposure........................................................ 68009553001
MOTOTRBO SL1M Portable User Guide ................................................................................ MN000892A01
MOTOTRBO SL1M Portable Quick Reference Guide............................................................. MN000899A01
MOTOTRBO SL1M CMM Leaflet ............................................................................................ MN000898A01
Final Draft

--- Halaman 16 ---
xvi List of Tables
Notes
Final Draft

--- Halaman 17 ---
Commercial Warranty xvii
Commercial Warranty
Limited Warranty
MOTOROLA COMMUNICATION PRODUCTS
I. What This Warranty Covers And For How Long
MOTOROLA SOLUTIONS INC. (“MOTOROLA”) warrants the MOTOROLA manufactured 
Communication Products listed below (“Product”) against defects in material and workmanship 
under normal use and service for a period of time from the date of purchase as scheduled below:
Motorola, at its option, will at no charge either repair the Product (with new or reconditioned parts), 
replace it (with a new or reconditioned Product), or refund the purchase price of the Product during 
the warranty period provided it is returned in accordance with the terms of this warranty. Replaced 
parts or boards are warranted for the balance of the original applicable warranty period. All replaced 
parts of Product shall become the property of MOTOROLA.
This express limited warranty is extended by MOTOROLA to the original end user purchaser only 
and is not assignable or transferable to any other party. This is the complete warranty for the Product 
manufactured by MOTOROLA. MOTOROLA assumes no obligations or liability for additions or 
modifications to this warranty unless made in writing and signed by an officer of MOTOROLA. 
Unless made in a separate agreement between MOTOROLA and the original end user purchaser, 
MOTOROLA does not warrant the installation, maintenance or service of the Product.
MOTOROLA cannot be responsible in any way for any ancillary equipment not furnished by 
MOTOROLA which is attached to or used in connection with the Product, or for operation of the 
Product with any ancillary equipment, and all such equipment is expressly excluded from this 
warranty. Because each system which may use the Product is unique, MOTOROLA disclaims 
liability for range, coverage, or operation of the system as a whole under this warranty.
II. General Provisions
This warranty sets forth the full extent of MOTOROLA'S responsibilities regarding the Product. 
Repair, replacement or refund of the purchase price, at MOTOROLA's option, is the exclusive 
remedy. THIS WARRANTY IS GIVEN IN LIEU OF ALL OTHER EXPRESS WARRANTIES. IMPLIED 
WARRANTIES, INCLUDING WITHOUT LIMITATION, IMPLIED WARRANTIES OF 
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, ARE LIMITED TO THE 
DURATION OF THIS LIMITED WARRANTY. IN NO EVENT SHALL MOTOROLA BE LIABLE FOR 
DAMAGES IN EXCESS OF THE PURCHASE PRICE OF THE PRODUCT, FOR ANY LOSS OF 
USE, LOSS OF TIME, INCONVENIENCE, COMMERCIAL LOSS, LOST PROFITS OR SAVINGS 
OR OTHER INCIDENTAL, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE 
USE OR INABILITY TO USE SUCH PRODUCT, TO THE FULL EXTENT SUCH MAY BE 
DISCLAIMED BY LAW.
SL1M Portable Radios 24 Months
Product Accessories (Including Batteries and Chargers) 12 Months
Final Draft

--- Halaman 18 ---
xviii Commercial Warranty 
III. State Law Rights 
SOME STATES DO NOT ALLOW THE EXCLUSION OR LIMITATION OF INCIDENTAL OR 
CONSEQUENTIAL DAMAGES OR LIMITATION ON HOW LONG AN IMPLIED WARRANTY 
LASTS, SO THE ABOVE LIMITATION OR EXCLUSIONS MAY NOT APPLY.
This warranty gives specific legal rights, and there may be other rights which may vary from state to 
state.
IV. How To Get Warranty Service
You must provide proof of purchase (bearing the date of purchase and Product item serial number) 
in order to receive warranty service and, also, deliver or send the Product item, transportation and 
insurance prepaid, to an authorized warranty service location. Warranty service will be provided by 
Motorola through one of its authorized warranty service locations. If you first contact the company 
which sold you the Product, it can facilitate your obtaining warranty service. 
V. What This Warranty Does Not Cover
A. Defects or damage resulting from use of the Product in other than its normal and customary 
manner.
B. Defects or damage from misuse, accident, water, or neglect.
C. Defects or damage from improper testing, oper ation, maintenance, installation, alteration, 
modification, or adjustment.
D. Breakage or damage to antennas unless caused  directly by defects in material workmanship.
E. A Product subjected to unauthorized Product  modifications, disassemblies or repairs 
(including, without limitation, the addition to the Product of non-Motorola supplied equipment) 
which adversely affect performance of the Product or interfere with Motorola's normal 
warranty inspection and testing of the Product to verify any warranty claim.
F. Product which has had the serial number removed or made illegible.
G. Rechargeable batteries if:
- any of the seals on the battery enclosure of cells are broken or show evidence of 
tampering.
- the damage or defect is caused by charging or using the battery in equipment or service 
other than the Product for which it is specified.
H. Freight costs to the repair depot.
I. A Product which, due to illegal or unauthorize d alteration of the software/firmware in the 
Product, does not function in accordance with MOTOROLA’s published specifications or the 
FCC type acceptance labeling in effect for the Product at the time the Product was initially 
distributed from MOTOROLA.
J. Scratches or other cosmetic damage to Product surfaces that does not affect the operation of 
the Product.
K. Normal and customary wear and tear.
Final Draft

--- Halaman 19 ---
Commercial Warranty xix
VI. Patent And Software Provisions
MOTOROLA will defend, at its own expense, any suit brought against the end user purchaser to the 
extent that it is based on a claim that the Product or parts infringe a United States patent, and 
MOTOROLA will pay those costs and damages finally awarded against the end user purchaser in 
any such suit which are attributable to any such claim, but such defense and payments are 
conditioned on the following:
A. that MOTOROLA will be notified pr omptly in writing by such purchaser of any notice of such 
claim;
B. that MOTOROLA will have sole control of the def ense of such suit and all negotiations for its 
settlement or compromise; and
C. should the Product or parts become, or in MOTOROLA's opinion be likely to become, the 
subject of a claim of infringement of a United States patent, that such purchaser will permit 
MOTOROLA, at its option and expense, either to procure for such purchaser the right to 
continue using the Product or parts or to replace or modify the same so that it becomes 
noninfringing or to grant such purchaser a credit for the Product or parts as depreciated and 
accept its return. The depreciation will be an equal amount per year over the lifetime of the 
Product or parts as established by MOTOROLA.
MOTOROLA will have no liability with respect to any claim of patent infringement which is based 
upon the combination of the Product or parts furnished hereunder with software, apparatus or 
devices not furnished by MOTOROLA, nor will MOTOROLA have any liability for the use of ancillary 
equipment or software not furnished by MOTOROLA which is attached to or used in connection with 
the Product. The foregoing states the entire liability of MOTOROLA with respect to infringement of 
patents by the Product or any parts thereof.
Laws in the United States and other countries preserve for MOTOROLA certain exclusive rights for 
copyrighted MOTOROLA software such as the exclusive rights to reproduce in copies and distribute 
copies of such Motorola software. MOTOROLA software may be used in only the Product in which 
the software was originally embodied and such software in such Product may not be replaced, 
copied, distributed, modified in any way, or used to produce any derivative thereof. No other use 
including, without limitation, alteration, modification, reproduction, distribution, or reverse 
engineering of such MOTOROLA software or exercise of rights in such MOTOROLA software is 
permitted. No license is granted by implication, estoppel or otherwise under MOTOROLA patent 
rights or copyrights.
VII. Governing Law
This Warranty is governed by the laws of the State of Illinois, USA.
Final Draft

--- Halaman 20 ---
xx Battery and Charger Warranty 
Battery and Charger Warranty
Workmanship Warranty
The workmanship warranty guarantees against defects in workmanship under normal use and 
service.
Capacity Warranty
The capacity warranty guarantees 80% of the rated capacity for the warranty duration.
Battery Lilon 2200mAh 12 Months
Chargers 12 Months
Battery Lilon 2200mAh 12 Months
Final Draft

--- Halaman 21 ---
Introduction: Notations Used in This Manual 1-1
Chapter 1 Introduction
1.1 Notations Used in This Manual
Throughout the text in this publication, you will notice the use of note and caution notations. These 
notations are used to emphasize that safety hazards exist, and due care must be taken and 
observed.
1.2 Radio Description
The SL1M portable radios are available in the following frequency ranges and power levels.
These digital radios are among the most sophisticated two-way radios available. They have a robust 
design for radio users who need high performance, quality, and reliability in their daily 
communications. This architecture provides the capability of supporting a multitude of legacy and 
advanced features resulting in a more cost-effective two-way radio communications solution.
NOTE An operational procedure, practice, or condition that is essential to emphasize.
CAUTION indicates a potentially hazardous situation which, if 
not avoided, might result in equipment damage.
WARNING indicates a potentially hazardous situation 
which, if not avoided, could result in death or injury.
Table 1-1.  Radio Frequency Ranges and Power Levels
Frequency Band Bandwidth Power Level
VHF 136 – 174 MHz Analogue: 2 or 1 Watt, Digital: 3 or 1 Watt
UHF 403 – 470 MHz Analogue: 2 or 1 Watt, Digital: 3 or 1 Watt
!
C a u t i o n
Final Draft

--- Halaman 22 ---
1-2 Introduction: Radio Description
1.2.1 Radio Overview
Figure 1-1.  Display Model
• ON/OFF/INFORMATION BUTTON – Long press to turn  the radio on or off. Short press once to 
show the Radio Signal Strength Index (RSSI) and the battery level, and short press twice to 
show the radio name.
• LED INDICATOR – Red, Green and Orange light-e mitting diodes indicate operating status.
• SIDE PROGRAMMABLE BUTTON – Field programmable button using the CPS. 
• CHANNEL SELECTOR SWITCH – Toggle down to increase the channel and toggle up to 
decrease the channel.
• VOLUME BUTTON – To adjust speaker volume, and to select the action list when the side 
programmable button is pressed to call out the action list selections.
• PUSH-TO-TALK (PTT) BUTTON– Press to execute voice operations (e.g. Group call and 
Private Call).
• ANTENNA – Provides the needed RF amplif ication when transmitting or receiving.
• MICROPHONE – Allows voice to be sent when PTT or voice operations are activated.
• ACCESSORY CONNECTOR – Interface point for audi o accessories to be used with the radio. 
• USB – Programs the radio through a computer, and charges the radio through a wall charger or 
a computer.
• SPEAKER – Outputs all tones and audio generated by the radio (e.g. features such as keypad 
tones and voice audio).
• CHARGING CONTACT – Contact point for the stan dard multi-unit and single unit charger.
LED Indicator
Push-to-Talk (PTT) Button
On/Off/Information Button
Side Programmable Button
Antenna
Channel Selector Switch
Volume Up Button
Accessory Connector
Microphone
Micro USB Connector
Volume Down Button
Speaker
Charging Contact
Final Draft

--- Halaman 23 ---
Introduction: Portable Radio Model Numbering Scheme 1-3
1.3 Portable Radio Model Numbering Scheme
Figure 1-2.  Portable Radio Model Numbering Scheme
Model No.Example :  AZ H 8 8 Q C P 9 J A 2 A N
Position           :  1 2 3 4 5 6 7 8 9 10 11 12
Unique Variation
N: Standard Package
Version Letter
Feature Level
2: Non-FM
Primary System Type
A: Conventional
Primary Operation
J: Basic
Channel Spacing
9: Variable/Programmable
Power Level
C: 2W, 3W
88: SL Series
Band
Q: 403 – 470MHz
J:  136 – 174MHz
Physical Packages
P: LED Matrix Display,
No Keypad
C: Plain Model
H: Portable
AZ: APAC Australia
LA: Latin America
AA: North America
MD: EMEA
Final Draft

--- Halaman 24 ---
1-4 Introduction: Model Charts
1.4 Model Charts
1.4.1 VHF (136–174 MHz)  2–3W Model Chart
 SL1M, VHF 136–174 MHz 
Model Description
AZH88JCP9JA2_N 136–174 MHz, 2–3W, LED Matrix Display, Non Keypad 
Item Description
X PMLD4699_ Back Housing Kit Assembly 
X PMLD4697_ Display Front Kit Assembly 
X PMLD4696_S Main Board Assembly Service Kit
X PMAD4144_ VHF stubby antenna (136–144 MHz)
X PMAD4145_ VHF stubby antenna (144–156 MHz)
X PMAD4146_ VHF stubby antenna (156–174 MHz)
X = Item Included
_ = The latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “A.3 Additional Service Kits Information” on page A-2, for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of the radio.
Final Draft

--- Halaman 25 ---
Introduction: Model Charts 1-5
1.4.2 UHF (403–470 MHz) 2–3W Model Chart
SL1M, UHF 403–470 MHz 
Model Description
AZH88QCP9JA2_N 403–438 MHz, 2–3W, LED Matrix Display, Non Keypad 
AZH88QCP9JA2_N 403–470 MHz, 2–3W, LED Matrix Display, Non Keypad
Item Description
X X PMLE5029_ Back Housing Kit Assembly
X X PMLE5027_ Display Front Kit Assembly
X X PMLE5020_S Main Board Assembly Service Kit
X X PMAE4093_ UHF stubby antenna (403–425 MHz)
X X PMAE4094_ UHF stubby antenna (420–445 MHz)
X X PMAE4095_ UHF stubby antenna (435–470 MHz)
X = Item Included
_ = The latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “A.3 Additional Service Kits Information” on page A-2, for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of the radio.
Note: 403–438 MHz is only available in Indonesia.
Final Draft

--- Halaman 26 ---
1-6 Introduction: Specifications
1.5 Specifications
General SL1M Display
Channel Capacity 256
Frequency VHF : 136–174 MHz
UHF: 403–470 MHz
Dimensions (HxWxT) 
with Lilon battery
125.7 x 55.0 x 22.0 mm
Weight
with Lilon battery
163.4g
Power Supply 3.7 V nominal 
FCC Description VHF: AZ489FT3835
UHF: AZ489FT4922
IC Description VHF: 109U-89FT3835
UHF: 109U-89FT4922
Average battery life at 5/5/90 duty cycle with battery saver enabled 
Lilon battery VHF: Analogue: 12.3 hours, Digital: 14.5 hours
UHF: Analogue: 12.3 hours, Digital: 14.5 hours
Final Draft

--- Halaman 27 ---
Introduction: Specifications 1-7
 Receiver SL1M
Frequencies VHF: 136–174 MHz
UHF: 403–470 MHz
Channel Spacing 12.5 kHz/25kHz
Frequency Stability (-30°C to +60°C, 
+25°C Ref) 
+/-1.5 ppm
Analog Sensitivity (12 dB SINAD) 0.3 µV 
0.22 µV (typical)
Digital Sensitivity (5% BER) 0.25 µV
0.19 µV (typical)
Intermodulation (TIA603D) 70 dB 
Adjacent Channel Selectivity 
(TIA603D)
45 dB @ 12.5 kHz, 70 dB @ 25 kHz
Spurious Rejection (TIA603D) 70 dB 
Rated Audio 0.5 W (internal)
Audio Distortion @ Rated Audio 5% (3% typical) 
Hum and Noise -40 dB @ 12.5 kHz
-45 dB @ 25 kHz
Audio Response TIA603D
Conducted Spurious Emission -57 dBm 
Speaker Impedance 4 Ohms (internal)
Voltage @ Rated Audio 1.414 V (internal)
Final Draft

--- Halaman 28 ---
1-8 Introduction: Specifications
Transmitter SL1M
Frequencies VHF: 136–174 MHz
UHF: 403–470 MHz 
Channel Spacing 12.5 kHz/25 kHz
Frequency Stability (-30°C to +60°C) +/-1.5 ppm 
Power Output (Low Power)  1W
Power Output (High Power) Analog: 2W
Digital: 3W
Modulation Limiting +/-2.5 kHz @ 12.5 kHz
+/-5.0 kHz @ 25 kHz
FM Hum and Noise -40 dB @ 12.5 kHz
-45 dB @ 25 kHz
Conducted / Radiated Emission -36 dBm < 1 GHz
-30 dBm > 1 GHz 
Adjacent Channel Power 60 dB @ 12.5 kHz
70 dB @ 25 kHz
Audio Response TIA603D
Audio Distortion 3% (typical)
4FSK Digital Modulation 12.5 kHz Data: 7K60F1D & 7K60FXD
12.5 kHz Voice: 7K60F1E & 7K60FXE
Combination of 12.5 kHz Data & Voice: 7K60F1W 
Digital Vocoder Type AMBE+2 ™
Digital Protocol ETSI-TS102361-1
ETSI-TS102361-2
ETSI-TS102361-3
Final Draft

--- Halaman 29 ---
Introduction: Specifications 1-9
UHF Self-Quieter Frequencies
403.20 MHz ± 15 kHz
408.00 MHz ± 10 kHz
412.80 MHz ± 10 kHz
417.60 MHz ± 10 kHz
422.40 MHz ± 15 kHz
427.20 MHz ± 10 kHz
432.00 MHz ± 20 kHz
436.80 MHz ± 10 kHz
441.60 MHz ± 20 kHz
446.40 MHz ± 10 kHz
451.20 MHz ± 20 kHz
456.00 MHz ± 10 kHz
460.80 MHz ± 20 kHz
465.60 MHz ± 10 kHz
VHF Self-Quieter Frequencies
139.20 MHz ± 10 kHz
144.00 MHz ± 10 kHz
148.80 MHz ± 10 kHz
153.60 MHz ± 10 kHz
158.40 MHz ± 10 kHz
163.20 MHz ± 10 kHz
168.00 MHz ± 15 kHz
172.80 MHz ± 10 kHz
Final Draft

--- Halaman 30 ---
1-10 Introduction: Specifications
Applicable 
MIL-STD
810C 810D 810E 810F 810G
Methods Procedures Methods Procedures Methods Procedures Methods Procedures Methods Procedures
Low 
Pressure 
500.1 I 500.2 II 500.3 II 500.4 I/II 500.5 I/II
High 
Temperature 
501.1 I,II 501.2 I/AI,II/AI 501.3 I/A1, II/A1 501.4 I/HOT, II/
HOT
501.5 I/A1, II/A2
Low 
Temperature 
502.1 I 502.2 I/C3,II/C1 502.3 I/C3,II/C1 502.4 I/C3, II/C1 502.5 I/C3, II/C1
Temperature 
Shock
503.1 I 503.2 I/AI,C3 503.3 I/A1, C3 503.4 I 503.5 I/C
Solar 
Radiation 
505.1 II 505.2 I 505.3 I 505.4 I 505.5 I/A1
Rain 506.1 I,II 506.2 I,II 506.3 I, II 506.4 I, III 506.5 I, III
Humidity 507.1 II 507.2 II 507.3 II 507.4 - 507.5 II/Agg
Salt fog 509.1 I 509.2 I 509.3 I 509.4 - 509.5 -
Dust 510.1 I 510.2 I 510.3 I 510.4 I 510.5 I
Vibration 514.2 VIII/F,W 514.3 I/I0,II /3 514.4 I/10, II/3 514.5 I/24 514.6 I/24
Shock 516.2 I,III,V 516.3 I,IV,VI 516.4 I, IV, VI 516.5 I, IV, VI 516.6 I, IV, VI
 Environmental Specifications
*Operating Temperature -30 °C to +60 °C 
Storage Temperature -40 °C to +85 °C 
Thermal Shock Per MIL-STD
Humidity Per MIL-STD
ESD IEC 61000-4-2 Level 3
Dust and Water Intrusion IEC60529 - IP54
Packaging test Per MIL-STD
* Operating temperature specification for a Lilon battery is -10 °C to +60 °C.
Final Draft
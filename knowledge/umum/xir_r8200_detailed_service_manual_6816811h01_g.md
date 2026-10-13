--- Halaman 1 ---
PROFESSIONAL DIGITAL TWO-WAY RADIO SYSTEM
MOTOTRBO™REPEATERDETAILED SERVICEMANUAL
XPR™ 8300 REPEATER
XPR™ 8400 REPEATER


--- Halaman 3 ---
i
Foreword
This manual covers all models of the XPR™ 8300/XPR™ 8400 Repeater, unless otherwise specified. This manual 
provides sufficient information to enable qualified service technicians to troubleshoot and repair the XPR™ 8300/
XPR™ 8400 Repeater to the component level.
For details on radio operation or basic troubleshooting, refer to the applicable manuals available separately.
Product Safety and RF Exposure Compliance
ATTENTION!
Before using this product, XPR™ 8300/XPR™ 8400 Repeater, read the RF Exposure and Safety guide 
that ships with the repeater which contains important operating instructions for safe usage and RF 
energy awareness and control for Compliance with applicable Standards and Regulations.
Computer Software Copyrights
The Motorola products described in this manual may include copyrighted Motorola computer programs stored in 
semiconductor memories or other media. Laws in the United States and other countries preserve for Motorola certain 
exclusive rights for copyrighted computer programs, including, but not limited to, the exclusive right to copy or reproduce 
in any form the copyrighted computer program. Accordingly, any copyrighted Motorola computer programs contained in 
the Motorola products described in this manual may not be copied, reproduced, modified, reverse-engineered, or 
distributed in any manner without the express written permission of Motorola. Furthermore, the purchase of Motorola 
products shall not be deemed to grant either directly or by implication, estoppel, or otherwise, any license under the 
copyrights, patents or patent applications of Motorola, except for the normal non-exclusive license to use that arises by 
operation of law in the sale of a product.
Document Copyrights
No duplication or distribution of this document or any portion thereof shall take place without the express written 
permission of Motorola. No part of this manual may be reproduced, distributed, or transmitted in any form or by any 
means, electronic or mechanical, for any purpose without the express written permission of Motorola.
Disclaimer
The information in this document is carefully examined, and is believed to be entirely reliable. However, no responsibility is 
assumed for inaccuracies. Furthermore, Motorola reserves the right to make changes to any products herein to improve 
readability, function, or design. Motorola does not assume any liability arising out of the applications or use of any product 
or circuit described herein; nor does it cover any license under its patent rights nor the rights of others.
Trademarks
MOTOROLA, MOTO, MOTOROLA SOLUTIONS and the Stylized M logo are trademarks or registered trademarks of 
Motorola Trademark Holdings, LLC and are used under license.  All other trademarks are the property of their respective 
owners.
© 2006–2010, 2014 Motorola Solutions, Inc. All rights reserved.
These servicing instructions are for use by qualified personnel only. To 
reduce the risk of electric shock, do not perform any servicing other than 
that contained in the Operating Instructions unless you are qualified to do 
so. Refer all servicing to qualified service personnel.
!
C a u t i o n

--- Halaman 4 ---
ii
Notes

--- Halaman 5 ---
iii
 
Document History
The following major changes have been implemented in this manual since the previous edition:
Edition Description Date
6816811H01-A Initial edition. May 2007
6816811H01-B Added VHF High Power Band Information June 2007
6816811H01-C Added UHF Low Power and VHF Low Power Band 
Information. Added issue C boards to all bands.
Nov. 2007
6816811H01-D Added UHF2 Band Information. June 2008
6816811H01-E For UHF2 Band: changed four capacitors namely 
C0811, C0812, C0719 and C0746 in Power Amp 
schematic and parts list .
Added section: Summary of Printed Circuit Boards and 
Bands available in manual.
June 2009
6816811H01-F Added R6 Controller. 
Added Repeater Indicator Board PMLN5643_.
Added Connector Board PMLN5644_.
Added a new set of Printed Circuit Boards, Schematics 
and Parts Lists to: VHF (High & Low Power), UHF1 
(High & Low Power), UHF2 (High Power) bands.
Sept. 2010
6816811H01-G Replaced Parts List of UHF1 HP PCB 8486777Z15.
Added 8486777Z15 Printed Circuit Board, Schematics 
and Parts List to UHF2 band.
Feb. 2014

--- Halaman 6 ---
iv
 
Notes

--- Halaman 7 ---
Commercial Warranty v
Commercial Warranty
Limited Warranty
MOTOROLA COMMUNICATION PRODUCTS
I. What This Warranty Covers And For How Long
MOTOROLA INC. (“MOTOROLA”) warrants the MOTOROLA manufactured Communication 
Products listed below (“Product”) against defects in material and workmanship under normal use and 
service for a period of time from the date of purchase as scheduled below:
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
remedy. THIS WARRANTY IS GIVEN IN LIEU OF ALL OTHER EXPRESS WARRANTIES. 
IMPLIED WARRANTIES, INCLUDING WITHOUT LIMITATION, IMPLIED WARRANTIES OF 
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, ARE LIMITED TO THE 
DURATION OF THIS LIMITED WARRANTY. IN NO EVENT SHALL MOTOROLA BE LIABLE FOR 
DAMAGES IN EXCESS OF THE PURCHASE PRICE OF THE PRODUCT, FOR ANY LOSS OF 
USE, LOSS OF TIME, INCONVENIENCE, COMMERCIAL LOSS, LOST PROFITS OR SAVINGS 
OR OTHER INCIDENTAL, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE 
USE OR INABILITY TO USE SUCH PRODUCT, TO THE FULL EXTENT SUCH MAY BE 
DISCLAIMED BY LAW.
Repeater Two (2) Years
Product Accessories One (1) Year

--- Halaman 8 ---
vi Commercial Warranty 
III. State Law Rights
SOME STATES DO NOT ALLOW THE EXCLUSION OR LIMITATION OF INCIDENTAL OR 
CONSEQUENTIAL DAMAGES OR LIMITATION ON HOW LONG AN IMPLIED WARRANTY 
LASTS, SO THE ABOVE LIMITATION OR EXCLUSION MAY NOT APPLY.
This warranty gives specific legal rights, and there may be other rights which may vary from state to 
state.
IV. How To Get Warranty Service
You must provide proof of purchase (bearing the date of purchase and Product item serial number) 
in order to receive warranty service and, also, deliver or send the Product item, transportation and 
insurance prepaid, to an authorized warranty service location. Warranty service will be provided by 
Motorola through one of its authorized warranty service locations. If you first contact the company 
which sold you the Product, it can facilitate your obtaining warranty service. You can also call 
Motorola at 1-888-567-7347 US/Canada.
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
G. Freight costs to the repair depot.
H. A Product which, due to illegal  or unauthorized alteration of the software/firmware in the 
Product, does not function in accordance with MOTOROLA’s published specifications or the 
FCC type acceptance labeling in effect for the Product at the time the Product was initially 
distributed from MOTOROLA.
I. Scratches or other cosmetic damage to Product surfaces that does not affect the operation of 
the Product.
J. Normal and customary wear and tear.

--- Halaman 9 ---
Commercial Warranty vii
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

--- Halaman 10 ---
Notes
viii Commercial Warranty

--- Halaman 11 ---
February, 2014
XPR 8300/XPR 8400
MOTOTRBO Repeater
Detailed Service Manual
Contents
Chapter 1 Service Maintainability
Chapter 2 Repeater Indicator Board Service Information
Chapter 3 Connector Boar d Service Information
Chapter 4 Controller Service Information
Chapter 5 VHF Low Power Service Information
Chapter 6 VHF High Powe r Service Information
Chapter 7 UHF1 Low Power Service Information
Chapter 8 UHF1 High Power Service Information
Chapter 9 UHF2 High Power Service Information
Appendix A Replacement Parts Ordering
Appendix B Motorola Service Centers
Glossary

--- Halaman 12 ---
x
Notes

--- Halaman 13 ---
xi
 
Summary of Printed Circuit Boards and Bands available:
Table below lists all the bands available in this manual and the revision of the Printed Circuit Boards used. For 
details, please refer to the respective chapters.
Chapter Description PC Board Part Number Board Revision
2 Repeater Indicator Board (PMLN4814_) 8415470H02 B
2 Repeater Indicator Board (PMLN5269_) 8415470H04 D
2 Repeater Indicator Board (PMLN5643_) 84012135001 A
3 Connector Board (PMLN4815_) 8415472H01 A
3 Connector Board (PMLN5270_) 8415472H05 E
3 Connector Board (PMLN5644_) 8402133002 B
5 VHF Low Power 136–174 MHz, 1–25 W 8471495L01
8471495L03
8471495L04
A
C
D
6 VHF High Power 136–174 MHz, 25–45 W 8478023A12
8478023A16
8478023A17
P8
C
D
7 UHF1 Low Power 403–470 MHz, 1–25 W 8471165L03
8471165L05
8471165L06
A
C
D
8 UHF1 High Power 403–470 MHz, 25–40 W 8486777Z12
8486777Z14
8486777Z15
A
C
D
9 UHF2 High Power 450–512 MHz, 1–40 W 8471696M01
8471696M02
8486777Z15
A
D
D

--- Halaman 14 ---
xii
 
Notes

--- Halaman 15 ---
 XPR 8300/XPR8400
MOTOTRBO Repeater
Chapter 1
Service Maintainability
M
Issue: February, 2014

--- Halaman 16 ---
Computer Software Copyrights
The Motorola products described in this manual may include copyrighted Motorola computer programs stored 
in semiconductor memories or other media. Laws in the United States and other countries preserve for 
Motorola certain exclusive rights for copyrighted computer programs, including, but not limited to, the 
exclusive right to copy or reproduce in any form the copyrighted computer program. Accordingly, any 
copyrighted Motorola computer programs contained in the Motorola products described in this manual may 
not be copied, reproduced, modified, reverse-engineered, or distributed in any manner without the express 
written permission of Motorola. Furthermore, the purchase of Motorola products shall not be deemed to grant 
either directly or by implication, estoppel, or otherwise, any license under the copyrights, patents or patent 
applications of Motorola, except for the normal non-exclusive license to use that arises by operation of law in 
the sale of a product.

--- Halaman 17 ---
i
Chapter 1 – Service Maintainability
Table of Contents
Section 1 Introduction
1.0 Notations Used in This Manual ... .........................................................................1-1
2.0 Repeater Description ...... .....................................................................................1-1
Section 2 Maintenance
1.0 Introduction ................ ..........................................................................................2-1
2.0 Preventive Maintenance .......... ............................................................................2-1
2.1 Inspection ................ .......................................................................................2-1
2.2 Cleaning Procedures............... .......................................................................2-1
3.0 Safe Handling of CMOS  and LDMOS Devices....................................................2-2
4.0 Repair Procedures and Techniques  – General....................................................2-3
Section 3 Test Equipment and Service Aids
1.0 Recommended Test Equipment ... .......................................................................3-1
2.0 Service Aids............. ............................................................................................3-2
3.0 Programming Cables ...... .....................................................................................3-3

--- Halaman 18 ---
ii
Notes

--- Halaman 19 ---
1-1
Section 1
INTRODUCTION
1.0 Notations Used in This Manual
Throughout the text in this publication, you will notice the use of note and caution notations. These 
notations are used to emphasize that safety hazards exist, and due care must be taken and 
observed.
NOTE: An operational procedure, practice, or condition that is essential to emphasize.
2.0 Repeater Description
The XPR 8300/XPR 8400 repeater is available in the following frequency ranges and power levels.
This repeater is among the most sophisticated two-way repeaters available. It has a robust design 
for users who need high performance, quality, and reliability in their daily communications. This 
architecture provides the capability of supporting a multitude of legacy and advanced features 
resulting in a more cost-effective two-way repeater communications solution. 
CAUTION indicates a potentially hazardous situation which, if 
not avoided, might result in equipment damage.
Table 1-1  Frequency Ranges and Power Levels
Freq. Band Bandwidth Power Level
VHF 136–174 MHz 1–25 Watts
25–45 Watts
350 350–400 MHz 25–40 Watts
UHF B1 403–470 MHz 1–25 Watts
25–40 Watts
UHF B2 450–512 MHz 1–40 Watts
!
C a u t i o n

--- Halaman 20 ---
1-2 Repeater Description
Notes

--- Halaman 21 ---
2-1
Section 2
MAINTENANCE
1.0 Introduction
This chapter provides details about the following:
• Preventive maintenance (inspection and cleaning).
• Safe handling of CMOS and LDMOS devices.
• Repair procedures and techniques.
2.0 Preventive Maintenance
Periodic visual inspection and cleaning is recommended.
2.1 Inspection
Check that the external surfaces of the repeater are clean, and that all external controls and 
switches are functional. It is not recommended to inspect the interior electronic circuitry.
2.2 Cleaning Procedures
The following procedures describe the recommended cleaning agents and the methods to be used 
when cleaning the external and internal surfaces of the repeater. External surfaces include the top 
cover and repeater enclosure.
Periodically clean smudges and grime from exterior enclosure. Use a soft, non-abrasive cloth 
moistened in a mild soap and water solution Rinse the surface using a second cloth moistened in 
clean water, and clean any dirt or debris from the fan grill and louvers on the front side.
NOTE: Internal surfaces should be cleaned only when the repeater is disassembled for service or 
repair.
The only recommended agent for cleaning the external repeater surfaces is a 0.5% solution of a mild 
dishwashing detergent in water. The only factory recommended liquid for cleaning the printed circuit 
boards and their components is isopropyl alcohol (100% by volume).
Cleaning Internal Circuit Boards and Components
Isopropyl alcohol (100%) may be applied with a stiff, non-metallic, short-bristled brush to dislodge 
embedded or caked materials located in hard-to-reach areas. The brush stroke should direct the 
dislodged material out and away from the inside of the repeater. Make sure that controls or tunable 
components are not soaked with alcohol. Do not use high-pressure air to hasten the drying process 
since this could cause the liquid to collect in unwanted places. Once the cleaning process is 
complete, use a soft, absorbent, lintless cloth to dry the area. Do not brush or apply any isopropyl 
alcohol to the top cover and repeater enclosure.
NOTE: Always use a fresh supply of alcohol and a clean container to prevent contamination by 
dissolved material (from previous usage).

--- Halaman 22 ---
2-2 Safe Handling of CMOS and LDMOS Devices
3.0 Safe Handling of CM OS and LDMOS Devices
Complementary Metal Oxide Semiconductor (CMOS) and Laterally Diffused Metal Oxide 
Semiconductor (LDMOS) devices are used in this family of repeaters, and are susceptible to 
damage by electrostatic or high voltage charges. Damage can be latent, resulting in failures 
occurring weeks or months later. Therefore, special precautions must be taken to prevent device 
damage during disassembly, troubleshooting, and repair. 
Handling precautions are mandatory for CMOS/LDMOS circuits and are especially important in low 
humidity conditions. 
DO NOT attempt to disassemble the repeater without first referring to the following CAUTION 
statement.
This repeater contains static-sensitive devices. Do not open the repeater unless you 
are properly grounded. Take the following precautions when working on this unit:
• Store and transport all CMOS/L DMOS devices in conductive 
material so that all exposed leads are shorted together. Do not insert 
CMOS/LDMOS devices into conventional plastic “snow” trays used 
for storage and transportation of other semiconductor devices.
• Ground the working surface of the service bench to protect the 
CMOS/LDMOS device. We recommend using a wrist strap, two 
ground cords, a table mat, a floor mat, ESD shoes, and an ESD 
chair.
• Wear a conductive wrist strap in series with a 100k resistor to 
ground. (Replacement wrist straps that connect to the bench top 
covering are Motorola part number 4280385A59).
• Do not wear nylon clothing while handling CMOS/LDMOS devices.
• Do not insert or remove CMOS/L DMOS devices with power applied. 
Check all power supplies used for testing CMOS/LDMOS devices to 
be certain that there are no voltage transients present.
• When straightening CMOS/LDMOS pins, provide ground straps for 
the apparatus used.
• When soldering, use a grounded soldering iron.
• If at all possible, handle CMOS/LDMOS devices by the package and 
not by the leads. Prior to touching the unit, touch an electrical 
ground to remove any static charge that you may have 
accumulated. The package and substrate may be electrically 
common. If so, the reaction of a discharge to the case would cause 
the same damage as touching the leads.
!
C a u t i o n

--- Halaman 23 ---
Repair Procedures and Techniques – General 2-3
4.0 Repair Procedures an d Techniques – General
Any rework or repair on Environmentally Preferred Products must be done using the appropriate 
lead-free solder wire and lead-free solder paste as stated in the following table:
Parts Replacement and Substitution
When damaged parts are replaced, identical parts should be used. If the identical replacement part 
is not locally available, check the parts list for the proper Motorola part number and order the part. 
Refer to Appendix A of this manual.
Rigid Circuit Boards
The repeater uses bonded, multi-layer, printed circuit boards. Since the inner layers are not 
accessible, some special considerations are required when soldering and unsoldering components. 
The printed through holes may interconnect multiple layers of the printed circuit. Therefore, exercise 
care to avoid pulling the plated circuit out of the hole.
When soldering near a connector: 
• Avoid accidentally getting solder in the connector. 
• Be careful not to form solder bridges between the connector pins. 
• Examine your work closely for shorts due to solder bridges.
For soldering components with Hot-Air or infra red solder systems, please check your user guide of 
the solder system to get information on solder temperature and time for the different housings of the 
integrated circuits and other components.
NOTE Environmentally Prefer red Products (EPP) (refer to t he marking on the printed circuit
boards – examples shown below) were developed and assembled using environmentally
preferred components and solder assembly techniques to comply with the European
Union’s Restriction of Hazardous Substances  (ROHS 2) Directive 2011/65/EU and
Waste Electrical and Electronic Equipment (WEEE) Directive 2012/19/EU. To 
maintain product compliance and reliability, us e only the Motorola specified parts in this
manual.
Table 2-1  Lead Free Solder Wire Part Number List
Motorola 
Part Number Alloy Flux Type Flux Content by Weight Melting Point Supplier Part number Diameter Weight
1088929Y01 95.5Sn/3.8Ag/0.7Cu RMA Version 2.7–3.2% 217°C 52171 0.015” 1lb spool
Table 2-2  Lead Free Solder Paste Part Number List
Motorola Part 
Number
Manufacturer Part 
Number Viscosity Type Composition & Percent Metal Liquid Temperature
1085674C03 NC-SMQ230 900–1000KCPs 
Brookfield (5rpm)
Type 3 
(-325/+500)
(95.5%Sn–3.8%Ag–0.7%Cu) 
89.3%
217°C

--- Halaman 24 ---
2-4 Repair Procedures and Techniques – General
Notes

--- Halaman 25 ---
3-1
Section 3
TEST EQUIPMENT AND SERVICE AIDS
1.0 Recommended Test Equipment
The list of equipment contained in Table 3-1 includes most of the standard test equipment required 
for servicing Motorola repeaters.
Table 3-1  Recommended Test Equipment
Equipment Characteristic Example Application
Service Monitor Can be used as a 
substitute for items 
marked with an asterisk 
(*)
Aeroflex 3920, or equivalent Frequency/deviation meter and 
signal generator for wide-range 
troubleshooting and alignment
Digital RMS 
Multimeter*
100 µV to 300 V
5 Hz to 1 MHz
10 Mega Ohm 
Impedance
Fluke 179 or equivalent 
(www.fluke.com)
AC/DC voltage and current 
measurements. Audio voltage 
measurements.
RF Signal 
Generator*
100 MHz to 1 GHz
-130 dBM to +10 dBM
FM Modulation 0 kHz to 
10 kHz
Agilent N5181 
(www.agilent.com) or equivalent
Receiver measurements
Oscilloscope* 2 Channels
50 MHz Bandwidth
5 mV/div to 20 V/div
 Tektronix TDS1001b 
(www.tektronix.com) or 
equivalent
Waveform measurements
Power Meter and 
Sensor*
5% Accuracy
100 MHz to 500 MHz
50 Watts
Bird 43 Thruline Watt Meter
(www.bird-electronic.com) or 
equivalent
Transmitter power output 
measurements
RF Millivolt Meter 100 mV to 3 V RF
10 kHz to 1 GHz
Boonton 92EA 
(www.boonton.com) or 
equivalent
RF level measurements

--- Halaman 26 ---
3-2 Service Aids
2.0 Service Aids
Table 3-2 lists the service aids recommended for working on the repeater. While all of these items 
are available from Motorola, most are standard workshop equipment items, and any equivalent item 
capable of the same performance may be substituted for the item listed.
Table 3-2  Service Aids
Motorola
Part Number Description Application
RLN4460_ Test Box Enables connection to audio/accessory jack. Allows 
switching for radio testing.
RVN5115_ Customer Programming Soft-
ware on CD-ROM
Allows servicer to program repeater parameters, tune 
and troubleshoot repeaters.
PMKN4010_ Mobile & Repeater Rear 
Programming Cable
Connects the radio’s rear connector to a USB port for 
radio programming and data applications.
PMKN4016_ Mobile & Repeater Rear 
Accessory Programming and 
Test Cable
Connects the radio’s rear connector to a USB port for 
radio programming, data applications, testing and 
alignment.
PMKN4018_ Mobile & Repeater Rear 
Accessory Connector Universal 
Cable
Connects the radio’s rear connector to accessory 
devices such as desk sets. Cable contains all 26 wires 
and is unterminated at the user end.

--- Halaman 27 ---
Programming Cables 3-3
3.0 Programming Cables
Figure 3-1  Mobile & Repeater Rear Programming Cable PMKN4010_
Figure 3-2  Mobile & Repeater Rear Accessory Programming and Test Cable PMKN4016_
TABLE 2-3: WIRE DIAGRAM
26 PIN 
ACCESSORY PORT CONNECTOR USB DB25P
PIN 
NO. DESCRIPTION
3 VCC (5v) 1
2D A T A  - 2
1D A T A  + 3
4
GND 4
DRAIN WIRE AND BRAID SHELL
7SPEAKER -9
71EXT MIC11
17 DIGI IN  I (EXT PTT) 20
61GND61
1SPEAKER +01
DB 25 CONNECTOR
1
1
14 25
13
14
915±15
CABLE
1455±24
CABLE
TO MOBILE RADIO
ACCESSORY
CONNECTOR
VIEWED FROM 
FRONT (PIN END)
OF CONNECTOR
1
22 6
25
13
14 25
USB CONNECTOR

--- Halaman 28 ---
3-4 Programming Cables
Notes

--- Halaman 29 ---
 XPR 8300/XPR 8400
MOTOTRBO Repeater
Chapter 2
Repeater Indicator Board
Service Information
M
Issue: February, 2014

--- Halaman 30 ---
Computer Software Copyrights
The Motorola products described in this manual may include copyrighted Motorola computer programs stored 
in semiconductor memories or other media. Laws in the United States and other countries preserve for 
Motorola certain exclusive rights for copyrighted computer programs, but not limited to, the exclusive right to 
copy or reproduce in any form, the copyrighted computer program. Accordingly, any copyrighted Motorola 
computer programs contained in the Motorola products described in this manual may not be copied, 
reproduced, modified, reverse-engineered, or distributed in any manner without the express written 
permission of Motorola. Furthermore, the purchase of Motorola products shall not be deemed to grant either 
directly or by implication, estoppel or otherwise, any license under the copyrights, patents or patent 
applications of Motorola, except for the normal non-exclusive license to use that arises by operation of law in 
the sale of a product.
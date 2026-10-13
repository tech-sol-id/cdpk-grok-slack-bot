--- Halaman 1 ---
PROFESSIONAL DIGITAL TWO-WAY RADIO
MOTOTRBO™ MOBILE
BASIC SERVICE MANUAL
XiR™ M8620 NUMERIC DISPLAY MOBILE
XiR™ M8628 NUMERIC DISPLAY MOBILE (WITH BLUETOOTH & GPS)
XiR™ M8660 COLOUR DISPLAY MOBILE
XiR™ M8668 COLOUR DISPLAY MOBILE (WITH BLUETOOTH & GPS)
CM7668 COLOUR DISPLAY MOBILE (WITH BLUETOOTH, GPS & NOB)


--- Halaman 3 ---
i
Foreword
This manual covers all CM7668/XiR™ M8600 Series Mobiles, unless otherwise specified. It includes all the information 
necessary to maintain peak product performance and maximum working time, using levels 1 and 2 maintenance 
procedures. This level of service goes down to the board replacement level and is typical of some local service centers, 
Motorola Authorized Dealers, self-maintained customers, and distributors.
Product Safety and RF Exposure Compliance
ATTENTION!
Before using the mobile two-way product, CM7668/XiR™ M8600 Series Mobiles, read the RF Exposure 
and Safety guide that ships with the radio which contains important operating instructions for safe 
usage and RF energy awareness and control for Compliance with applicable Standards and 
Regulations.
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
© 2011 and 2018 Motorola Solutions, Inc. All rights reserved.
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
The following major changes have been implemented in this manual since the previous edition.
Edition Description Date
68012003051-A Initial Release. Dec. 2011
68012003051-B Added UHF2 Band Information.
Updated Table 3-6 Transmitter Performance 
Checks, Table 5-4 Colour Display Control Head 
Exploded View Parts List and Table 5-5 Numeric 
Display Control Head Exploded View Parts List.
Dec. 2012
68012003051-C Added 350-400 MHz High Power and Low Power 
Band Information. 
Added CM7668 models to UHF1 High Power 
band. Updated model charts with Optional Item, 
Service Kit, Generic Option Board.
Aug. 2014
68012003051-DA Added PMUD3363_S* Service Kit, 350 MHz
Band, LP–HP , De-Moto to 350 MHz Low Power
(350–400 MHz) Model Chart.
Added PMUD3363AHHAFAS to Appendix Sec-
tion A.3.4 350 MHz Low Power Super Tanapa.
Nov. 2015
68012003051-DB  Amended Numeric Display Control Head part 
number from PMLN5677_ to PMLN7500_.
Amended Display Control Head part number from 
PMLN5678_ to PMLN7501_.
Amended description for PMUD3363_ for Sales 
Model No. AZM28PNN9KA2AN in Table 1.8 350 
MHz Low Power (350–400 MHz) Model Chart and 
Table A.3.4 350 MHz Low Power Super Tanapa
Amended Display Control Head part number from 
PMLN5678_ to PMLN7501_.
Amended description for PMUE5132_ for Sales 
Model No. AZM28QNN9KA2AN in Table 1.10 
UHF1 Low Power (403–470 MHz) Model Chart 
and Table A.3.6 UHF1 Low Power Super Tanapa.
Added PMUD3363AAHAFA in Table A.3.4 for 
Sales Model No. AZM28PNN9KA2AN.
June 2016
68012003051-DC Updated Control H ead Flex Cable part number 
from 30012045002 to PF001884A01.
Sept. 2018

--- Halaman 6 ---
iv
Notes

--- Halaman 7 ---
Table of Contents v
Table of Contents
Foreword..........................................................................................................i
Product Safety and RF Exposure Compliance...................... .......................................................................i
Computer Software Copyrights ....................................................................................................................i
Document Copyrights....... ............................................................................................................................i
Disclaimer.....................................................................................................................................................i
Trademarks ..................................................................................................................................................i
Document History ........................................................................................ iii
Warranty and Service Support.....................................................................xi
Warranty Period and Return Instructions ...................................................................................................xi
After Warranty Period .....................................................................................................................xi
Chapter 1 Introductio n ......................................................................... 1-1
1.1 Notations Used in This Manual............................... ..................................................................... 1-1
1.2 Radio Description ........................................... ............................................................................. 1-1
1.3 Control Head Description.................................... ......................................................................... 1-2
1.3.1 Control Head Controls (Colour Display Model) .............. ................................................. 1-2
1.3.2 Control Head Controls (Num eric Display Model)............................................................. 1-3
1.4 MOTOTRBO Mobile Radio Model  Numbering Scheme............................................................... 1-4
1.5 VHF High Power (136–174 MHz ) Model Chart ........................................................................... 1-5
1.6 VHF Low Power (136–174 MHz) Model Chart  ................... ....................................................... 1-6
1.7 350 MHz High Power (350–40 0 MHz) Model Chart .................................................................... 1-7
1.8 350 MHz Low Power (350–400 MHz) Model Chart ................ .................................................... 1-8
1.9 UHF1 High Power (403–470 MHz) Model Chart .................. ...................................................... 1-9
1.10 UHF1 Low Power (403–470 M Hz) Model Chart   ................ ..................................................... 1-10
1.11 UHF2 (450–527 MHz) Model Chart ............................ .............................................................. 1-11
1.12 Specifications   .......................................... ................................................................................ 1-12
Chapter 2 Test Equipment a nd Service Aids ..................................... 2-1
2.1 Recommended Test Equipment .................................. ................................................................2 - 1
2.2 Service Aids................................................ ................................................................................. 2-2
2.3 Programming Cables .......................................... ......................................................................... 2-3
Chapter 3 Transceiver Per formance Testing ..................................... 3-1
3.1 General ..................................................... ................................................................................... 3-1
3.2 Setup ....................................................... .................................................................................... 3-1
3.3 Colour Display Model Test Mode.............................. ................................................................... 3-2
3.3.1 Entering Display Radio Test Mode.......................... ........................................................ 3-2
3.3.2 RF Test Mode.............................................. .................................................................... 3-2
3.3.3 Colour Display Test Mode .................................. ............................................................. 3-3
3.3.4 LED Test Mode............................................. ................................................................... 3-3

--- Halaman 8 ---
vi Table of Contents
3.3.5 Backlight Test Mode ....................................... ................................................................. 3-3
3.3.6 Speaker Tone Test Mode .................................... ............................................................ 3-3
3.3.7 Earpiece Tone Test Mode ................................... ............................................................ 3-3
3.3.8 Audio Loopback Test Mode.................................. ........................................................... 3-4
3.3.9 Audio Loopback Earpiece Test Mode......................... ..................................................... 3-4
3.3.10 Button/Knob/PTT Test Mode ........................................................................................... 3-4
3.4 Numeric Display Model Tes t Mode .............................................................................................. 3-4
3.4.1 Entering Display Radio Test Mode .......................... ........................................................ 3-4
3.4.2 RF Test Mode.............................................. .................................................................... 3-4
3.4.3 Display Test Mode......................................... .................................................................. 3-5
3.4.4 LED Test Mode............................................. ................................................................... 3-5
3.4.5 Speaker Tone Test Mode .................................... ............................................................ 3-5
3.4.6 Earpiece Tone Test Mode ................................... ............................................................ 3-5
3.4.7 Audio Loopback Test Mode.................................. ........................................................... 3-5
3.4.8 Audio Loopback Earpiece Test Mode......................... ..................................................... 3-5
3.4.9 Button/Knob/PTT Test Mode ................................. .......................................................... 3-5
Chapter 4 Radio Programming  and Tuning ....................................... 4-1
4.1 Introduction ................................................ .................................................................................. 4-1
4.2 Customer Programming Software Setup ......................... ............................................................ 4-1
4.3 AirTracer Application Tool.................................. .......................................................................... 4-2
4.4 Radio Tuning Setup .......................................... ........................................................................... 4-3
Chapter 5 Disassembl y/Reassembly Procedures ............................. 5-1
5.1 Introduction ................................................ .................................................................................. 5-1
5.2 Preventive Maintenance ...................................... ........................................................................ 5-1
5.2.1 Inspection ................................................ ........................................................................ 5-1
5.2.2 Cleaning Procedures ....................................... ................................................................5 - 1
5.3 Safe Handling of CMOS and LDMOS Devices ..................... ....................................................... 5-2
5.4 Repair Procedures and Techniques – General............................................................................ 5-4
5.5 Disassembling and Reassemblin g the Radio – General.............................................................. 5-5
5.6 Radio Disassembly – Detailed ................................ ..................................................................... 5-5
5.6.1 Control Head Removal ...................................... .............................................................. 5-5
5.6.2 Top Cover Removal......................................... ................................................................5 - 6
5.6.3 Transceiver Board Removal ................................. ........................................................... 5-7
5.6.4 GPS/GNSS Antenna C onnector Removal (For GPS/GNSS Models Only) ................... 5-12
5.6.5 Option Board Removal (For  Option Board Models Only) .............................................. 5-14
5.6.6 Disassembly of Colour Display Control Head................ ................................................ 5-15
5.6.7 Disassembly of Numeric Dis play Control Head ............................................................. 5-20
5.7 Radio Reassembly – Deta iled.................................................................................................... 5-23
5.7.1 Colour Display Control Head ............................... .......................................................... 5-23
5.7.2 Numeric Display Control Head .............................. ........................................................ 5-28
5.7.3 Radio Assembly............................................ ................................................................. 5-33
5.7.4 Thermal Pad Replacement Procedure ......................... ................................................. 5-34
5.7.5 Transceiver Board Rea ssembly..................................................................................... 5-36
5.7.6 GPS/GNSS Plug or GPS/GNSS An tenna Connector Reassembly.... ........................... 5-44
5.7.7 Option Board Reassembly (Fo r Option Board Models Only)......................................... 5-49
5.7.8 Assemble Control Head to Radio Assembly................... ............................................... 5-51
5.8 Exploded Mechanical Views and Parts Lists ................... .......................................................... 5-53
5.8.1 Radio Assembly Exploded Vi ew and Parts List .............. .............................................. 5-53
5.8.2 Control Head Exploded Views and Parts Lists ............... ............................................... 5-55

--- Halaman 9 ---
Table of Contents vii
5.9 Torque Chart................................................ .............................................................................. 5-57
Chapter 6 Basic Troubles hooting ....................................................... 6-1
6.1 Introduction ................................................ .................................................................................. 6-1
6.1.1 High Power RF Precaution.................................. ............................................................ 6-1
6.2 Replacement Service Kit Procedures .......................... ................................................................6 - 1
6.3 Power-Up Error Codes ........................................ ........................................................................ 6-2
Chapter 7 Accessories ......................................................................... 7-1
7.1 Introduction ................................................ .................................................................................. 7-1
7.1.1 Audio ..................................................... .......................................................................... 7-1
7.1.2 Speakers .................................................. ....................................................................... 7-1
7.1.3 Desktop Accessories ....................................... ................................................................7 - 1
7.1.4 Mounting Kits............................................. ...................................................................... 7-2
7.1.5 Cables .................................................... ......................................................................... 7-2
7.1.6 Antennas .................................................. ....................................................................... 7-2
7.1.7 Bluetooth ................................................. ........................................................................ 7-4
7.1.8 Miscellaneous Accessories ................................. ............................................................ 7-5
Appendix A Replacement Parts & Kits ..................................................A-1
A.1 Level 1 and 2 Maintenance................................... .......................................................................A-1
A.1.1 Replacement Parts Ordering................................ ...........................................................A-1
A.2 Level 3 Maintenance......................................... ...........................................................................A-1
A.3 Additional Service Kit Information.......................... ......................................................................A-2
A.3.1 VHF High Power Super Tanapa............................... .......................................................A-2
A.3.2 VHF Low Power Super Tanapa................................ .......................................................A-2
A.3.3 350 MHz High Power Super Tanapa........................... ....................................................A-3
A.3.4 350 MHz Low Power Super  Tanapa................................................................................A-3
A.3.5 UHF1 High Power Super Tanapa.............................. ......................................................A-4
A.3.6 UHF1 Low Power Super Tanapa............................... ......................................................A-4
A.3.7 UHF2 Super Tanapa ........................................ ..............................................................A -5
Glossary.........................................................................................Glossary-1

--- Halaman 10 ---
viii List of Figures
List of Figures
Figure 1-1 Radio Control Head ( Colour Display Model) ........................................................................ 1-2
Figure 1-2 Radio Control Head ( Numeric Display Model) ..................................................................... 1-3
Figure 1-3 Mobile Radi o Model Numbering Scheme............................................................................. 1-4
Figure 2-1 Mobile Front Progra mming Cable HKN6184_...................................................................... 2-3
Figure 2-2 Mobile & Repeater Rear  Programming Cable PMKN4010_ ................................................ 2-3
Figure 2-3 Mobile & Repeater Rear  Accessory Programming and Test Cable PMKN4016_ ................ 2-3
Figure 4-1 Customer Programming Software Setup from Front Connec tor .......................................... 4-1
Figure 4-2 Customer Programming Software Setup from Rear Accesso ry Connector.......................... 4-2
Figure 4-3 Customer Programming Software Setup with Test Box Con nection .................................... 4-2
Figure 4-4 Radio Tuning Equipment Setup ......................... .................................................................. 4-3
Figure 5-1 Typical Control Head Removal......................... ....................................................................5-5
Figure 5-2 Flexible Connection Removal .......................... .................................................................... 5-6
Figure 5-3 Top Cover Removal ................................... .......................................................................... 5-6
Figure 5-4 Acoustic Plug Remo val ........................................................................................................ 5-7
Figure 5-5 Die Cast Main Shield Removal ......................... ................................................................... 5-8
Figure 5-6 PA Screw Removal..................................... .......................................................................... 5-9
Figure 5-7 Accessory Connector Removal.......................... .................................................................. 5-9
Figure 5-8 DC Connector Retention Clip Removal.................. ............................................................ 5-10
Figure 5-9 RF Connector Nut Removal ............................. .................................................................. 5-10
Figure 5-10 Transceiver Board  Removal............................................................................................... 5-11
Figure 5-11 Expansion Board and Flex Removal.................... .............................................................. 5-12
Figure 5-12 GPS/GNSS Nameplate Removal.......................... ............................................................. 5-12
Figure 5-13 GPS/GNSS Connector Nut Removal ................................................................................. 5-13
Figure 5-14 GPS/GNSS Cable Removal.............................. ................................................................. 5-13
Figure 5-15 Option Board Removal................................ ....................................................................... 5-14
Figure 5-16 Control Head Flex Removal ............................................................................................... 5-15
Figure 5-17 Volume/Channel Knob Removal ........................................................................................ 5-15
Figure 5-18 Control Head Screws  and Speaker Removal..................................................................... 5-16
Figure 5-19 PCB Retainer Removal ...................................................................................................... 5-16
Figure 5-20 Control Head Boar d Removal ............................................................................................ 5-17
Figure 5-21 Power Button Removal ...................................................................................................... 5-17
Figure 5-22 Keypad Removal...................................... .......................................................................... 5-18
Figure 5-23 Volume Encoder Seal and Mic Jack Seal Removal ........................................................... 5-18
Figure 5-24 Display Pad Gasket Removal ............................................................................................ 5-19
Figure 5-25 Colour Display Removal from PCB .................................................................................... 5-19
Figure 5-26 Control Head Flex Removal ............................................................................................... 5-20
Figure 5-27 Volume/Channel Knob Removal ........................................................................................ 5-20
Figure 5-28 Control Head Boar d Removal ............................................................................................ 5-21
Figure 5-29 Power Button and Keypad Removal .................................................................................. 5-21
Figure 5-30 Speaker Removal (Optional).......................... .................................................................... 5-22
Figure 5-31 Volume Encoder Seal and Mic Jack Seal Removal ........................................................... 5-22
Figure 5-32 Power Button Placement.............................. ...................................................................... 5-23
Figure 5-33 Keypad Assembly..................................... .......................................................................... 5-23
Figure 5-34 Assembly to Control Head Housing ................................................................................... 5-24
Figure 5-35 Assembling Colour Display to PCB.................... ................................................................5 - 2 4
Figure 5-36 Assembling Mic Jack Se al and Display Pad Gasket..... ..................................................... 5-25
Figure 5-37 Assembling Control Head Board to Control Head Assembly ............................................. 5-25
Figure 5-38 Assembling PCB Retainer............................. ..................................................................... 5-26
Figure 5-39 Assembling Speaker .......................................................................................................... 5-26
Figure 5-40 Orientation of Speaker ....................................................................................................... 5-27

--- Halaman 11 ---
List of Figures ix
Figure 5-41 Volume/Channel Kn ob Assembly....................................................................................... 5-27
Figure 5-42 Power Button Pl acement ................................................................................................... 5-28
Figure 5-43 Keypad Assembly .............................................................................................................. 5-28
Figure 5-44 Assembly to Contr ol Head Housing ................................................................................... 5-29
Figure 5-45 Assembling Mic Jack Seal ................................................................................................. 5-29
Figure 5-46 Assemble Speaker ............................................................................................................. 5-30
Figure 5-47 Speaker Retainer Assembly........................... .................................................................... 5-30
Figure 5-48 Assembling Control He ad Board to Control Head Assembly ............................................. 5-31
Figure 5-49 Screw Sequence. ............................................................................................................... 5-31
Figure 5-50 Volume/Channel Kn ob Assembly....................................................................................... 5-32
Figure 5-51 Thermal Pads and Shie ld Gasketing on Chassis and Die Cast Main Shield ..................... 5-33
Figure 5-52 Chassis with Ther mal Pads................................................................................................ 5-33
Figure 5-53 Replacing Regulator Thermal Pads ................................................................................... 5-34
Figure 5-54 Replacing Audio PA Thermal Pad ......................................................................................5 - 3 5
Figure 5-55 Replacing Final Dr iver Thermal Pad ..................................................................................5 - 3 5
Figure 5-56 Applying Therma l Grease .................................................................................................. 5-36
Figure 5-57 Placing the Transceiv er Board in the Chassis.................................................................... 5-36
Figure 5-58 Inserting DC Rete ntion Clip................................................................................................ 5-37
Figure 5-59 Inserting RF Lock Washer and Nut ....................................................................................5 - 3 8
Figure 5-60 Screw Sequence to Compress PCB .................................................................................. 5-38
Figure 5-61 Installing PA Scr ews........................................................................................................... 5-39
Figure 5-62 Inserting Accesso ry Connector .......................................................................................... 5-39
Figure 5-63 Assemblin g Die Cast Main Shield onto Chassis ................................................................ 5-40
Figure 5-64 Screw Sequence to Ti ghten Die Cast Main Shield............................................................. 5-41
Figure 5-65 RF Connector Nut Final Torque ......................................................................................... 5-41
Figure 5-66 Acoustic Plug Ins tallation ................................................................................................... 5-42
Figure 5-67 Inspection of Cover  Assembly with Seal ............................................................................ 5-42
Figure 5-68 Assemb ling Cover onto Chassis ........................................................................................ 5-43
Figure 5-69 GPS/GNSS Plug Ass embly................................................................................................ 5-44
Figure 5-70 GPS/GNSS Cable Inst allation............................................................................................ 5-44
Figure 5-71 GPS/GNSS Cable Inst allation............................................................................................ 5-45
Figure 5-72 Flex Connection Co nnectors.............................................................................................. 5-45
Figure 5-73 Expansion Board A ssembly ............................................................................................... 5-46
Figure 5-74 GPS/GNSS Nameplate Assembly...................................................................................... 5-46
Figure 5-75 GPS/GNSS Antenna C onnector Assembly ........................................................................ 5-47
Figure 5-76 Flex Connection Co nnectors.............................................................................................. 5-47
Figure 5-77 GPS/GNSS Antenna C onnector Assembly ........................................................................ 5-48
Figure 5-78 Orientation of Option Board Flex to Option Board ............................................................. 5-49
Figure 5-79 Assemble Option Boa rd to Radio Chassis ............. ........................................................... 5-49
Figure 5-80 Align Opti on Board to Mounting Holes................ ............................................................... 5-50
Figure 5-81 Assemble O-ring t o Chassis .............................................................................................. 5-51
Figure 5-82 Assemble Control Head to Chassis ................................................................................... 5-51
Figure 5-83 Flex Connection Co nnectors.............................................................................................. 5-52
Figure 5-84 Radio Assembly Exploded View........................ ................................................................. 5-53
Figure 5-85 Colour Display Control Head Exploded View........... .......................................................... 5-55
Figure 5-86 Numeric Display Con trol Head Exploded View .................................................................. 5-56

--- Halaman 12 ---
x List of Tables
List of Tables
Table 1-1 Radio Frequency Ranges  and Power Levels............... ........................................................ 1-1
Table 2-1 Recommended Test Equipment ............................ ............................................................... 2-1
Table 2-2 Service Aids .......................................... ............................................................................... 2-2
Table 3-1 Initial Equipment Control Settings .................... .................................................................... 3-1
Table 3-2 Front Panel Access Test Mode Displays ................. ............................................................. 3-2
Table 3-3 Test Environments..................................... ........................................................................... 3-6
Table 3-4 Test Channel Spacing .................................. ........................................................................ 3-6
Table 3-5 Test Frequencies  .................................... ............................................................................ 3-6
Table 3-6 Transmitter Performance Checks........................ ................................................................. 3-7
Table 3-7 Receiver Performance Checks ........................... ................................................................. 3-8
Table 4-1 Radio Software Program Kit............................ ..................................................................... 4-1
Table 5-1 Lead Free Solder Wire Part Number List ................ ............................................................. 5-4
Table 5-2 Lead Free Solder Paste Part Number List ............... ............................................................ 5-4
Table 5-3 Radio Exploded View Parts List ........................ ................................................................. 5-54
Table 5-4 Colour Display Control H ead (PMLN7501_) Exploded View Parts List.............................. 5-55
Table 5-5 Numeric Display Control Head (PMLN7500_) Exploded View  Parts List........................... 5-56
Table 5-6 Torque Specifications  for Nuts and Screws........................................................................ 5-57
Table 6-1 Power-Up Error Codes.................................. ....................................................................... 6-2

--- Halaman 13 ---
Warranty and Service Support xi
Warranty and Service Support
Motorola offers long term support for its products. This support includes full exchange and/or repair 
of the product during the warranty period, and service/ repair or spare parts support out of warranty. 
Warranty Period and Return Instructions
The terms and conditions of warranty are defined fully in the Motorola Dealer or Distributor or 
Reseller contract. These conditions may change from time to time and the following notes are for 
guidance purposes only. In instances where the product is covered under a "return for replacement" 
or "return for repair" warranty, a check of the product should be performed prior to shipping the unit 
back to Motorola. This is to ensure that the product has been correctly programmed or has not been 
subjected to damage outside the terms of the warranty.
Prior to shipping any radio back to the appropriate Motorola warranty depot, please contact 
Customer Resources or your Motorola dealer, distributor or reseller. All returns must be 
accompanied by a Warranty Claim Form, available from your Customer Service representative or 
Motorola Online Extranet (MOL) or your Motorola dealer, distributor or reseller. Products should be 
shipped back in the original packaging, or correctly packaged to ensure no damage occurs in transit.
After Warranty Period
After the Warranty period, Motorola continues to support its products in two ways. 
1. Motorola's Managed Technical Services (MTS) offers a repair service to both end users and 
dealers at competitive prices. 
2. MTS supplies individual parts and modules that can be purchased by dealers who are 
technically capable of performing fault analysis and repair.
CM7668/XiR M8600 Series Mobile Radios Two (2) Years
Product Accessories One (1) Year

--- Halaman 14 ---
xii Warranty and Service Support 
Notes

--- Halaman 15 ---
Chapter 1 Introduction
1.1 Notations Use d in This Manual
Throughout the text in this publication, you will notice the use of note and caution notations. These 
notations are used to emphasize that safety hazards exist, and due care must be taken and 
observed.
NOTE: An operational procedure, practice, or condition that is essential to emphasize.
1.2 Radio Description
The CM7668/XiR M8600 series mobile radios are available in the following frequency ranges and 
power levels.
* Low Power: 1–25 Watts
High Power: 25–40 Watts
These radios are among the most sophisticated two-way radios available. They have a
robust design for radio users who need high performance, quality, and reliability in their daily 
communications. This architecture provides the capability of supporting a multitude of legacy and 
advanced features resulting in a more cost-effective two-way radio communications solution.
CAUTION indicates a potentially hazardous situation which, if 
not avoided, might result in equipment damage.
Table 1-1  Radio Frequency Ranges and Power Levels
Freq. Band Bandwidth Power Level
VHF 136–174 MHz 1–25 Watts
25–45 Watts
350 MHz 350–400 MHz 1–25 Watts
1–40 Watts
UHF B1 403–470 MHz 1–25 Watts
25–40 Watts
UHF B2 450–527 MHz *1–40 Watts
!
C a u t i o n

--- Halaman 16 ---
1-2 Introduction: Control Head Description
1.3 Control Head Description
The control head used with the radio has logic circuitry that operates the standard and optional 
features built into the system.
The following illustrations show the typical radio control heads.
Figure 1-1  Radio Control Head (Colour Display Model)
1.3.1 Control Head Controls (Colour Display Model)
• POWER BUTTON – Turns the radio on and off.
• VOLUME/CHANNEL KNOB – Rotate clockwise to increase volume level; rotate 
counterclockwise to decrease volume level. Push knob to activate channel function; rotate 
clockwise and counterclockwise to select channel.
• LED INDICATORS – Red, yellow and green light-emitting diodes indicate operating status.
• LCD (Liquid Crystal Display) – 160x72 display provides visual information about many radio 
features.
• OK/MENU BUTTON – One button to provide menu navigation and selection interface.
• PROGRAMMABLE BUTTONS – Four buttons are field programmable using the CPS.
• SCROLL UP/DOWN BUTTONS – Press buttons to scroll.
• RETURN/HOME BUTTON – One button which quickly brings you to the home page.
Scroll Up/DownLCD ScreenVolume/Channel Knob
Power Button
Speaker
Return/Home Button
Programmable ButtonsMic Connector
LED
Indicators
OK/Menu Button

--- Halaman 17 ---
Introduction: Control Head Description 1-3
Figure 1-2  Radio Control Head (Numeric Display Model)
1.3.2 Control Head Controls (Numeric Display Model)
• POWER BUTTON – Turns the radio on and off.
• VOLUME/CHANNEL KNOB – Rotate clockwise to increase volume level; rotate 
counterclockwise to decrease volume level. Push knob to activate channel function; rotate 
clockwise and counterclockwise to select channel.
• LED INDICATORS – Red, yellow and green light-emitting diodes indicate operating status.
• LED NUMERIC DISPLAY – Two digit numeric display.
• PROGRAMMABLE BUTTONS – Four buttons are field programmable using the CPS.
P1 P2 P3 P4P4
Volume/Channel Knob
Power Button
LED
Indicators LED Display
Programmable Buttons
Speaker
Mic Connector

--- Halaman 18 ---
1-4 Introduction: MOTOTRBO Mobile Radio Model Numbering Scheme
1.4 MOTOTRBO  Mobile Radio Model Numbering Scheme
  
Figure 1-3  Mobile Radio Model Numbering Scheme
Model No.Example :  AZ M 2 8 Q P H 9 L A 1 A N
Position           :  1 2 3 4 5 6 7 8 9 10 11 12
Unique Variations
N: Standard Package
Version Letter
Feature Level
1: Mini-U (Mobile)
2: BNC (Mobile)
Primary System Type
A: Conventional
B: Trunking 
C: Analogue Only
D: Limited System
Channel Information
9: Variable/Programmable
    Channel Spacing 
Power Level
N: 1–25W
P: 25–40W
Q: 25–45W
R: 1–40W
M: 10–35W
MOTOTRBO Mobile
CM7668/XiR M8600 Series : 28
Band
J 
M
K : 300–360 MHz
P
Q
T 
X 
U
V Physical PackagesC: Low Tier (Numeric Display)
H: Mid Tier (Monochrome Display)
N: High Tier (Colour Display)
Mobile
AZ: Asia
LA: Latin America
AA: North America (except Mexico)
MD: Europe/Middle East/
        Africa/Australia
: 136–174 MHz
: 217–222 MHz
: 350–400 MHz
: 403–470 MHz
: 450–527 MHz
: 450–520 MHz
: 806–941 MHz
: 806–870 MHz
Primary Operation
J: Basic (No GPS, No Bluetooth)
K: GNSS (GPS, GALILEO, QZSS,
     GLONASS, or BEIDOU2) and Bluetooth
L: GPS Only
M: Bluetooth Only

--- Halaman 19 ---
Introduction: VHF High Power (136–174 MHz) Model Chart 1-5
1.5 VHF High Power (136 –174 MHz) Model Chart 
VHF 136–174 MHz 25–45W, BNC
Model Description
AZM28JQC9JA2_N 136–174 MHz, 25–45W, MOTOTRBO XiR M8620 Numeric Display 
Mobile
AZM28JQC9KA2_N 136–174 MHz, 25–45W, MOTOTRBO XiR M8628 Numeric D isplay 
Mobile with Bluetooth and GPS
AZM28JQN9JA2_N 136–174 MHz, 25–45W, MOTOTRBO XiR M8660 Colour Display 
Mobile
AZM28JQN9KA2_N 136–174 MHz, 25–45W , MOTOTRBO XiR M8668 Colour Display 
Mobile with Bluetooth and GPS
Item Description
X X X X PMUD2565_S *Service Kit, VHF, 25–45W
X X PMLN6042_S Bluetooth and GPS Expansion Board Service Kit
O O O O PMLN5718_S Generic Option Board Service Kit
X X PMLN7500_ Numeric Display Model Control Head
X X PMLN7501_ Colour Display Model Control Head
X = Item Included
O = Optional Item
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 20 ---
1-6 Introduction: VHF Low Power (136–174 MHz) Model Chart
1.6 VHF Low Power (136–174 MHz) Model Chart  
VHF 136–174 MHz 1–25W, BNC
Model Description
AZM28JNC9JA2_N 136–174 MHz, 1–25W, MOTOTRBO XiR M8620 Numeric Display 
Mobile
AZM28JNC9KA2_N 136–174 MHz, 1–25W, MOTOTRBO XiR M8628 Numeric Di splay 
Mobile with Bluetooth and GPS
AZM28JNN9JA2_N 136–174 MHz, 1–25W, MOTOTRBO XiR M8660 Colour Display 
Mobile
AZM28JNN9KA2_N 136–174 MHz, 1–25W , MOTOTRBO XiR M8668 Colour Display 
Mobile with Bluetooth and GPS
Item Description
X X X X PMUD2568_S *Service Kit, VHF, 1–25W
X X PMLN6042_S Bluetooth and GPS Expansion Board Service Kit
O O O O PMLN5718_S Generic Option Board Service Kit
X X PMLN7500_ Numeric Dis play Model Control Head
X X PMLN7501_ Colour Display Model Control Head
X = Item Included
O = Optional Item
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 21 ---
Introduction: 350 MHz High Power (350–400 MHz) Model Chart 1-7
1.7 350 MHz High Power (350–400 MHz) Model Chart
350 MHz Band, 350–400 MHz 1–40W, BNC
Model Description
AZM28PRC9KA2_N 350–400 MHz, 1–40W, MOTOTRBO XiR M8628 Numeric Display 
Mobile with Bluetooth and GNSS
AZM28PRN9KA2_N 350–400 MHz, 1–40W, MOTOTRBO XiR M8668 Colour Dis play 
Mobile with Bluetooth and GNSS
Item Description
X X PMUD3329_S *Service Kit , 350 MHz Band, LP–HP
X X PMLN6847_S Service Kit, Blueto oth and GNSS Expansion Board 
X PMLN5718_S Service Kit, Generic Option Board
X PMLN7500_ Numeric Display Model Control Head
X PMLN7501_ Colour Display Model Control Head
X = Item Included
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 22 ---
1-8 Introduction: 350 MHz Low Power (350–400 MHz) Model Chart
1.8 350 MHz Low Power (350–400 MHz) Model Chart  
350 MHz Band, 350–400 MHz 1–25W, BNC
Model Description
AZM28PNC9KA2_N 350–400 MHz, 1–25W, MOTOTRBO XiR M8628 Numeric Display 
Mobile with Bluetooth and GNSS
AZM28PNN9KA2_N 350–400 MHz, 1–25W, MOTOTRBO XiR M8668 Colour Dis play 
Mobile with GOB2, Bluetooth and GNSS
Item Description
X X PMUD3329_S *Service Kit , 350 MHz Band, LP–HP
X PMUD3363_S *Service Kit , Colour  Display, GOB2, Bluetooth and GNSS Expan-
sion Board, De-Moto
X X PMLN6847_S Service Kit, Bluetooth and GNSS Expansion Board 
X X PMLN6665_S Service Kit, Generic Option Board 2
X PMLN7500_ Numeric Display Model Control Head
X PMLN7501_ Colour Display Model Control Head
X = Item Included
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 23 ---
Introduction: UHF1 High Power (403–470 MHz) Model Chart 1-9
1.9 UHF1 High Power (4 03–470 MHz) Model Chart 
UHF1 403–470 MHz 25–40W, BNC
Model Description
AZM28QPC9JA2_N 403–470 MHz, 25–40W, MOTOTRBO XiR M8620 Numeric Display 
Mobile
AZM28QPC9KA2_N 403–470 MHz, 25–40W, MOTOTRBO XiR M8628 Numeric D isplay 
Mobile with Bluetooth and GPS
AZM28QPN9JA2_N 403–470 MHz, 25–40W, MOTOTRBO XiR M8660 Colour Display 
Mobile
AZM28QPN9KA2_N 403–470 MHz, 25–40W, MOTOTRBO XiR M8668 Colour Di splay 
Mobile with Bluetooth and GPS
AZM28QPN9KD2_N 403–470 MHz, 25–40W, MOTOTRBO CM7668 Colour Display 
Mobile with Bluetooth, GPS and NOB
Item Description
XXXXXP M U E 3 6 4 7 _ S * S e r v i c e  K i t ,  U H F  B 1 ,  2 5 – 4 0 W
X X X PMLN6042_S Bluetooth and GPS Expansion Board Service Kit
OOOOOP M L N 5 7 1 8 _ S G e n e r i c  O p t i o n  B o a r d  S e r v i c e  K i t
X X PMLN7500_ Numeric Display Model Control Head
X X X PMLN7501_ Colour Display Model Control Head
X = Item Included
O = Optional Item
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 24 ---
1-10 Introduction: UHF1 Low Power (403–470 MHz) Model Chart
1.10 UHF1 Low Power (403–470 MHz) Model Chart   
UHF1 403–470 MHz 1–25W, BNC
Model Description
AZM28QNC9JA2_N 403–470 MHz, 1–25W, MOTOTRBO XiR M8620 Numeric Display 
Mobile
AZM28QNC9KA2_N 403–470 MHz, 1–25W, MOTOTRBO XiR M8628 Numeric Di splay 
Mobile with Bluetooth and GPS
AZM28QNN9JA2_N 403–470 MHz, 1–25W, MOTOTRBO XiR M8660 Colour Display 
Mobile
AZM28QNN9KA2_N 403–470 MHz, 1–25W, MOTOTRBO XiR M8668 Colour Dis play 
Mobile with Bluetooth and GPS
Item Description
X X X X PMUE3646_S *Service Kit, UHF B1, 1–25W
X PMUE5132_ *Service Kit, UHF B1,  1–25W, Bluetooth, GPS, Colour Display, 
DE-MOTO
X X PMLN6042_S Bluetooth and GPS Expansion Board Service Kit
O O O O PMLN5718_S Generic Opt ion Board Service Kit
X X PMLN7500_ Numeric Display Model Control Head
X X PMLN7501_ Colour Displ ay Model Control Head
X = Item Included
O = Optional Item
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 25 ---
Introduction: UHF2 (450–527 MHz) Model Chart 1-11
1.11 UHF2 (450–527 MHz) Model Chart 
UHF2 450–527 MHz 1–40W, BNC
Model Description
AZM28TRC9JA2_N 450–527 MHz, 1–40W, MOTOTRBO XiR M8620 Numeric Display 
Mobile
AZM28TRC9KA2_N 450–527 MHz, 1–40W, MOTOTRBO XiR M8628 Numeric Di splay 
Mobile with Bluetooth and GPS
AZM28TRN9JA2_N 450–527 MHz, 1–40W, MOTOTRBO XiR M8660 Colour Display 
Mobile
AZM28TRN9KA2_N 450–527 MHz, 1–40W , MOTOTRBO XiR M8668 Colour Display 
Mobile with Bluetooth and GPS
Item Description
X X X X PMUE4125_S *Service Kit, UHF B2, 1–40W
X X PMLN6042_S Bluetooth and GPS Expansion Board Service Kit
O O O O PMLN5718_S Generic Option Board Service Kit
X X PMLN7500_ Numeric Display Model Control Head
X X PMLN7501_ Colour Display Model Control Head
X = Item Included
O = Optional Item
* = Service Kit is the main board only
_ = the latest version kit. When ordering a kit, refer to your specific kit for the suffix number.
See “Additional Service Kit Information” on page A-2 for guidelines on selecting the appropriate 
Service Kit, based on the Model and Super Tanapa combination of your radio.

--- Halaman 26 ---
1-12 Introduction: Specifications
1.12 Specifications   
* Low Power: 1–25 Watts
High Power: 25–40 Watts
General
Specification VHF 350 MHz UHF1 UHF2
Model: NumericDisplay ColorDisplay NumericDisplay ColorDisplay NumericDisplay ColorDisplay NumericDisplay ColorDisplay
Channel 
Capacity: 99 1000 99 1000 99 1000 99 1000
Typical RF Output:
Low Power
High Power
1–25 W 1–25 W
1–40 W
1–25 W 1–40 W
Frequency Range: 136–174 MHz 350–400 MHz 403–470 MHz 450–527 MHz
Dimensions: 
(HxWxL)
2.1 x 6.9 x 8.1 in 
(53.3 x 175.3 x 205.7 mm)
Weight: 3.9 lbs. (1.8 kg)
Current Drain:
Standby
Rx @ rated audio
Transmit
0.81 A max
2 A max
1–25 W: 11.0 A max
25–40 W: 14.5 A max
25–45 W: 14.5 A max
FCC Description:
1–25 W: 
ABZ99FT3086
25–45 W: 
ABZ99FT3087
–
1–25 W: 
ABZ99FT4087
25–40 W: 
ABZ99FT4088
1–40 W: 
ABZ99FT4085
IC Description:
1–25 W: 
109AB-99FT3086
25–45 W: 
109AB-99FT3087
–
1–25 W: 
109AB-99FT4087
25–40 W: 
109AB-99FT4088
1–40 W: 
109AB-99FT4085

--- Halaman 27 ---
Introduction: Specifications 1-13
 
Receiver
Specification VHF 350 MHz UHF1 UHF2
Model: Numeric
Display
Color
Display
Numeric
Display
Color
Display
Numeric
Display 
Color
Display
Numeric
Display 
Color
Display
Frequencies: 136–174 MHz 350–400 MHz 403–470 MHz 450–527 MHz
Channel Spacing: 12.5 kHz/20 kHz/25 kHz 12.5 kHz/25 kHz
Analog
Sensitivity:
0.3 µV 
0.22 µV (Typical)
Digital Sensitivity:
(5% BER)
 0.25 µV
0.19 µV (Typical)
Intermodulation
TIA603D:
ETS:
78 dB
70 dB
75 dB
70 dB
Adjacent Channel 
Selectivity
TIA603D:
ETS:
50 dB @ 12.5 kHz,
80 dB @ 25 kHz
60 dB @ 12.5 kHz,
70 dB @ 25 kHz
50 dB @ 12.5 kHz,
75 dB @ 25 kHz
60 dB @ 12.5 kHz,
70 dB @ 25 kHz
Spurious
Rejection 
TIA603D:
ETS:
80 dB
70 dB
75 dB
70 dB
Rated Audio:
3 W (Internal)
7.5 W (External – 8 ohms)
13 W (External – 4 ohms)
Audio Distortion @ 
Rated Audio: 3% (Typical)
Hum and Noise: -40 dB @ 12.5 kHz-45 dB @ 20/25 kHz -40 dB @ 12.5 kHz-45 dB @ 25 kHz
Audio Response: +1, -3 dB
Conducted 
Spurious 
Emission:
-57 dBm

--- Halaman 28 ---
1-14 Introduction: Specifications
 
* Low Power: 1–25 Watts
High Power: 25–40 Watts
Transmitter
Specification VHF 350 MHz UHF1 UHF2
Model: NumericDisplay ColorDisplay NumericDisplay ColorDisplay NumericDisplay  ColorDisplay NumericDisplay ColorDisplay
Frequencies: 136–174 MHz 350–400 MHz 403–470 MHz 450–527 MHz
Channel Spacing: 12.5 kHz/20 kHz/25 kHz 12.5 kHz/25 kHz
Frequency 
Stability:
(-30°C to +60°C, 
+25°C Ref)
±0.5 ppm 
Power Output:
Low Power
High Power
1–25 W
25–45 W
1–25 W
1–40 W
1–25 W
25–40 W 1–40 W
Modulation
Limiting:
±2.5 kHz @ 12.5 kHz
±4.0 kHz @ 20 kHz
±5.0 kHz @ 25 kHz
±2.5 kHz @ 12.5 
kHz
±5.0 kHz @ 25 kHz
FM Hum and 
Noise:
-40 dB @ 12.5 kHz
-45 dB @ 20/25 kHz
-40 dB @ 12.5 kHz
-45 dB @ 25 kHz
Conducted/
Radiated 
Emission:
-36 dBm <1 GHz
-30 dBm >1 GHz
Adjacent 
Channel Power:
60 dB @ 12.5 kHz
70 dB @ 20/25 kHz
60 dB @ 12.5 kHz
70 dB @ 25 kHz
Audio Response: +1, -3 dB
Audio Distortion: 3%
Digital Vocoder 
Type: AMBE+2™
Digital Protocol:
ETSI TS 102 361-1
ETSI TS 102 361-2
ETSI TS 102 361-3

--- Halaman 29 ---
Introduction: Specifications 1-15
  
Conforms to:
ETSI TS 102 361 (Parts 1, 2 & 3) – ETSI DMR Standard
1999/5/EC (R&TTE – Radio and Telecommunications Terminal Equipment)
2011/65/EU (RoHS 2 – Banned Substances)
2012/19/EU (WEEE – Waste Electrical and Electronic Equipment)
94/62/EC (Packaging and Packaging Waste)
Radio meets applicable regulatory requirements.
 
NOTE: Global Navigation Satellite System (GNSS) is only applicable to 350–400 MHz band.
 
Self-Quieter
VHF 350 MHz UHF1 UHF2
– 391.2 MHz – 489.000 MHz
GPS/GNSS
Model: Numeric Display Colour Display
Accuracy specs are for long-term tracking (95th percentile values > 5 satellites 
visible at a nominal -130 dBm signal strength).
TTFF (Time to First 
Fix) Cold Start: < 1 minute
TTFF Hot Start: < 10 seconds
Horizontal 
Accuracy: < 5 meters
Bluetooth 
Model: Numeric Display Colour Display
Version: Supports Bluetooth 2.1 + EDR Specification.
Range: Class 2, 10 meters

--- Halaman 30 ---
1-16 Introduction: Specifications
Specifications subject to change without notice. All specifications shown are typical.
Military Standards 810C, D, E, F & G
MIL-STD 810C MIL-STD 810D MIL- STD 810E MIL-STD 810F MIL-STD 810G
Method Proc./Cat Method Proc./Cat Me thod Proc./Cat Method Proc./Cat Met hod Proc./Cat
Low 
Pressure
500.1 I 500.2 II 500.3 II 500.4 II 500.5 II
High 
Temperature
501.1 I, II 501.2 I/A1,
II/A1
501.3 I/A, 
II/AI
501.4 I/HOT, 
II/HOT
501.5 I/AI, II
Low 
Temperature
502.1 I 502.2 I/C3,
II/C1
502.3 I/C3, 
II/C1
502.4 I/C3,
II/C1
502.5 I/C3, II
Temperature 
Shock
503.1 – 503.2 I/A1/C3 503.3 I/AI/C3 503.4 I 503.5 I/C
Solar 
Radiation
505.1 II 505.2 I 505.3 I 505.4 I 505.5 I/A1
Rain 506.1 I, II 506.2 I, II 506.3 I , II 506.4 I, II I 506.5 I, III
Humidity 507.1 II 507.2 II 507.3 II 507.4 – 507.5 II - Aggra-
vated
Salt Fog 509.1 – 509.2 – 509.3 – 509.4 – 509.5 –
Dust 510.1 I 510.2 I 510.3 I 510.4 I 510.5 I
Vibration 514.2 VIII/F,
Curve-W
514.3 I/10,
II/3
514.4 I/10, 
II/3
514.5 I/24 514.6 I/24
Shock 516.2 I, II 516.3 I, IV 516.4 I, IV 516.5 I, IV 516.6 I, IV, 
V, VI
Environmental Specifications
Operating Temperature -30°C to +60°C
Storage Temperature -40°C to +85°C
Temperature Shock Per MIL-STD
Humidity Per MIL-STD
ESD IEC 61000-4-2 Level 3
Water and Dust Intrusion IP54, MIL-STD
<a href="../README.md"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/640d8577-87b5-481d-8511-f9ecea8db5e7"> HOME</a>

# Production Files

On this page, we cover how to output all the required production files from the KiCAD project. All production files should end up in the `output/` folder:

<a href="https://raw.githubusercontent.com/Embeetle/tiny-scarab/main/output.zip"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/2217c6c9-1fad-4934-8090-661ed2869178"> output.zip</a>



&nbsp;<br>
## 1. Gerber Files

The Gerber Files specify the layout of copper tracks, vias, solder masks, and other components. To generate them, open the PCB Layout from your KiCAD project. Then click `File` > `Fabrication Outputs` > `Gerbers`:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/64948d99-f300-4e62-b19a-73a3d4b9f682">

The following window appears:

<img width="700" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/aba4294d-9814-47b1-8691-7afbc32a4692">

I left everything in the default value, except for `Subtract soldermask from silkscreen`. I checked that option to ensure no silkscreen ends up on the copper pads. Set the Output directory to `output/` and click `Plot` at the bottom of the window. Now you should have the following files in `output/`:

- [`tiny-scarab-B_Cu.gbr`](../output/tiny-scarab-B_Cu.gbr)
- [`tiny-scarab-B_Mask.gbr`](../output/tiny-scarab-B_Mask.gbr)
- [`tiny-scarab-B_Paste.gbr`](../output/tiny-scarab-B_Paste.gbr)
- [`tiny-scarab-B_Silkscreen.gbr`](../output/tiny-scarab-B_Silkscreen.gbr)
- [`tiny-scarab-Edge_Cuts.gbr`](../output/tiny-scarab-Edge_Cuts.gbr)
- [`tiny-scarab-F_Cu.gbr`](../output/tiny-scarab-F_Cu.gbr)
- [`tiny-scarab-F_Mask.gbr`](../output/tiny-scarab-F_Mask.gbr)
- [`tiny-scarab-F_Paste.gbr`](../output/tiny-scarab-F_Paste.gbr)
- [`tiny-scarab-F_Silkscreen.gbr`](../output/tiny-scarab-F_Silkscreen.gbr)
- [`tiny-scarab-In1_Cu.gbr`](../output/tiny-scarab-In1_Cu.gbr)
- [`tiny-scarab-In2_Cu.gbr`](../output/tiny-scarab-In2_Cu.gbr)
- [`tiny-scarab-job.gbrjob`](../output/tiny-scarab-job.gbrjob)

&nbsp;<br>
## 2. Drill Files

The Drill Files specify all the drill holes in the board. Click `Generate Drill Files...` in the bottom-right corner of the previous window. Another popup window comes on top now:

<img width="600" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/f971f83d-d349-4f99-85cd-cc5e1674ea15">

Again, I left everything in the default state, except for the Drill Units. I put them to `mm`. Make sure the output directory is set to `output/` and click the `Generate Drill File` button at the bottom. Then click also the `Generate Map File`. Now you should end up with the following output files:

- [`tiny-scarab-NPTH.drl`](../output/tiny-scarab-NPTH.drl)
- [`tiny-scarab-NPTH-drl_map.gbr`](../output/tiny-scarab-NPTH-drl_map.gbr)
- [`tiny-scarab-PTH.drl`](../output/tiny-scarab-PTH.drl)
- [`tiny-scarab-PTH-drl_map.gbr`](../output/tiny-scarab-PTH-drl_map.gbr)

&nbsp;<br>
## 3. BOM

KiCAD outputs two BOM (Bill of Materials) files:

- [`tiny-scarab.csv`](../output/tiny-scarab.csv)
- [`tiny-scarab.xml`](../output/tiny-scarab.xml)

They can be generated in the KiCAD Schematic Editor by clicking `Tools` > `Generate BOM`:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/a2b37f38-c881-4602-8dc7-6ffaf24ca673">

KiCAD then generates these two BOM files in the toplevel folder. I moved them to the `output/` subfolder to keep the toplevel folder tidy.

Below is the BOM file trimmed down to the essential columns:

 - **Manufacturer**
 - **MPN** (Manufacturer Part Number)
 - **Supplier**
 - **SPN** (Supplier Part Number)


| **Item** | **Qty** | **Reference(s)**                                                                                          | **Value** | **Manufacturer**                    | **MPN**                | **Supplier** | **SPN**                   |
|----------|---------|-----------------------------------------------------------------------------------------------------------|-----------|-------------------------------------|------------------------|--------------|---------------------------|
| 1        | 23      | C1, C2, C3, C4, C5, C6, C7, C8, C13, C14, C15, C19, C20, C21, C22, C23, C26, C27, C28, C29, C33, C34, C36 | 100n      |                                     | `GPC0402104-16`        |              |                           |
| 2        | 4       | C9, C11, C12, C16                                                                                         | 1u        |                                     | `GPC0402105-16`        |              |                           |
| 3        | 2       | C10, C17                                                                                                  | 10u       |                                     | `GPC0402106-6.3`       |              |                           |
| 4        | 9       | C18, C30, C31, C32, C35, C37, C38, C39, C40                                                               | 10u       |                                     | `GPC0805106`           |              |                           |
| 5        | 1       | D1                                                                                                        |           | Littelfuse Inc.                     | `SMAJ5.0A`             | DigiKey      | `SMAJ5.0ALFTR-ND`         |
| 6        | 1       | D2                                                                                                        |           | Micro Commercial Co                 | `SMAZ5V6-TP`           | DigiKey      | `SMAZ5V6-TPMSTR-ND`       |
| 7        | 2       | D3, D4                                                                                                    |           | Bourns                              | `CDSOD323-T05LC`       | DigiKey      | `CDSOD323-T05LCTR-ND`     |
| 8        | 1       | D5                                                                                                        |           | ANBON SEMICONDUCTOR (INT'L) LIMITED | `SD103AWS`             | DigiKey      | `4530-SD103AWSTR-ND`      |
| 9        | 1       | F1                                                                                                        |           | Bourns Inc.                         | `SF-1206F100-2`        | DigiKey      | `SF-1206F100-2TR-ND`      |
| 10       | 1       | F2                                                                                                        |           | Littelfuse Inc.                     | `0402L050SLKR`         | DigiKey      | `F5759TR-ND`              |
| 11       | 1       | J1                                                                                                        |           | GCT                                 | `USB4110-GF-A`         | DigiKey      | `2073-USB4110-GF-A-2-ND`  |
| 12       | 2       | J3, J4                                                                                                    |           | Amphenol ICC (FCI)                  | `10129383-914001ALF`   | DigiKey      | `10129383-914001ALF-ND`   |
| 13       | 4       | LED1, LED2, LED3, LED4                                                                                    |           | Wurth Elektronik                    | `150060GS55040`        | DigiKey      | `732-12014-2-ND`          |
| 14       | 3       | Q1, Q2, Q3                                                                                                |           | Infineon Technologies               | `IRLML2502TRPBF`       | DigiKey      | `IRLML2502TRPBFTR-ND`     |
| 15       | 2       | R1, R2                                                                                                    | 5k1       |                                     | `GPR04025K1`           |              |                           |
| 16       | 2       | R3, R25                                                                                                   | 200       |                                     | `GPR0402200R`          |              |                           |
| 17       | 2       | R4, R6                                                                                                    | 270       |                                     | `GPR0402270R`          |              |                           |
| 18       | 4       | R8, R17, R18, R19                                                                                         | 0         |                                     | `GPR04020R`            |              |                           |
| 19       | 3       | R10, R12, R24                                                                                             | 1k        |                                     | `GPR04021K`            |              |                           |
| 20       | 1       | R11                                                                                                       | 100k      |                                     | `GPR0402100K`          |              |                           |
| 21       | 1       | R13                                                                                                       | 130       |                                     | `GPR0402130R`          |              |                           |
| 22       | 1       | R14                                                                                                       | 20        |                                     | `GPR040220R`           |              |                           |
| 23       | 3       | R15, R16, R23                                                                                             | 10k       |                                     | `GPR040210K`           |              |                           |
| 24       | 1       | R22                                                                                                       | 470       |                                     | `GPR0402470R`          |              |                           |
| 25       | 4       | SW1, SW2, SW3, SW4                                                                                        |           | C&K                                 | `PTS636 SL43 SMTR LFS` | DigiKey      | `CKN12309-2-ND`           |
| 26       | 1       | SW5                                                                                                       |           | CUI Devices                         | `SLW-883935-2A-D`      | DigiKey      | `2223-SLW-883935-2A-D-ND` |
| 27       | 1       | U1                                                                                                        |           | Microchip Technology                | `MCP1825ST-3302E/DB`   | DigiKey      | `MCP1825ST-3302E/DBTR-ND` |
| 28       | 1       | U2                                                                                                        |           | WCH                                 | `CH32V305FBP6`         | AliExpress   | `1005004329064488`        |
| 29       | 1       | U3                                                                                                        |           | WCH                                 | `CH32V003F4P6`         | AliExpress   | `1005005036714708`        |
| 30       | 1       | XTAL1                                                                                                     |           | Diodes Incorporated                 | `FL1200156`            | DigiKey      | `FL1200156-ND`            |
| 31       | 1       | XTAL2                                                                                                     |           | ECS Inc.                            | `ECS-240-20-30B-TR`    | DigiKey      | `XC1122TR-ND`             |


Please note that the capacitors and resistors got a special **MPN** code. Their MPN code doesn't represent a *Manufacturer Part Number*, but rather a *Generic Part Number*. More on that in the next paragraph.


&nbsp;<br>
### Generic Part Numbers

For some components - like (most of) the resistors and capacitors - it doesn't make sense to give specific part numbers to your board manufacturer. If you want a `0402` sized `1k` resistor, you probably don't care what brand it is. Let the board manufacturer choose what they have in stock. For this reason, Eurocircuits came up with *'Generic Part Numbers'*:

 - <a href="https://www.eurocircuits.com/generic-components/generic-capacitors/" target="_blank">Eurocircuits Generic Capacitors</a>
 - <a href="https://www.eurocircuits.com/generic-components/generic-resistors/" target="_blank">Eurocircuits Generic Resistors</a>

Below is a table of the Generic Components used in the Tiny Scarab board:

#### Generic Capacitors

| **MPN/GPN**            | **Value** | **Tol%** | **Voltage** | **Dielectric** | **Description**                                         |
|------------------------|-----------|----------|-------------|----------------|---------------------------------------------------------|
| `GPC0402104-16`        | 100n      | 10%      | 16V         | X7R            | 0.1µF ±10% 16V Ceramic Capacitor X7R 0402 (1005 Metric) |
| `GPC0402105-16`        | 1u        | 10%      | 16V         | X5R            | 1µF ±10% 16V Ceramic Capacitor X5R 0402 (1005 Metric)   |
| `GPC0402106-6.3`       | 10u       | 20%      | 6.3V        | X5R            | 10µF ±20% 6.3V Ceramic Capacitor X5R 0402 (1005 Metric) |
| `GPC0805106`           | 10u       | 10%      | 10V         | X7R            | 10 µF ±10% 10V Ceramic Capacitor X7R 0805 (2012 Metric) |


#### Generic Resistors

| **MPN/GPN**            | **Value** | **Tol%** | **Power**   | **Voltage**    | **Description**                                                                             |
|------------------------|-----------|----------|-------------|----------------|---------------------------------------------------------------------------------------------|
| `GPR04025K1`           | 5k1       | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 5.1 kohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose |
| `GPR0402200R`          | 200       | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 200 ohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose  |
| `GPR0402270R`          | 270       | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 270 ohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose  |
| `GPR04020R`            | 0         |          | 100mW       |                | SMD Chip Resistor, Jumper, 0 ohm, 100 mW, 0402 [1005 Metric], Thick Film, General Purpose   |
| `GPR04021K`            | 1k        | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 1 kohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose   |
| `GPR0402100K`          | 100k      | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 100 kohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose |
| `GPR0402130R`          | 130       | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 130 ohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose  |
| `GPR040220R`           | 20        | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 20 ohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose   |
| `GPR040210K`           | 10k       | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 10 kohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose  |
| `GPR0402470R`          | 470       | 1%       | 62.5mW      | 50V            | SMD Chip Resistor, 470 ohm, ± 1%, 62.5 mW, 0402 [1005 Metric], Thick Film, General Purpose  |

&nbsp;<br>
## 4. Component Placement File

The Component Placement File specifies where each component must be placed as well as its rotation. Click `File` > `Fabrication Outputs` > `Component Placement File`:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/c1ce2ba6-2be8-4be1-81e7-73c1e3df238b">

Make sure the output directory is set to `output/`. I selected `csv` for the format, `mm` for the units and `Single file for board` because I only have components on the top side of the PCB:

<img width="500" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7fd13245-4d97-4a83-b29f-578cd033f318">

Click the button `Generate Position File`. You should now get this result:

- [`tiny-scarab-all-pos.csv`](../output/tiny-scarab-all-pos.csv)



&nbsp;<br>
<a href="../README.md#index"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7eef998b-278f-46d1-8f7c-8e4333ccd19c"> GO BACK</a>

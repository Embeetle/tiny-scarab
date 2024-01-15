<a href="../README.md"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/640d8577-87b5-481d-8511-f9ecea8db5e7"> HOME</a>

# Production Files

## 1. BOM

The BOM (Bill Of Materials) files `tiny-scarab.csv` and `tiny-scarab.xml` can be generated in the KiCAD Schematic Editor by clicking `Tools` > `Generate BOM`:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/a2b37f38-c881-4602-8dc7-6ffaf24ca673">

KiCAD then generates these two BOM files in the toplevel folder. I move them to the `output/` subfolder. You can click them below to access them directly:

- [`tiny-scarab.csv`](../output/tiny-scarab.csv)
- [`tiny-scarab.xml`](../output/tiny-scarab.xml)

Or you can just observe the table below:


| **Item** | **Qty** | **Reference(s)**                                                                                          | **Value** | **MPN**                | **Manufacturer**                    | **SPN**                   | **Supplier** |
|----------|---------|-----------------------------------------------------------------------------------------------------------|-----------|------------------------|-------------------------------------|---------------------------|--------------|
| 1        | 23      | C1, C2, C3, C4, C5, C6, C7, C8, C13, C14, C15, C19, C20, C21, C22, C23, C26, C27, C28, C29, C33, C34, C36 | 100n      | `GPC0402104-16`        |                                     |                           |              |
| 2        | 4       | C9, C11, C12, C16                                                                                         | 1u        | `GPC0402105-16`        |                                     |                           |              |
| 3        | 2       | C10, C17                                                                                                  | 10u       | `GPC0402106-6.3`       |                                     |                           |              |
| 4        | 9       | C18, C30, C31, C32, C35, C37, C38, C39, C40                                                               | 10u       | `GPC0805106`           |                                     |                           |              |
| 5        | 1       | D1                                                                                                        |           | `SMAJ5.0A`             | Littelfuse Inc.                     | `SMAJ5.0ALFTR-ND`         | DigiKey      |
| 6        | 1       | D2                                                                                                        |           | `SMAZ5V6-TP`           | Micro Commercial Co                 | `SMAZ5V6-TPMSTR-ND`       | DigiKey      |
| 7        | 2       | D3, D4                                                                                                    |           | `CDSOD323-T05LC`       | Bourns                              | `CDSOD323-T05LCTR-ND`     | DigiKey      |
| 8        | 1       | D5                                                                                                        |           | `SD103AWS`             | ANBON SEMICONDUCTOR (INT'L) LIMITED | `4530-SD103AWSTR-ND`      | DigiKey      |
| 9        | 1       | F1                                                                                                        |           | `SF-1206F100-2`        | Bourns Inc.                         | `SF-1206F100-2TR-ND`      | DigiKey      |
| 10       | 1       | F2                                                                                                        |           | `0402L050SLKR`         | Littelfuse Inc.                     | `F5759TR-ND`              | DigiKey      |
| 11       | 1       | J1                                                                                                        |           | `USB4110-GF-A`         | GCT                                 | `2073-USB4110-GF-A-2-ND`  | DigiKey      |
| 12       | 2       | J3, J4                                                                                                    |           | `10129383-914001ALF`   | Amphenol ICC (FCI)                  | `10129383-914001ALF-ND`   | DigiKey      |
| 13       | 4       | LED1, LED2, LED3, LED4                                                                                    |           | `150060GS55040`        | Wurth Elektronik                    | `732-12014-2-ND`          | DigiKey      |
| 14       | 3       | Q1, Q2, Q3                                                                                                |           | `IRLML2502TRPBF`       | Infineon Technologies               | `IRLML2502TRPBFTR-ND`     | DigiKey      |
| 15       | 2       | R1, R2                                                                                                    | 5k1       | `GPR04025K1`           |                                     |                           |              |
| 16       | 2       | R3, R25                                                                                                   | 200       | `GPR0402200R`          |                                     |                           |              |
| 17       | 2       | R4, R6                                                                                                    | 270       | `GPR0402270R`          |                                     |                           |              |
| 18       | 4       | R8, R17, R18, R19                                                                                         | 0         | `GPR04020R`            |                                     |                           |              |
| 19       | 3       | R10, R12, R24                                                                                             | 1k        | `GPR04021K`            |                                     |                           |              |
| 20       | 1       | R11                                                                                                       | 100k      | `GPR0402100K`          |                                     |                           |              |
| 21       | 1       | R13                                                                                                       | 130       | `GPR0402130R`          |                                     |                           |              |
| 22       | 1       | R14                                                                                                       | 20        | `GPR040220R`           |                                     |                           |              |
| 23       | 3       | R15, R16, R23                                                                                             | 10k       | `GPR040210K`           |                                     |                           |              |
| 24       | 1       | R22                                                                                                       | 470       | `GPR0402470R`          |                                     |                           |              |
| 25       | 4       | SW1, SW2, SW3, SW4                                                                                        |           | `PTS636 SL43 SMTR LFS` | C&K                                 | `CKN12309-2-ND`           | DigiKey      |
| 26       | 1       | SW5                                                                                                       |           | `SLW-883935-2A-D`      | CUI Devices                         | `2223-SLW-883935-2A-D-ND` | DigiKey      |
| 27       | 1       | U1                                                                                                        |           | `MCP1825ST-3302E/DB`   | Microchip Technology                | `MCP1825ST-3302E/DBTR-ND` | DigiKey      |
| 28       | 1       | U2                                                                                                        |           | `CH32V305FBP6`         | WCH                                 | `1005004329064488`        | AliExpress   |
| 29       | 1       | U3                                                                                                        |           | `CH32V003F4P6`         | WCH                                 | `1005005036714708`        | AliExpress   |
| 30       | 1       | XTAL1                                                                                                     |           | `FL1200156`            | Diodes Incorporated                 | `FL1200156-ND`            | DigiKey      |
| 31       | 1       | XTAL2                                                                                                     |           | `ECS-240-20-30B-TR`    | ECS Inc.                            | `XC1122TR-ND`             | DigiKey      |

&nbsp;<br>
<a href="../README.md#index"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7eef998b-278f-46d1-8f7c-8e4333ccd19c"> GO BACK</a>

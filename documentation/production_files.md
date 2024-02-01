<a href="../README.md"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/640d8577-87b5-481d-8511-f9ecea8db5e7"> HOME</a>

# Production Files

This board is designed with JLCPCB in mind for the production. That's why all components are selected to be in stock or at least accessible at <a href="https://jlcpcb.com/" target="_blank">JLCPCB</a>. In the schematic, you'll notice that each component has a `JLCPCB Part #` field:

<img width="800" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/a5225fb6-dbb8-4e13-b3ef-a879fd17de8c">

Based on this part number, JLCPCB knows which exact component to select from its stock. On this page, we cover how to output all the required production files from this KiCAD project for manufacturing the board at JLCPCB - both the board production and assembly.

> <img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/53f683d4-09b7-4b09-bea6-555c26a2688a"> Note: as you can see, not only the `JLCPCB Part #` field is provided for each component. We also added fields for other distributors, like `DigiKey`, `Farnell` and `Mouser`.


&nbsp;<br>
## 1. Install JLCPCB Plugin

First install the JLCPCB plugin in KiCAD:

<img width="800" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/dcd885ff-c29e-4df6-8e38-63975aa3dfd2">

Search for the `"JLC PCB Fabrication Toolkit"`:

<img width="500" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/602b6b75-8781-4c30-8689-d8f3f521a85e">

Install the plugin.

&nbsp;<br>
## 2. Generate Production Files

Once you've installed the JLCPCB plugin, you should see a new button in the PCB Layout Window:

<img width="500" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/ec97a4e5-2891-4716-9ab3-64f16c2dd888">




&nbsp;<br>
## 3. BOM

KiCAD outputs two BOM (Bill of Materials) files:

- [`tiny-scarab.csv`](../output/tiny-scarab.csv)
- [`tiny-scarab.xml`](../output/tiny-scarab.xml)

They can be generated in the KiCAD Schematic Editor by clicking `Tools` > `Generate BOM`:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/a2b37f38-c881-4602-8dc7-6ffaf24ca673">

KiCAD then generates these two BOM files in the toplevel folder. I moved them to the `output/` subfolder to keep the toplevel folder tidy.



&nbsp;<br>
<a href="../README.md#index"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7eef998b-278f-46d1-8f7c-8e4333ccd19c"> GO BACK</a>

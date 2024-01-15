<a href="../README.md"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/640d8577-87b5-481d-8511-f9ecea8db5e7"> HOME</a>

# A Deeper Dive in the KiCAD Files

All the files in this GitHub repository work together to create the entirety of the KiCAD project. Roughly speaking, these files can be grouped in four categories:

<img width="600" alt="open_project_01" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/c994d7d8-85a9-4e37-97d9-607ed6dfa8d6">

&nbsp;<br>
## <img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/9bca8022-6bff-431c-b7eb-bea506ce30f7"> KiCAD Component Library

KiCAD libraries come in two kinds: global and project libraries. Global libraries are available for each and every project you work on. Let's not mess with them. For the customized components, we created a project library. When you launch the Tiny Scarab project in KiCAD, the software should automatically recognize the presence of this project library and find all the components inside. To keep things simple, we decided to put all the customized components in this one project library.

The project library is stored in the file `Tiny_Scarab.kicad_sym`. Well, that is, all the schematic symbols are stored in there with their footprint *references*. The footprints themselves are located in the `Tiny_Scarab.pretty` folder. The 3D models from these footprints are in the `3d_models` folder.

Then what are `fp-lib-table` and `sym-lib-table` for? These files simply help KiCAD to know where to find the footprints and symbols from (one or more) project libraries. In our KiCAD project, it's pretty simple because there's only a single project library. But these two files come in handy if things would be more complicated.

&nbsp;<br>
## <img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/700a40ca-2f0f-42db-b38c-136012c5b887"> KiCAD Schematic Pages

The Tiny Scarab KiCAD project consists of three schematic pages. The root page is `tiny-scarab.kicad_sch` - it has the same name as the project file `tiny-scarab.kicad_pro` (which represents the entire project). Then there is the `USB.kicad_sch` page and `WCH-LinkE-R0-1v3.kicad_sch`. You can view these pages from within the Schematic Editor in KiCAD:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/f7df5988-e797-43f1-a00e-d72eee18f62c">

&nbsp;<br>
## <img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/1df25eac-82e7-4247-9bed-7e46277bb1cb"> KiCAD PCB Layout

The PCB Layout is stored in a single file: `tiny-scarab.kicad_pcb`.

&nbsp;<br>
## <img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/f06540f0-08be-4fc5-86cf-60528deadd96"> KiCAD Project

The entire KiCAD project is represented by `tiny-scarab.kicad_pro`. This file tells KiCAD how to open the project and where to find all the files.

&nbsp;<br>
<a href="../README.md"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7eef998b-278f-46d1-8f7c-8e4333ccd19c"> GO BACK</a>

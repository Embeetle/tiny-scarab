# Tiny Scarab

The Tiny Scarab is an open-source development board built around the popular 10 cent `CH32V003F4P6` RISC-V microcontroller from WCH. Using this dev board is uncomplicated: just plug it into your computer with a USB-C cable, and you're ready to code - the flasher/debugger is already embedded in the board for your convenience. Now you might wonder - why yet another dev board? Aren't there thousands already?

<img width="900" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/9c6070eb-ec15-4a7c-8f02-bf1a274b2bb3">

Well - this dev board is presented to you with a new coding IDE. Not satisfied with the current offering of IDEs for microcontrollers, we created a brand new one from scratch: <a href="https://embeetle.com/" target="_blank"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/e0cdd4a1-5d5b-47df-a8c9-bfc94e6a3e78" style="float:left"> Embeetle IDE</a>. With the Tiny Scarab and Embeetle IDE, you'll discover how smooth programming a microcontroller can be.

> <img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/677a9296-f9f8-4ee2-b77c-d166b05c937f" style="float:left"> This open-source dev board is developed in collaboration with the <a href="https://devheads.io/" target="_blank"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/80b0f2b4-92b5-459e-b805-48252bfecde0" style="float:left"> DevHeads</a> community. Please join the <a href="https://discord.gg/devheads">DevHeads Discord channel</a> if you want to know more about this Tiny Scarab board, Embeetle IDE or any other topic related to hardware and embedded software. We're waiting for you on the server!

&nbsp;<br>
# Overview

The Tiny Scarab is based on the 10-cent RISC-V `CH32V003F4P6` MCU from WCH:

<img width="100" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/c23c5a8a-db1b-4bea-a1cd-c7b025ab6012">

The Tiny Scarab board merges the <a href="https://embeetle.com/#supported-hardware/wch/probes/wch-linke-r0-1v3" target="_blank">`WCH-LinkE-R0-1v3`</a> flash/debug probe and the <a href="https://embeetle.com/#supported-hardware/wch/boards/ch32v003f4p6-evt-r0-1v1" target="_blank">`CH32V003F4P6-EVT-R0-1v1`</a> board into a single development board:

<img width="600" alt="comparison" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/590d21fe-cd38-49ad-960f-c5b6c0e88530">

There's no need to wire up anything. Just plug the Tiny Scarab's USB-C port in your computer, fire up Embeetle IDE and start coding!

&nbsp;<br>
# Index

- **Hardware**
  - [Download Tiny Scarab Schematic](tiny-scarab.pdf)
  - [Open Tiny Scarab in KiCAD](documentation/readme_open_project.md)
  - [A Deeper Dive in the KiCAD Files](documentation/readme_deeper_dive_kicad_files.md)
  - [Tiny Scarab Pinout and Features](documentation/readme_pinout_and_features.md)
  - [Tiny Scarab vs CH32V003F4P6-EVT-R0-1v1 - a Comparison](documentation/readme_compare.md)
  - [Production Files](documentation/production_files.md)

- **Software**
  - [Flash/Debug Probe Firmware](documentation/readme_flash_debug_probe_firmware.md)
  - [Target MCU Firmware](documentation/readme_target_mcu_firmware.md)

NOTES FOR MYSELF
================
Improvement points:
- Bulges in encasing don't fit board.
- Tag Connect needs a recess in the enclosure.
- Light bleeds between lightpipes. Lightpipes and LEDs too expensive.
- Graphical membrane needs 1.2mm edge.
- 3/5V indication on board is wrong. On graphical membrane it's correct.



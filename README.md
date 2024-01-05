# Tiny Scarab

## 1. Intro
The *Tiny Scarab* is a Beetle Board based on the 10-cent RISC-V `CH32V003F4P6` MCU from WCH:

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/4840a74b-d4f1-482b-b448-0be99c1800d8" width="100">

It's a merge of the <a href="https://embeetle.com/#supported-hardware/wch/probes/wch-linke-r0-1v3" target="_blank">`WCH-LinkE-R0-1v3`</a> flash/debug probe and the <a href="https://embeetle.com/#supported-hardware/wch/boards/ch32v003f4p6-evt-r0-1v1" target="_blank">`CH32V003F4P6-EVT-R0-1v1`</a> development board:

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/944e1196-e3e2-4832-a820-2a8ed98dba4c" height="200">

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/126dbb40-b49b-4934-9bd0-13f18f251917" height="200">

Resulting in this *Tiny Scarab* board:

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/7d400d2e-7ca1-4cbb-adb9-cae5566adc2b" width="400">

## 2. Comparison with `CH32V003F4P6-EVT-R0-1v1` board
The pinout is identical to the pinout from the `CH32V003F4P6-EVT-R0-1v1` development board:

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/d3f2d8d6-2687-4ef2-b670-73da3d5d2c28" width="400">

With a few exceptions:

- Pins `PA1` and `PA2` are used to drive the crystal. The `CH32V003F4P6-EVT-R0-1v1` board still breaks them out to the pin headers, but you then have to remove the crystal and solder two 0R resistors. We don't expect our users will make any modifications to the board, so we decided to leave out that option. The corresponing pins on the pin headers are just tied to `GND`.

- Pins `PD1`, `PD5`, `PD6` and `PD7` are connected to the `CH32V305FBP6` chip for flash and debug purposes (the `CH32V305FBP6` is the heart of the on-board `WCH-LinkE-R0-1v3` flash/debug probe). It is safer not to connect them to the pin headers.

## 3. Features
[UNDER CONSTRUCTION]

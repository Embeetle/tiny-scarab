# Tiny Scarab

<img src="https://github.com/Embeetle/tiny-scarab/assets/19362684/e0cdd4a1-5d5b-47df-a8c9-bfc94e6a3e78" width="100"> The **Tiny Scarab** is an open source hardware project launched by <a href="https://embeetle.com/" target="_blank">Embeetle</a> - the clean and efficient IDE for microcontroller programming. It's the first in the series of **Beetle Boards**. Expect more to show up in the months ahead.

The Beetle Boards will get special attention in Embeetle IDE. The're the perfect candidates to discover the capabilities of this IDE. Being open source, they're also a great option for your next hardware project.

## 1. Overview

The **Tiny Scarab** is based on the 10-cent RISC-V `CH32V003F4P6` MCU from WCH:

<img src="https://github.com/Embeetle/tiny-scarab/assets/19362684/c23c5a8a-db1b-4bea-a1cd-c7b025ab6012" width="150">

It's a merge of the <a href="https://embeetle.com/#supported-hardware/wch/probes/wch-linke-r0-1v3" target="_blank">`WCH-LinkE-R0-1v3`</a> flash/debug probe and the <a href="https://embeetle.com/#supported-hardware/wch/boards/ch32v003f4p6-evt-r0-1v1" target="_blank">`CH32V003F4P6-EVT-R0-1v1`</a> development board:

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/944e1196-e3e2-4832-a820-2a8ed98dba4c" height="200">

<img src="https://github.com/Embeetle/tiny-scarab/assets/152429714/126dbb40-b49b-4934-9bd0-13f18f251917" height="200">

This merge results in a very convenient development board that requires no external wires to get started. Just plug the **Tiny Scarab** in your computer with a USB-C cable and you're good to go:

<img src="https://github.com/Embeetle/tiny-scarab/assets/19362684/5433562a-a2f2-4a67-80d9-aade71c5e43a" width="400">

## 2. Comparison with `CH32V003F4P6-EVT-R0-1v1` board

With a few exceptions, the Tiny Scarab pinout is identical to the `CH32V003F4P6-EVT-R0-1v1` development board:

<img src="https://github.com/Embeetle/tiny-scarab/assets/19362684/9edd799f-8b77-4ab7-be1a-869cee57abe2" width="800">

The exceptions are:

- Pins `PA1` and `PA2` are used to drive the crystal. The `CH32V003F4P6-EVT-R0-1v1` board still breaks them out to the pin headers, but you then have to remove the crystal and solder two 0R resistors. We don't expect our users will make any modifications to the board, so we decided to leave out that option. The corresponing pins on the pin headers are just tied to `GND`.

- Pins `PD1`, `PD5`, `PD6` and `PD7` are connected to the `CH32V305FBP6` chip for flash and debug purposes (the `CH32V305FBP6` is the heart of the on-board `WCH-LinkE-R0-1v3` flash/debug probe). It is safer not to connect them to the pin headers.

## 3. Features
[UNDER CONSTRUCTION]

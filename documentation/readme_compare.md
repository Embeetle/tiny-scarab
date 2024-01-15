<a href="../README.md"><img width="24" alt="open_project_01" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/640d8577-87b5-481d-8511-f9ecea8db5e7"> HOME</a>

# Tiny Scarab vs CH32V003F4P6-EVT-R0-1v1 - a Comparison

With a few exceptions, the Tiny Scarab pinout is identical to the `CH32V003F4P6-EVT-R0-1v1` development board:

<img width="800" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/9edd799f-8b77-4ab7-be1a-869cee57abe2">

The exceptions are:

- Pins `PA1` and `PA2` are used to drive the crystal. The `CH32V003F4P6-EVT-R0-1v1` board still breaks them out to the pin headers, but you then have to remove the crystal and solder two 0R resistors. We don't expect our users will make any modifications to the board, so we decided to leave out that option. The corresponing pins on the pin headers are just tied to `GND`.

- Pins `PD1`, `PD5`, `PD6` and `PD7` are connected to the `CH32V305FBP6` chip for flash and debug purposes (the `CH32V305FBP6` is the heart of the on-board `WCH-LinkE-R0-1v3` flash/debug probe). It is safer not to connect them to the pin headers.

&nbsp;<br>
<a href="../README.md#index"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7eef998b-278f-46d1-8f7c-8e4333ccd19c"> GO BACK</a>

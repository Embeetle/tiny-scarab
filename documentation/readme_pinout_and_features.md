<a href="../README.md"><img width="24" alt="open_project_01" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/640d8577-87b5-481d-8511-f9ecea8db5e7"> HOME</a>

# Tiny Scarab Pinout and Features

## 1. Power System
The Tiny Scarab draws 5V power from its USB-C connector:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/102d7877-ca92-454d-8697-7cc354e7fe9e">

&nbsp;<br>
The 5V power rail is protected in several ways:

<img width="600" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/4c6e9073-f790-4b50-a72a-28b8e92c4c43">

Let's go over all the safety measures.

&nbsp;<br>
### 1.1 ESD Protection
TVS diode `TVS3` (`SMAJ5.0A`) protects the board from incoming voltage transients and ESD discharges on the 5V line:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/2f214e45-fc82-478a-8061-c67f315647aa">

&nbsp;<br>
### 1.2 Overvoltage Protection
The TVS diode is ideal for short voltage transients - like an ESD discharge. But what about permanent overvoltage incidents? What if a faulty USB-C charger outputs 20V on the `VBUS` line? In that case, fuse `F1` (`MFU0603FF02000P500`) cooperates with zener diode `D1` (`1SMA4734A`) to protect the board:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/19c6556a-60d2-4a9d-aa07-ea866fc4bcf9">

Sometimes a faulty USB-C charger can output 20V on the `VBUS` line, even though it never negotiated this with the device on the receiving end. It shouldn't happen ... but when it does you don't want the board to go up in flames! Zener diode `D1` has a zener voltage of 5V6, so it will draw a lot of current in this particular case. Fuse `F1` blows, interrupting the current flow to prevent further damage.

&nbsp;<br>
### 1.3 Overcurrent Protection
Chip `U1` (`AP2141WG-7`) limits the current flow to the whole board at 500mA. This limit ensures that any PC can drive the board risk-free:

<img width="600" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/6116bd5a-5b8a-49dc-8d34-6d2b544ee261">

There's already a 2A fuse on the 5V line. Why don't we remove this `U1` chip and just reduce the 2A fuse to 500mA?



> <img width="24" alt="open_project_01" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/409d84ec-fc51-49c5-b86b-5535085c416a">Fuse `F1` and current-limiting chip `U1` serve an entirely different purpose. Fuse `F1` (in collaboration with zener diode `D1`) protects the board from permanent overvoltage incidents. Replacing fuse `F1` with a 500mA version isn't a good idea because the on-resistance would be too high. Leaving out the fuse and only relying on current-limiting chip `U1` isn't smart either - a fuse is just perfect because of its simplicity and robustness. Summarized, the roles of fuse `F1` and chip `U1` are:
> - Fuse `F1`: simple and robust, ideal for the overvoltage incident described earlier.
> - Chip `U1`: more sophisticated, will limit current to 500mA while keeping a low on-resistance.


&nbsp;<br>
### 1.4 Power Indicator LEDs
The board has two LEDs to indicate the status of the 5V power input:

<img width="500" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/d83dc2fa-f977-4952-aeac-e5dbdb8ec1c3">

The `PWR` LED simply shows if 5V power is present on the board. The `ERR` LED lights up if the overcurrent protection chip `U1` reports a fault condition.

&nbsp;<br>
### 1.5 Voltage Conversion
Parts of the board - such as the flash/debug probe - operate on 3V3. So we need to create that voltage from the 5V rail:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/db1cfe7c-594a-42d0-9886-90b77e779c02">



&nbsp;<br>
That's because the flash/debug probe `CH32V305FBP6` MCU runs on 3V3. The target `CH32V003F4P6` MCU can run on both. The Tiny Scarab provides a switch to choose how you want to feed your target chip.

&nbsp;<br>
The switch is on the right side of the board:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/8229f6ea-ea41-497b-b088-8876300fb8c5">

## 2. Pinout

Almost all pins of the target `CH32V003F4P6` MCU are accessible through the pin headers at the bottom of the board:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/ed47ef23-bd5a-4d68-844b-f4df3d9bb480">

## 3. LEDs

[UNDER CONSTRUCTION]

## 4. Switches and Buttons

[UNDER CONSTRUCTION]


&nbsp;<br>
<a href="../README.md#index"><img width="24" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/7eef998b-278f-46d1-8f7c-8e4333ccd19c"> GO BACK</a>

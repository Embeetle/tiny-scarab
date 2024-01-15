

# Tiny Scarab Pinout and Features

## 1. Power System

The Tiny Scarab draws 5V power from its USB-C connector, fused at 1A:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/0c23efe4-9736-4a1d-8a5e-c0e16d7035b6">

Two zener diodes protect the 5V rail. `SMAJ5.0A` is a TVS diode to protect against incoming voltage transients. `SMAZ5V6-TP` is a zener diode to short permanent overvoltage (eg. a faulty USB-C charger outputs 20V) such that fuse `F1` will blow:

<img width="200" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/30390d9a-f192-4fb8-a330-97c635dd15dd">

`LED1` indicates if the board has 5V power:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/d6e32443-0e28-42ba-97ec-bb4f3912d161">


&nbsp;<br>
Eventually, the Tiny Scarab converts the 5V rail into 3V3:

<img width="300" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/1bf3f0da-04fe-481f-9b5f-a67c29f580a9">

&nbsp;<br>
That's because the flash/debug probe `CH32V305FBP6` MCU runs on 3V3. The target `CH32V003F4P6` MCU can run on both. The Tiny Scarab provides a switch to choose how you want to feed your target chip:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/a9cbcc63-ddaf-4cb2-9bc2-2f14425c3a62">

&nbsp;<br>
The switch is on the right side of the board:

<img width="400" src="https://github.com/Embeetle/tiny-scarab/assets/19362684/8229f6ea-ea41-497b-b088-8876300fb8c5">

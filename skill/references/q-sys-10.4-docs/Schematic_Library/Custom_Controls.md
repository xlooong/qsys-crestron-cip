# Custom Controls

> 来源: https://help.qsys.com/q-sys_10.4/#Schematic_Library/custom_controls.htm

The Custom Controls component allows you to create a component with various types of Controls that can be used to control other components through Control Pins.

- Only Control Pin Input and Output, no audio inputs/outputs
- Up to 10 different types (Groups) of controls
- Each Group can have up to 32 controls
- Each Group can have a different count

## Properties

| Property | Description |
|----------|-------------|
| Type | Selects control type for the Group. Up to 10 Groups. |
| Count | 1 to 32 controls per Group |
| Default Range Message | Default range for specific Control type |
| Customize Range | Yes/No - customize min/max |
| Minimum | Custom minimum range |
| Maximum | Custom maximum range |

## Available Control Types and Ranges

| Type | Default Range | Custom Min | Custom Max |
|------|--------------|------------|------------|
| Distance knob (meters) | 0 to 100 | 0 | 999 |
| Frequency knob (Hz) | 20 to 20000 | 0.1 | 20000 |
| Generic float knob | 0 to 1 | -1,000,000,000 | 1,000,000,000 |
| Generic integer knob | 0 to 1 | -16,777,216 | 16,777,216 |
| Hexadecimal knob | 0x0 to FFFFFF | 0 | 8 bits (24) |
| LED | Off / On | — | — |
| Level fader w/taper (dBFS) | -100 to 10 | — | — |
| Level knob (dBFS) | -100 to 20 | -100 | 100 |
| Meter (dB) | -100 to 20 | — | — |
| Momentary button | Off / On | — | — |
| Mute button (Toggle) | Off / On | — | — |
| Pan knob | -1 to 1 | — | — |
| Percent knob (%) | 0 to 100 | 0 | 100 |
| Position knob | 0 to 1 | — | — |
| Status Display | 0=OK, 1=Compromised, 2=Fault, 3=Not Present, 4=Missing, 5=Initializing | — | — |
| Text display | — | — | — |
| Text edit | — | — | — |
| Time knob | 0 to 86,399 | 0 | 86,399 |
| Time knob (seconds) | 0 to 1 | 0 | 86,400 |
| Toggle button | Off / On | — | — |
| Trigger button (single pulse) | Off / On | — | — |

## Control Pins

For each Control Type, Input and Output Control Pins are supplied. Key pin behaviors:

| Pin Name | Value | String | Position | Direction |
|----------|-------|--------|----------|-----------|
| Generic integer knob | 0/1 | 0 or 1 | 0/1 | Input/Output |
| LED | 0/1 | false/true | 0/1 | Input/Output |
| Momentary button | 0/1 | false/true | 0/1 | Input/Output |
| Toggle button | 0/1 | false/true | 0/1 | Input/Output |
| Trigger button | — | — | — | Input/Output |
| Text display | 1 | text | 1 | Input/Output |
| Text edit | 2 | text | 2 | Input/Output |
| Percent knob | 0 to 1 | — | 0 to 1 | Input/Output |

## Troubleshooting

Components such as Crossover, Text Controller, or Custom Controls (Integer Knobs, Hexadecimal Knobs) will NOT be recalled by Snapshot if the Ramp Time is a non-zero number.

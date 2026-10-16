# GPS Info
> 来源: https://help.qsys.com/Content/Schematic_Library/gps_info.htm

The GPS Info component displays various information received from connected GPS receiver hardware. Most often this hardware is used in conjunction with the Loop Player to synchronize audio playback between systems. This information is transmitted to the Core over RS-232 in NMEA 0183 format.

> **Note:** All information may not be available depending on the features and configuration of the specific GPS hardware.

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## GPS Info Properties

This component has no configurable properties .

## Controls

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

- OK (0)
- Compromised (1)
- Fault (2)
- Not Present (3) Is Required Dynamically Paired Is Required Dynamic Pairing
- Unknown (3)
- Missing (4)
- Initializing (5)

### UTC

Displays current UTC time in HH;MM;SS format.

### Date

Displays the current UTC date. Reads as Day , Month , Year .

### Latitude

Latitude read by GPS in the form of 37° 41' 22.68" N.

### Longitude

Longitude read by GPS. In the form 106° 55' 22.30" W.

### Speed

Speed read by GPS.

### Course

Course read by GPS.

### Satellite Count

Current number of satellites GPS is locked to.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| Course | Float (text) | Input / Output |  |  |
| Day | Integer (text) | Input / Output |  |  |
| Latitude | String : n° n' n.nn" N\|S | Output |  |  |
| Longitude | String : n° n' n.nn" W\|E | Output |  |  |
| Month | Integer (text) | Input / Output |  |  |
| Satellite Count | Integer (text) | Input / Output |  |  |
| Speed | Float (text) | Input / Output |  |  |
| Status | 0 1 2 3 4 5 | OK (Green) Compromised (Orange) Fault (Red) Not Present (Gray) Missing (Red) Initializing (Blue) | - | Output |
| UTC | Time Control (text) | Input / Output |  |  |
| Year | Integer (20XX - i.e. 23 for 2023) | Input / Output |  |  |


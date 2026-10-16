# Astronomical Clock
> 来源: https://help.qsys.com/Content/Schematic_Library/sun.htm

Use the Astronomical Clock component to determine your location's latitude and longitude, and then trigger events based on that location's sunrise, sunset, or solar noon.

> **Note:** The component uses https://sunrise-sunset.org/api to obtain astronomical data for your location. An internet connection is required.

## Configuration Overview

1. Drag the Astronomical Clock component into your schematic.
2. Tip: You can also expose the 'Is Day' control pin, which provides a boolean value of whether the current time is after sunrise and before sunset. This may be simpler than using conditional logic with sunrise and sunset times.
3. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
4. Get

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, the Astronomical Clock component is configured to trigger Audio Player playback based on the sunrise and sunset times for a set location. When sunrise occurs, playback begins. When sunset occurs, playback stops.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Astronomical Clock Properties

This component has no configurable properties.

## Controls

> **Note:** The component refreshes its state every minute, so it can take up to 59 seconds to reflect a change.

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

- OK (0)
- Compromised (1)
- Fault (2)
- Not Present (3) Is Required Dynamically Paired Is Required Dynamic Pairing
- Unknown (3)
- Missing (4)
- Initializing (5)

### Latitude and Longitude

Indicates the latitude and longitude, in Degrees Minutes Seconds (DMS) format, obtained using the Get button. Or, you can manually enter values in decimal format. (Manually-entered decimal values are converted to DMS format.)

### Sunrise

Text indicator of the sunrise time, as determined by the location coordinates.

### Sunset

Text indicator of the sunset time, as determined by the location coordinates.

### Solar Noon

Text indicator of the solar noon time, as determined by the location coordinates.

### Day Length

Text indicator of the hours, minutes, and seconds in the daytime period, as determined by the location coordinates.

### Daytime

Boolean indicator of whether the current time is between the sunrise and sunset times.

### Get

Click to obtain the latitude and longitude of your system's location, based on IP address.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| Solar Noon Trigger | (trigger) | Output |  |  |
| Sunrise Trigger | (trigger) | Output |  |  |
| Sunset Trigger | (trigger) | Output |  |  |
| Day Length | – | hh : mm : ss | – | Input / Output |
| Get | (trigger) | Input / Output |  |  |
| Is Day | 0 1 | false true | – | Output |
| Latitude | – | Input : [-] nnn . nnnnn Output : nnn ° nn ' nn . nn " N\|S | – | Input / Output |
| Longitude | – | Input : [-] nnn . nnnnn Output : nnn ° nn ' nn . nn " W\|E | – | Input / Output |
| Solar Noon | – | hh : mm : ss AM\|PM | – | Input / Output |
| Sunrise Time | – | hh : mm : ss AM\|PM | – | Input / Output |
| Sunset Time | – | hh : mm : ss AM\|PM | – | Input / Output |


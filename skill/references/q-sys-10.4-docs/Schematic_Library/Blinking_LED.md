# Blinking LED
> 来源: https://help.qsys.com/Content/Schematic_Library/blinker.htm

The Blinking LED is a component that you can use to visually monitor the status of a Core or I/O Frame. When you set the Properties of the Blinking LED, you assign it to a Core or an I/O Frame. If the Core or I/O Frame should go off line for any reason, the LED stops blinking. You can also use the Blinking LED to provide a square wave input to a script. A Period control is available to control the blink rate, or the frequency of the square wave, measured in seconds rather than Hz.

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, we are using the Blinking LED Component visually monitor the signal to a third party Projector.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Blinking LED Properties

### Assign Component To

Selects which item this Blinking LED is to be assigned to.

### Network ID 1

If the I/O Frame is selected, enter the Network Id, not the IP address. This is done to prevent issues if the network is using DHCP.

1. Available only when "Assign Component to" is set to I/O Frame.

## Controls

### LED

Blinks at the rate set by the Period control.

### Period (seconds)

Sets the blink rate of the LED.

### Duty Cycle (percent)

Sets the percentage of the period where the pulse is positive, or on. Duty Cycle can be set from 10% to 90%.

The ratio between the pulse duration and the period of a rectangular waveform expressed as a percentage.

### Enable

Enables blinking on the LED.

### Random

Set a random Duty Cycle of the LED.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| LED | 0 1 | false true | 0 1 | Output |
| Period | 0.100 to 10 | 100 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Duty Cycle | 10 to 90 | - | 0.010 to 9.0 | Input / Output |
| Random | 0 1 | disable enable | 0 1 | Input / Output |


# Signal Snakes
> 来源: https://help.qsys.com/Content/Schematic_Library/signal_snakes.htm

Signal Snakes provide the means to reduce a set of signals to a single graphical wire or named signal, similar to wrapping a number of wires into a bundle. Signal Snakes are comprised of two components: a Signal Snake Input , and a Signal Snake Output . Signal Snakes can have from 1 to 256 channels, and the signal types of those channels can be mixed.

## Inputs and Outputs

Signal Snake pins are unique; they change based on the type of pin to which they are connected.

> **Tip:** The number of signal pins is variable and set in the component's Channel Count Property.

## Schematic Examples

## Example 1: Using Signal Snakes

These Signal Snakes were created by dragging out the Signal Snake Input and Signal Snake Output components.

## Example 2: Using Component Pins

These Signal Snakes were created from selecting component pins.

## Example 3: Using Mixers

These Signal Snakes were created by wiring the Mixer's pins to the Signal Snake pins and then connecting the Snakes.

## Creating Signal Snakes

1. Select one or more pins on one or more components.
2. Click one of the pins and begin dragging away from the component.
3. Press the space bar. The Signal Snake is created.

OR

1. Signal Snake Input Signal Snake Output
2. Manually wire the Signal Snakes to and from the desired components.

Or, you can copy and paste Signal Snakes.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Signal Snake Properties

### Channel Count

Signal Snakes can have from 1 to 256 channels, and the signal types of those channels can be mixed. The default number is 8.

## Controls

This component has no configurable controls.

## Control Pins

This component has no control pins.

## Troubleshooting

## Using Signal Snakes Inside Containers

As you copy and paste the Signal Names to the input / output they belong, the Signal Name will enumerate to prevent multiple connections on the same input / output.

> **Tip:** When copying and pasting a Signal Name to any input/ output inside of a Container, be sure to use the correct Signal Name to the correct input / output.


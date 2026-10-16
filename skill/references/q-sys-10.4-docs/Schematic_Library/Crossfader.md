# Crossfader
> 来源: https://help.qsys.com/Content/Schematic_Library/crossfader.htm

The Crossfader component allows you to fade between two input channels going to one output. You can specify a mono Crossfader, having two inputs and one output, a Stereo Crossfader, having four inputs and two outputs, or a Multi-channel Crossfader. The number of inputs is always double the number of outputs.

You manually trigger the fade from Input A to Input B, and back. You can control the time it takes to fade from one channel to another. All of the inputs and outputs (Mono, Stereo, and Multi-channel) on a single Crossfader component are controlled simultaneously.

## Inputs and Outputs

> **Note:** The number of signal pins is variable and set in the component's Type Property.

## Input Pins

### Input

Audio signal pins are represented by a ( ) circle, and traditional wiring is represented by a thin black line.

By default, the Crossfader component is set to a Mono channel, which provides 2 inputs. Additionally, you can set the Properties to allow for Stereo , which gives you 4 inputs (Right and Left for each input); or you can choose Multi-Channel , which will allow you to choose between 2 and 256 inputs and outputs.

## Output Pins

### Output

Audio signal pins are represented by a ( ) circle, and traditional wiring is represented by a thin black line.

By default, the Crossfader component is set to a Mono channel, which provides 1 output. Additionally, you can set the Properties to allow for Stereo , which gives you 2 outputs (Right and Left); or you can choose Multi-Channel , which will allow you to choose between 2 and 256 inputs and outputs.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Crossfader Properties

## Channels

### Type

Selects the range for the number of inputs.

### Count

Only available if the Type Property is Set to Multi-Channel . Selects the number of inputs for Multi-Channel.

## Controls

## Crossfader

### Gain A and B (dB)

Displays the current gain value for each channel. During a crossfade operation, one value is increasing, the other decreasing.

### Position (percentage)

Displays the positional balance between Input A and Input B .

Zero percent (0%) the output is equal to Input A .

One hundred (100%) the output is equal to Input B .

### Xfade to A and B

Radio style buttons that start the crossfade operation. If the Position reading is at 0%, the Xfade to A button is on, or true and Channel A is going to the output.

If the Position reading is at 100%, the Xfade to B button is on, or true and Channel B is going to the output.

You can click either button to start the crossfade operation.

## Configure

### Time (seconds)

The Time controls the length of time it takes the Crossfader to fade from one channel to the other.

### Type

The Type control allows selection of the crossfade type: -6 dB constant gain or -3 dB constant power .

With -6 dB constant gain type selected, the Crossfader sums the input signals with a constant combined gain. The midpoint gain is -6dB. This setting is suited for correlated input signals but results in a 3 dB dip at the midpoint for uncorrelated signals.

With -3 dB constant power type selected, the Crossfader sums the input signals to a constant combined power. The midpoint gain is -3dB. This setting is suited for uncorrelated input signals and is the preferred one.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| Crossfade Time | 0.010 to 10 | 10 ms to 100 s | 0.000 to 1.00 | Input / Output |
| Crossfade To A 1 | 0 1 | false true | 0 1 | Input / Output |
| Crossfade To B 1 | 0 1 | false true | 0 1 | Input / Output |
| Crossfade Type | 1.00 2.00 | -6 dB Constant Gain -3 dB Constant Gain | 0 1 | Input / Output |
| Current Gain A | -100 to 20 | -100 dB to 20 dB | 0.000 1.000 | Output |
| Current Gain B | -100 to 20 | -100 dB to 20 dB | 0.000 1.000 | Output |
| Position | 0 to 100 | — | 0.000 1.000 | Output |

1. Crossfade to A and Crossfade to B are always the opposite Value, String, and Position of each other.

## Troubleshooting

There are some components that are unique in their operation in the Emulate mode. Some of these components are the Audio Player , Crossfader , Gain Ramp , and Listen buttons. For more information, see Limitations .


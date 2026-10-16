# Text Controller
> 来源: https://help.qsys.com/Content/Schematic_Library/device_controller_script.htm

Use the Text Controller component to easily declare one or more custom controls and then build the Lua script associated with those controls using a Lua text editor.

## Configuration Overview

1. In your schematic, double-click the Text Controller component to open the elements editor.
2. Controls
3. Properties Text Controller
4. Save changes
5. Run (F5) or emulate (F6) your design to start the script.
6. n

> **Note:** If there are no Panels configured, then the "Controls" tab is shown.

> **Tip:** The ‘Edit’ and ‘Add Panel’ buttons are next to the component name for easier access, even with large scripts. The ‘Close’ button stays on the right, but you can double-click the header to close it quickly.

To see an example configuration, see Example .

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Text Controller Properties

### User Panel Lock

When the property is set to no (Default), a Panel can be deleted by clicking on the X in the Panel tab.

When the property is set to yes , A lock icon appears on the Panel tab preventing any changes within or the option to delete the active Panel.

### Display User Panel

> **Note:** If there are no Panels, then the "Controls" tab is shown.

The dropdown will provide Panel 1- n , depending on how many you have set up. Whichever Panel you choose in this dropdown will be displayed by default when opening the Text Controller.

### Start Automatically

When the property is set to no , the script will not start when entering emulation or loading a design to a core.

When the property is set to yes (Default), the script will start when entering emulation mode or when loading a design to a core.

## Using the Elements Editor

Double-click the Text controller component to open the elements editor, which is where you define controls for your Lua script. After defining controls, click to open the Lua text editor.

## Controls

### Controls

- Select one or more control icons and drag or copy/paste them into your schematic or user control interface. (Use the Ctrl key to select multiple controls.)

### Serial Port Inputs

Specify how many serial port input pins to expose, from 0 to 128. Use these pins with the SerialPorts Lua library.

### Virtual Serial Port Outputs

Specify how many virtual serial port output pins to expose, from 0 to 128. Use these pins with the SerialServerPorts Lua library.

## Controls Properties

### General Properties

### Name

Specify a name for the input.

### Count

Specify the number of controls of the specified type to create.

### Control Type

### Category

## Button

Select a Push Action :

- Momentary
- Toggle
- Trigger
- State Trigger State Trigger

## Knob

Specify a Max Value and Min Value for the specified Units :

- dB
- Hz
- Float
- Integer
- Pan Note: The Pan range is ignored when setting the Pan value. When setting a pan control value in the Block Controller control panel, the valid range is L100 to 0 (or C) to R100. In the Blocks Editor, the valid range is -1 to 1, where -1 is the equivalent of 'L100', 0 is the equivalent of 'C', and 1 is the equivalent of 'R100'. For example, a value of -0.5 is L50, and a value of 0.5 is R50.
- Percent
- Position
- Seconds

## Indicator

Specify a Type : LED, Meter, Text, Status.

## Text

Specify a Type : Text Box, Combo Box, List Box

### Control Pin

Expose pins for these controls: None, Input (pins on the left), Output (pins on the right), or Both.

## Using the Script Editor

> **Tip:** While in the Script area, press F1 for help on the Lua scripting language.

The script editor contains these areas:

- Text editor – Write script for your configuration. You can edit the script in the Design, Emulate, or Run modes, but any errors are only detected in the Run or Emulate modes.
- Information bar at the top of the script – Click the yellow "Save changes" bar to reload (not run) the script. Syntax errors are indicated in a red bar at top-right, as well as in the Debug Output area.
- Search bar – Click the Search bar on the right side of the page to locate or replace text in your script. As a shortcut, press F3 to find the next item.

Platform-level horizontal scrolling is supported here to navigate layouts that extend beyond the visible workspace. You can scroll horizontally using any of the following input methods:

- Touchpad Gestures: Use side-to-side (two finger swipes on supported trackpads.
- Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
- Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
- Scroll Bar: Use mouse or arrow keys to drag the bar.

## Rules for Referencing Control Names in Script

- Control names that contain no spaces can be referenced with dotted notation. Examples: 'Button' could be referenced 'Controls.Button.Boolean'; Names with spaces: 'Big Button' = 'Controls["Big Button"].Boolean'
- 'Controls.MyKnob.Value'
- 'Controls.MyKnobs[1].Value', 'Controls.MyKnobs[2].Value', 'Controls.MyKnob[3].Value'
- 'Controls["My Knobs"][1].Value', 'Controls["My Knobs"][2].Value'

## Debug Output

See Debug Output .

## Control Pins

The available Control Pins depend on settings in Properties .

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| Code | (text) Allows you to enter code. | Input / Output |  |  |
| Script Start | (trigger) Starts the script running. | Input / Output |  |  |
| Script Status | (text) Current status of the script. | Output |  |  |
| Script Stop | (trigger) Stops the script. | Input / Output |  |  |

## Example

In this simple example, Text Controller is configured with a control button that can be used to retrieve a list of control names from any named component in the design.

## Naming components

This example contains two audio components - Gain and Delay. Rename each with a custom name ("MyGain", "MyDelay"). Renaming the components with custom names allows the Named Components function to retrieve a table of control names for those components. For more information about named components in Lua, see Component .

## Defining controls

Drag Text Controller onto the canvas and double-click it to open the elements editor. Add three controls with these names and properties:

- Get Controls – A trigger button that retrieves a table of control names for the specified component custom name. (Category = Button; Push Action = Trigger)
- Component Name – A text box for entering the custom name of a component. (Category = Text; Type = Text Box)
- Output – A text box to contain the returned table of control names. (Category = Text; Type = Text Box)

## Adding Lua script

Click to open the Lua text editor. Add the following script, and then click Save changes .


```
Controls[
"Component Name"
].EventHandler = 
function
(ctl)

comp = Component.New(ctl.String)

end

-- Returns all controls of the component in "Component Name"

Controls[
"Get Controls"
].EventHandler = 
function
()

local
 str = 
" Get Controls for "
..Controls[
"Component Name"
].String..
"\r"

for
 k,v 
in
 
pairs
(comp) 
do

str = str..k..
"\r"

end

Controls.Output.String = str

end

comp = Component.New(Controls[
"Component Name"
].String)
```

## Running the script

1. Emulate (F6) or run (F5) the design to start the script.
2. Click the schematic page tab ("Page 1" if you didn't rename it).
3. In the Component Name text box, type the name of one of the custom control names - MyGain - and then press Enter.
4. Get Controls
5. The Output text box shows the list of controls for that component name. Repeat the process for MyDelay to see how the output changes.

## Reference and Training

- Control Scripting Lua 5.3 Reference Manual
- Q-SYS Training - Control 101 Learn the basic Q-SYS third party control principles, including Lua scripting basics.

## Troubleshooting

## Using Components with Snapshot Controller Ramp Time

Components such as the Crossover Component or other Text Controller or Custom Controls like the Integer Knobs, and Hexadecimal Knobs will not be recalled by Snapshot if the Ramp Time is a non-zero number.

## LED State Retention

In a text controller, if you use a script to set the state of an LED, then disconnect and emulate again, the LED always starts in the ‘off' status. This is normal as an LED is an indicator. Indicators such as LED, Status, Text Indicators, and Meters reset their state to the default anytime the script restarts unless they are wired to another control and can get their state from the wired logic.

## UCI Layer Name Retrieval

When using a script to obtain the names of the layers on a UCI from a UCI Layer Controller component, it is recommended to avoid using underscores (“_” ) in the layer names. This ensures that the name returned matches the actual layer name, preventing any potential discrepancies.

## Text Controller settings not mirrored on Backup Core

Currently, scripts are only executed on the active Core, and not on the standby Core. Additionally, read-only controls are not synchronized between the Cores.


# Control Script

> 来源: https://help.qsys.com/q-sys_10.4/#Schematic_Library/control_script_2.htm

The Control Script component is used to write scripts, using the Lua language, for control and monitoring from within Q-SYS Designer. You can change or monitor the position, value, string, metadata and other attributes of controls. The script you write interacts with components through their control pins.

## Using the Control Script

The Control Script component is defined, in the component Properties, by the number of inputs and outputs. The body of the script is written in the Control Script Control Panel.

### About script compatibility
If you open a Q-SYS 3.3 or earlier design containing a Control Script component in Q-SYS 4.0 or later, the component will become a Control Script v1 component. The existing v1 script will continue to function. However, if the v1 script is pasted into a newly placed Control Script component, it will most likely fail. A v1 script can be converted to v2 by adding a property to use the New Script Engine (Yes/No).

## Properties

| Property | Description |
|----------|-------------|
| Input Count | Sets the number of inputs |
| Serial Input Count | Sets the number of serial connections |
| Output Count | Sets the number of outputs |
| Virtual Serial Output Count | Sets the number of virtual serial output pins (use with SerialServerPorts) |
| Start Automatically | When no, script will not start on emulation/load. Default yes. |

## Controls

- **Script Area**: Text-edit area to write script. Editable in Design, Emulate, or Run modes.
- **Top Bar**: Click "Save changes" to reload script. Syntax errors indicated in red bar.

## Control Pins

| Pin Name | Value | String | Position | Direction |
|----------|-------|--------|----------|-----------|
| Code | (text) | Allows you to enter code | — | Input/Output |
| Script Start | (trigger) | Starts the script running | — | Input/Output |
| Script Status | (text) | Current status of the script | — | Output |
| Script Stop | (trigger) | Stops the script | — | Input/Output |

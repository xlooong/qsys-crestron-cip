# Event Logger
> 来源: https://help.qsys.com/Content/Schematic_Library/event_logger.htm

Use the Event Logger component to place custom event messages – with a specified severity – into the Q-SYS Core's event log. Log entries can optionally include argument strings from the control pins of other design components.

## Configuration Overview

1. Drag the Event Logger component into your schematic.
2. Properties
3. If you want to include argument strings in the log message: Wire a component's output control pin to an Arg input control pin on the Event Logger component. Repeat for additional arguments.
  
  - Wire a component's output control pin to an Arg input control pin on the Event Logger component.
  - Repeat for additional arguments.
4. Run your design.
5. Double-click the Event Logger component to open the control panel.
6. Controls
7. Publish

Your log entry and any arguments are placed in the Q-SYS Core's event log, which is viewable from the Q-SYS Core Manager > Event Log .

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, a log entry containing a Gain component's current Gain value and Mute status is published to the Q-SYS Core's Event Log.

## Q-SYS Designer

## Q-SYS Core Manager > Event Log

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Event Logger Properties

### Arg Count

Select how many arguments to optionally include in your log entry, from 0 to 16.

## Controls

### Log Entry

Type the text to appear in the log entry. Use curly braces {} to optionally insert argument strings, which are placed into the log entry in numerical order - Arg 1, Arg 2, etc. Argument values are received from connected output control pins of other components.

## Example

If your Log Entry text is:

This is my log message, which contains {}, {}, and {}.

...your message would include argument strings from Arg 1, Arg 2, and Arg 3, in that order.

### Severity

Select a severity to associate with the log entry: default (normal), error , or warning .

### Publish

Click to publish this log entry to the Event Log.

### Arg 1 - 16

These text boxes indicate what strings are being received for each argument from connected component control pins.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| Arg n | (text) | Input / Output |  |  |
| Log Entry | (text) | Input / Output |  |  |
| Severity | - | default error warning | - | Input / Output |
| Publish | (trigger) | Input / Output |  |  |


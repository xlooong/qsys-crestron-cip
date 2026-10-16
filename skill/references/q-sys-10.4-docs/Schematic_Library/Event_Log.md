# Event Log
> 来源: https://help.qsys.com/Content/Schematic_Library/event_log.htm

The Event Log component displays the last item added to the event log. The information displayed is: date/time, severity, category, and message. You can use the Event log to send this information to a Lua Script. For the complete Event Log, refer to the Q-SYS Core Manager Event Log topic.

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, we are using a Status Combiner to verify the status of both our Amplifier and our Core. If the Status Combiner shows a fault in the status, a Momentary Button will trigger an outgoing E-mailer . However, first, it will go through a delay, long enough to capture the Last Entry of the Event Log , and then e-mail that information.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Event Log Properties

This component has no configurable properties.

## Controls

### Last Entry

Text field displaying the last Event Log entry. The field is updated every time there is an entry to the Event Log.

## Control Pins

| Pin Name | String | Pins Available |
|---|---|---|
| Last Entry | Text field containing the last Event Log entry. 2011-07-22T13:02:33 Normal Connect Accepted connection 10.10.200.200 | Output |
| Lua Table | Text field containing the last Event Log entry in the Lua table format. return { date="2011-07-22T13:02:58", severity="Normal", category="Connect", message="Accepted connection 10.10.200.200" } | Output |


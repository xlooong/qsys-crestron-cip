# Selector
> 来源: https://help.qsys.com/Content/Schematic_Library/selector.htm

The Selector component makes it easy to switch between a number of configured values to send to a downstream component. Configure a group of control buttons and assign a value or text string to send when a button is pushed on. One button from the group can be active at a time.

> **Note:** The selector component will, when the design starts, select the current selection, which could, depending on what comes after create an undesirable effect.

## Configuration Overview

1. Drag the Selector component into your schematic.
2. Properties
3. Connect the Selector component's Value control pin to the input control pin of another component.
4. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
5. Controls
6. Click a selection button (or, use the Selection combo box to select an assigned Label) to enable the selected control and send its assigned value to the connected component.

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, the Selector component is configured to set the gain value in the Gain component. The user can easily switch between the set gain values by either pressing a Selection button or selecting a label from the combo box.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Selector Properties

### Selection Count

Specify the number of control buttons. Can choose between 2 and 64 counts.

## Controls

### Selection

This will show 1- n depending on how many you specify for the Selection Count property.

### Label

Specify a text label for the Selection number.

### Output

Specify a text label for the Value number.

### Sel

Click a button to turn on a Selection. (Or, use the combo box to select an assigned Label.)

### Selection (combo box)

In Run or Emulate modes, select an assigned Label to turn on a Selection.

### Output (text box)

In Run or Emulate modes, shows the Value currently being sent.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| Label 1- n | (user-defined) | Input / Output |  |  |
| Output 1 | (user-defined) | Output |  |  |
| Output 1- n | (user-defined) | Input / Output |  |  |
| Selector 2 | (text) | Input / Output |  |  |
| Selector 1- n | 0 1 | false true | – | Input / Output |

1. The Output pin is always shown. It shows the “Output” String for the selected option. It will show an empty string if nothing is selected).

2. The “Selector” pin outputs a JSON text string indicating the selected option.


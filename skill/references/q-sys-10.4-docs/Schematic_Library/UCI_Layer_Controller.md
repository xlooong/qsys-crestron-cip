# UCI Layer Controller
> 来源: https://help.qsys.com/Content/Schematic_Library/uci_layer_controller.htm

Use the UCI Layer Controller to show or hide individual layers in a specified UCI and page.

## Configuration Overview

1. Drag the UCI Layer Controller component into your schematic.
2. Properties
3. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
4. In your schematic, double-click the component to open its control panel.
5. Controls
6. Click a layer's Show button to show or hide the layer in the UCI.

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, there are three UCI layers installed. Any of these layers can be transitioned on or off the screen by choosing the Transition type.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## UCI Layer Controller Properties

### UCI

Select a UCI name.

### Page

If Is Shared is set to 'No':

Select a page name to control the visibility of layers within that page.

### Is Shared

Select 'No' to control the visibility of standard layers in a selected Page.

Select 'Yes' to control the visibility of Shared Layers in the selected UCI name.

For information about adding layers to a UCI, see User Control Interface (UCI) Design Overview .

## Controls

### Transition (combo box)

Assign a transition type for the layer name.

### Show (button)

Click the button to show or hide the layer.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| layer name : Transition | N/A | left right top bottom fade none | N/A | Input / Output |
| layer name : Visibility | 0 1 | false true | – | Input / Output |

## Troubleshooting

## UCI Layer Name Retrieval

When using a script to obtain the names of the layers on a UCI from a UCI Layer Controller component, it is recommended to avoid using underscores (“_” ) in the layer names. This ensures that the name returned matches the actual layer name, preventing any potential discrepancies.


# Contact List
> 来源: https://help.qsys.com/Content/Schematic_Library/contact_list.htm

The Contact List component allows you to access contact lists that have been set up in Core Manager . After selecting a Contact List, you can select or search for the contact you want to call. To dial a selected number, expose the Number control pin and wire it to the Call Control > Dial String control pin of the Status/Control (Softphone) .

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, we have exposed the Number Control Pin on the Contact List as well as the Control Dial Control Pin on the Status Softphone component. With the connection made between them, we can create a UCI that will dial specific contacts at the press of a button.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## Contact List Properties

There are no configurable properties for this component.

## Controls

### Contact Lists

When a Contact List is established in the Q-SYS Core Manager > Telephony > Contacts page, it displays in this field. A contact list is comprised of one or more contacts.

### Search

Searches in the selected Contact List.

Select the search field and type the name for which you want to search. All items meeting the criteria display. Items not meeting the criteria are not displayed.

### Names

The names of the Contacts in the selected Contact List.

### Number

Displays the number associated with the selected Contact.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| List (Selected Contact List) | – | Text | – | Input / Output |
| Names (Selected Name) | – | Text | – | Input / Output |
| Number (Number of Selected Name) | – | Text | – | Output |
| Search (String typed in Search field after Dial is clicked) | – | Text | – | Input / Output |


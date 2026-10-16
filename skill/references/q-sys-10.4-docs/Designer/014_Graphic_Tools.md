# Graphic Tools
> 来源: https://help.qsys.com/Content/Q-SYS_Designer/014_Graphic_Tools.htm

Use the Graphic Tools to organize, label, annotate, and enhance the appearance of your design or User Control Interface (UCI) layout.

## Text Block Tool Use the Text Block tool to add a text box to your design or UCI. You can adjust the style of both the text itself and the surrounding box.

## Adding a Text Block

1. Click and drag within the schematic to draw the Text Block.
2. Type your desired text. To edit the text later, double-click it.
3. In the Properties pane, Set the Graphic Properties and Text Style.

## Graphic Properties

### Position

Set the horizontal and vertical coordinates of the Text Block location within the schematic. The values auto-adjust when you click and drag the Text Block, but you can also manually specify the values.

### Size

Set the horizontal and vertical size of the Text Block. The values auto-adjust when you click and drag to re-size the Text Block, but you can also manually specify the values.

### Fill

Click the Fill field to set the Text Block's background color and transparency, or use the eyedropper to click an item within the schematic with the desired color. By default, the Text Block is transparent.

### Corner Radius

Select how much corner rounding is applied to the Text Block, from 0 to 300. The higher the value, the more rounding is applied.

You can also adjust the corner radius for Text Boxes, Group Boxes, and controls using the corner radius handle.

## Show Me

Your browser does not support the video tag.

### Stroke Color

This is the color of the Text Block border. Click the Stoke Color field to select a color and set the transparency, or use the eyedropper to click an item within the schematic with the desired color.

### Stroke Width

This is the width of the Text Block border, from 0 to 64.

## Text Style

### Text Color

Click the Text Color field to set the text color and transparency, or use the eyedropper to click an item within the schematic with the desired color.

### Size

Set the pixel size of the text, from 6 to 2,048 (default is 12).

### Font

Set the font for the text (default is Roboto).

### Font Style

Set the font's weight, slant, etc. The available styles are determined by the selected Font.

### Horizontal Alignment

Set how the text aligns in relation to the left and right borders: Center (default), Left , Right .

### Vertical Alignment

Set how the text aligns in relation to the top and bottom borders: Center (default), Bottom , Top .

## Header Tool Use the Header tool to add a title to an area of your design.

## Adding a Header

1. Click and drag within the schematic to draw the Header.
2. Type your desired Header text. To edit the text later, double-click it.
3. In the Properties pane, Set the Graphic Properties and Text Style.

## Graphic Properties

### Position

Set the horizontal and vertical coordinates of the Header location within the schematic. The values auto-adjust when you click and drag the Header, but you can also manually specify the values.

### Size

Set the horizontal and vertical size of the Header. The values auto-adjust when you click and drag to re-size the Header, but you can also manually specify the values.

### Fill

Click the Fill field to set the Header's color and transparency, or use the eyedropper to click an item within the schematic with the desired color. The Fill sets the color for both the horizontal rule and text.

## Text Style

### Size

Set the pixel size of the text, from 6 to 2,048 (default is 12).

### Font

Set the font for the text (default is Roboto).

### Font Style

Set the font's weight, slant, etc. The available styles are determined by the selected Font.

### Horizontal Alignment

Set how the text aligns in relation to the left and right borders: Center (default), Left , Right .

## Group Box Tool Use the Group Box tool to visually group objects within a Q-SYS design or UCI.

## Adding a Group Box

1. Click and drag within the schematic to draw the Group Box.
2. Optionally, start typing to add a text label for the Group Box. To edit the text later, double-click it.
3. In the Properties pane, Set the Graphic Properties and Text Style.
4. User Control Interface (UCI) Design Overview

## Example 1

## Example 2

> **Note:** A Group Box and the items within it are not linked. To move a Group Box and its items, you must select them all.

## Graphic Properties

### Position

Set the horizontal and vertical coordinates of the Group Box location within the schematic. The values auto-adjust when you click and drag the Group Box, but you can also manually specify the values.

### Size

Set the horizontal and vertical size of the Group Box. The values auto-adjust when you click and drag to re-size the Group Box, but you can also manually specify the values.

### Fill

Click the Fill field to set the Group Box background color and transparency, or use the eyedropper to click an item within the schematic with the desired color. By default, the Group Box is transparent.

### Corner Radius

Select how much corner rounding is applied to the Group Box, from 0 to 300. The higher the value, the more rounding is applied.

You can also adjust the corner radius for Text Blocks, Group Boxes, and controls using the corner radius handle.

## Show Me

Your browser does not support the video tag.

### Stroke Color

This is the color of the Group Box border. Click the Stoke Color field to select a color and set the transparency, or use the eyedropper to click an item within the schematic with the desired color.

### Stroke Width

This is the width of the Group Box border, from 0 to 64.

## Text Style

### Text Color

Click the Text Color field to set the text color and transparency, or use the eyedropper to click an item within the schematic with the desired color.

### Size

Set the pixel size of the text, from 6 to 2,048 (default is 12).

### Font

Set the font for the text (default is Roboto).

### Font Style

Set the font's weight, slant, etc. The available styles are determined by the selected Font.

### Horizontal Alignment

Set how the text aligns in relation to the left and right borders: Center (default), Left , Right .

## Polygon Tool Use the Polygon tool to create a shape and assign a control to it. Clicking a Polygon changes the state of the control.

## Adding a Polygon

1. Tip: You can add points (or nodes) to a finished Polygon. Click and drag from any point on a line segment to create a new node.
2. Optionally, add text to the Polygon. Click the Polygon, and then begin typing. To edit the text later, double-click it.
3. In the Properties pane, set the Graphic Properties.

## Tip: Avoid placing polygons above buttons

Because polygons are actually bounded by a hidden rectangle, avoid placing a polygon (and its rectangular boundary) above a button, as that portion of the button cannot be interacted with in a UCI. In this example, the areas of each button marked with an 'X' are dead zones.

## Assigning a Control to a Polygon

1. Create a Polygon in your design or UCI.
2. Set the Region Properties for the polygon. These settings determine the style and action of the assigned control.
3. Drag a control from a control panel onto the shape while holding the Ctrl button.
4. Release the mouse button. The control is assigned to the shape.

## Example

In this example, the treble clef is assigned to the Play button of the Audio Player. If it was in a design or UCI, clicking the treble clef sign would start playing the selected file.

## Region Properties

### Button Style

Sets the style of button:

- Momentary
- Off
- On
- String
- Toggle

### Button String

Available when Button Style is set to 'String'. The string you enter is case sensitive and must be valid for the control in the Control Panel. For example a fader control has a range of -100 to 20, the string must be numeric and within that range, a toggle button must be true/false, On / Off, or 1/0.

## Special string commands

In addition, the following special commands may be used in the String field:

- ++ moves the control plus 1 minor division
- -- moves the control minus 1 minor division
- n n
- n n
- n
- max moves the control to its maximum value.
- min moves the control to its minimum value.

### Reverse Action

Changes the direction of the control.

For example, set Reverse Action to 'Yes' if you want to change a mute button (on state is muted, off is passing audio) to an enable button (on state is passing audio, off state is muted).

## Graphic Properties

### Position

Set the horizontal and vertical coordinates of the Polygon location within the schematic. The values auto-adjust when you click and drag the Polygon, but you can also manually specify the values.

### Size

Set the horizontal and vertical size of the Polygon. The values auto-adjust when you click and drag to re-size the Polygon, but you can also manually specify the values.

### Fill

Click the Fill field to set the Polygon's background color and transparency, or use the eyedropper to click an item within the schematic with the desired color. If you have assigned a control to the Polygon, the Fill color is the "on" state color for controls with binary states.

### Off Color

If you have assigned a control to the Polygon, this is the color for the "off" state for controls with binary states. When the Off Color is linked to the Fill color, the Off Color is automatically assigned. When unlinked , you can manually adjust the color.

### Stroke Color

This is the color of the Polygon border. Click the Stoke Color field to select a color and set the transparency, or use the eyedropper to click an item within the schematic with the desired color.

### Stroke Width

This is the width of the Polygon border, from 0 to 64.


# Inventory
> 来源: https://help.qsys.com/Content/Schematic_Library/inventory.htm

The Inventory section, in the left-side pane, displays a list of hardware items to use in your system. In a new design, the Inventory list is populated with only a Q-SYS Core processor. You must add the other items that match your physical inventory. Each inventory item contains at least one component that can be placed into the schematic, configured, and connected to other components as needed.

## Add Single Item to the Inventory

1. Inventory
2. Select the tab for the equipment type you want to add.
3. Click the item to add to the Inventory.

For configuration details, refer to the item's individual help topic (select item and press F1).

## Batch-Add Items to the Inventory

1. Inventory
2. Select the tab for the equipment type you want to add.
3. Ctrl
4. Quantity
5. Add

> **Note:** When naming your item, use only letters (a-z), numbers (0-9) or hyphens (-).

> **Note:** There is a 255 device limit for a single bulk addition.

## Handling Auto-Increment and Base Name Suffixes

### Generating Sequential Names with a Suffix

Scenario: You want to create multiple QIO-L4o devices with sequentially numbered names, such as QIO-L4o-1, QIO-L4o-2, QIO-L4o-3, QIO-L4o-4.

Configuration Steps

- In the Base Name field, enter:

`QIO-L4o-${padding=1;start=1;increment=1}`

- In the Quantity field , set the number of devices you want (e.g., 4).

Result

This will generate :

- QIO-L4o-1
- QIO-L4o-2
- QIO-L4o-3
- QIO-L4o-4

### Generating Names without a Suffix

Scenario: You want to generate a base name without any suffix (just QIO-L4o). All generated names will automatically include a numeric suffix (e.g., -1). To remove the suffix, you will need to edit the names manually after creation.

Configuration Steps

- In the Base Name field, enter:

`QIO-L4o-1-${padding=1;start=1;increment=1}`

- Generates QIO-L4o-1.

- Manually delete the “-1”.

### Generating Names without the Suffix

Scenario: You want to create multiple QIO-L4o devices and start numbering from a specific value.

Configuration Steps

- In the Base Name field, enter:

`QIO-L4o-1-${padding=1;start=1;increment=1}, which yields QIO-L4o-1.`

- In the Quantity field , set the number of devices you want (e.g., 3).

Result

This will generate :

- QIO-L4o-5
- QIO-L4o-6
- QIO-L4o-7

### Duplicate Handling

If some names already exist (e.g., QIO-L4o-1, QIO-L4o-2, QIO-L4o-5), the system will:

- Skip existing names.
- Fill in the next available numbers (e.g., QIO-L4o-3, QIO-L4o-4, QIO-L4o-6, etc.).

Example

Existing names:

- QIO-L4o-1
- QIO-L4o-2
- QIO-L4o-5

Adding three more devices will result in:

- QIO-L4o-3 (fills the gap)
- QIO-L4o-4 (fills the next gap)
- QIO-L4o-6 (next available after 5)

## Create New Locations for Inventory Items

You can create virtual Locations based on physical location, or what ever you want.

For example, a Location could be an equipment room, or a specific rack in the equipment room. Another example would be one Location for all the equipment used for a specific purpose. Items are in the "Default Location" when you add them to the Inventory list.

- Select an item (in the Inventory list, or the Schematic) and type a new Location name in the Properties of that item.
- This new Location is now available to select for other Inventory items.

## Filter the Inventory List

1. Inventory
2. Select a Type from the drop-down list. Only the selected type of Inventory items display.
3. filter

## Group the Inventory List

Click the double braces { } to cycle through the groupings, or use the drop-down list and choose a grouping option:

- Group by Type
- Group by Location
- Group by Q-SYS Reflect
- Group by Status


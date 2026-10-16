# Notifications

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Notifications.htm

Use the following methods to subscribe to a notification, publish a notification with specified data, and unsubscribe from a notification. This allows scripts running within the same Core to communicate with each other using control wiring or Component.

## Methods

| Method | Arguments | Description |
|--------|-----------|-------------|
| noteid = Notifications.Subscribe() | name, function | Subscribe to a notification with a given name. noteid: The token to use when unsubscribing. name: The name of the notification. function: The callback to call when the named notification is triggered. Signature: function(name, data). |
| Notifications.Publish() | name, data | Publish a named notification with given data. The data can be either a Lua table or a string. Note: You cannot call Notifications.Publish() inside a Notifications.Subscribe() callback. |
| Notifications.Unsubscribe() | noteid | Unsubscribe from a notification with the specified noteid. |

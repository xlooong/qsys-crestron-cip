# Q-SYS Lua Notifications API
> 来源: https://help.qsys.com/DeveloperHelp/Content/Standards_Definitions/Notifications_API.htm

A standardized command API for Q-SYS plugins using the Notification system. This system allows publishing commands to a device type or named channel without hard-coded knowledge of what is in the design. Devices can be addressed by type or by channel (if compliant). Reporting for discovery is optional and not required. Use Publish to keep multiple plugins on the same informational set.

> **Note:** This API may be extended. The standard presented here is the intended format for compliance and interoperability. Adding fields is allowed, but additional data for expanded use cases may be ignored by systems implementing the basic case.

## Addressing Notifications

To use this notification API, join the appropriate Notifications channel using the Notifications object in Q-SYS Lua. The Notification channel name will be Type.Subchannel

| Name | Pattern | Example |
|---|---|---|
| Type | Type | "Display" |
| Subchannel [optional] | Type.Subchannel | "Display.UpperConf" |

Type identifies the device family. Use reserved Reflect types (see Reserved Notification Names ). These predefined types ensure cross compatibility. This standard may be applied to custom names and types, but the target use case is for compliant systems to use the Reflect type to standardize Notifications.

subchannel [Optional] Is a secondary identifier. Add Channels logically to the design, and use this API to address all matching instances at once. For example, room, zone, floor, or IP address can be used as logical groups. A device may subscribe to multiple channels simultaneously (e.g., Display.UpperConf, Display.2ndFloor, and Display.192.168.1.10). A Channel may be a single instance or many. The Type should address all of that type of device.

## Message Format

Every notification conforming to this API contains a Lua table. Only name is required. The messages have the following fields:

| Name | Required? | description |
|---|---|---|
| name | yes | Name of the command this message |
| data | no | Data for this message |
| direction | no | Type of message for this message; "set", "publish" or "query" allowed |
| id | yes | Unique Id of the sender of this message; Use SCRIPT_NAME of the sending script. |

Example document:


```
{

  name      = 
"PowerOn"
,  
-- required, string

  data      = 
nil
,        
-- optional payload, all Lua data types allowed

  direction = 
"set"
,      
-- optional; defaults to "set" type, string

  id        = SCRIPT_NAME 
-- required, unique identifier for this message source, string. Use SCRIPT_NAME

}
```

Direction Types:

| direction | description |
|---|---|
| "set" or empty | command — receiving device should act on this |
| "publish" | unsolicited state update; informational only |
| "query" | information request; supporting members should respond in the channel with a publish |

Unknown fields should be silently ignored.

## Discovery

Compliant plugins may participate in the announcement channel for cross discovery. These messages identify the capabilities of devices using this system. The "system.announce" channel is used for presence and capability advertisement.

## system.announce — Announcement

Devices publish presence after a 2-second startup delay. The packet describes the type, subscribed channels, and supported command names:


```
Notifications.Publish(
"system.announce"
, {

  name      = 
"announce"
,

  data      = {

    
type
      = 
"Display"
,                                             
-- String

    channels  = {
"Display"
, 
"Display.UpperConf"
, 
"Display.2ndFloor"
},  
-- Array of strings

    commands  = {
"PowerOn"
, 
"PowerOff"
, 
"InputSet"
, 
"Volume"
},         
-- Array of strings

  },

  direction = 
"publish"
,

  id        = SCRIPT_NAME

})
```

## system.announce — WhoIsThere query

A plugin that starts after the announce window (or needs to rediscover) publishes a "query" to system.announce. All compliant sources that subscribe to system.announce re-announce after a short random delay to avoid a broadcast stampede.


```
-- Any plugin can send this to trigger re-announcement from all sources

Notifications.Publish(
"system.announce"
, {

  name      = 
"announce"
,

  direction = 
"query"
,

  id        = SCRIPT_NAME

})
```

Sources respond after a random delay (0–1 s) to prevent a broadcast stampede. The General Framework Start() handles this automatically. Avoid querying this channel to minimize spamming the interface. Members of channels will rarely change, and compliant members will announce when they join or depart a channel.

## system.announce — Depart

Published to system.announce immediately when a plugin leaves a channel. Best-effort — Q-SYS Lua can be halted out of band and this message may not be emitted in all shutdown paths. One message may list multiple channels.


```
Notifications.Publish(
"system.announce"
, {

  name      = 
"depart"
,

  channels  = {
"Display.UpperConf"
},

  direction = 
"publish"
,

  id        = SCRIPT_NAME

})
```

## Use Case Examples

## Send Behaviors

Send a command by publishing to a type or channel address. Omitting direction means the receiver should act.


```
-- command to all devices of a type

Notifications.Publish(
"Display"
, { name = 
"PowerOn"
, id = SCRIPT_NAME })

-- command to one channel

Notifications.Publish(
"Display.UpperConf"
, { name = 
"Volume"
, data = 
75
, , id = SCRIPT_NAME })
```

## Receive Behaviors

Create a subscription to listen for commands from any source.


```
function
 
ReceiveHandler
(notificationName, data)

  
print
(
"Received "
 .. data.name .. 
" command on "
 .. notificationName)

  
if
 data.name == 
"PowerOn"
 
and
 (data.direction == 
nil
 
or
 data.direction == 
"set"
) 
then

    DisplayPowerOn()  
-- Local function to operate on the message

  
end

end

mySubscription = Notifications.Subscribe(
"Display"
, ReceiveHandler)

myConferenceRoomSubscription = Notifications.Subscribe(
"Display.UpperConf"
, ReceiveHandler)
```

## Query Behaviors

Create a query request for a channel. Devices may or may not respond; query support is optional.


```
function
 
ReceiveHandler
(notificationName, data)

  
print
(
"Received "
 .. data.name .. 
" command on "
 .. notificationName)

  
if
 data.name == 
"Power"
 
and
 data.direction == 
"publish"
 
then

    
-- data.data will contain the response.  Many devices may respond.  How useful this is will be situationally dependent.  The response will arrive asynchronously.

  
end

end

mySubscription = Notifications.Subscribe(
"Display"
, ReceiveHandler)

-- query for power state to all devices of a type

Notifications.Publish(
"Display"
, { name = 
"Power"
, direction = 
"query"
, id = SCRIPT_NAME })
```

Responses will be received on the channel sent asynchronously.

## Publish Behaviors

Respond to query messages.


```
function
 
ReceiveHandler
(notificationName, data)

  
print
(
"Received "
 .. data.name .. 
" command on "
 .. notificationName)

  
if
 data.direction == 
"query"
 
and
 data.name == 
"Power"
 
then

    
-- Emit the response from a timer callback.  Notification eventhandlers are blocked from emitting Notifications for stability.

    Timer.CallAfter(
function
() 

      Notifications.Publish(notificationName, { name = data.name, direction = 
"publish"
, data = Controls[
"Power"
].Value, id = SCRIPT_NAME })

    
end
, 
0.01
)

  
end

end

mySubscription = Notifications.Subscribe(
"Display"
, ReceiveHandler)
```

## Announcement Behaviors

Use the system.announce channel to provide information on this instance's presence to listening channel members.

Send a Query:


```
-- Any plugin can send this to trigger re-announcement from all sources

Notifications.Publish(
"system.announce"
, {

  name      = 
"announce"
,

  direction = 
"query"
,

  id        = SCRIPT_NAME

})
```

Sending an Announcement:


```
function
 
AnnounceCapabilities
()

  Notifications.Publish(
"system.announce"
, {

    name      = 
"announce"
,

    data      = {

      
type
      = 
"Display"
,

      channels  = {
"Display"
, 
"Display.UpperConf"
, 
"Display.2ndFloor"
},  
--Channels currently subscribed to

      commands  = {
"PowerOn"
, 
"PowerOff"
, 
"InputSet"
, 
"Volume"
},  
-- Capabilities of this instance
 

    },

    direction = 
"publish"
,

    id        = SCRIPT_NAME

  })

end

AnnounceCapabilities()
```

Handling Announcements:


```
DisplaysAvailable = 
false

function
 
AnnouncementHandler
(notificationName, data)

  
print
(
"Received "
 .. data.name .. 
" command on "
 .. notificationName)

  
if
 data.direction == 
"query"
 
and
 data.name == 
"announce"
 
then

    Timer.CallAfter(AnnounceCapabilities, 
math
.
random
())  
-- 0-1s random jitter prevents stampede

  
elseif
 data.direction == 
"publish"
 
and
 data.name == 
"announce"
 
then

    DisplaysAvailable = 
true

  
end

end

announcementSubscription = Notifications.Subscribe(
"system.announce"
, AnnouncementHandler)
```

Departing a channel:

This message will identify when this instance is withdrawing from a channel to the system.announce.


```
Notifications.Publish(
"system.announce"
, {

  name      = 
"depart"
,

  channels  = {
"Display.UpperConf"
},

  direction = 
"publish"
,

  id        = SCRIPT_NAME

})
```

## General Framework

A flat, single-instance object. Populate Commands and Listeners, then call Start(). Commands can be changed at any time; the next announce will reflect the current state. This listener is designed to provide announcements and respond to set commands.


```
json = 
require
(
'rapidjson'
)

local
 Notifier = {

  Id               = SCRIPT_NAME, 
-- Insert a unique identifier to identify messages from this instance

  Type             = 
"Display"
,   
-- device family; see DeviceTypes.md

  Verbose          = 
false
,       
-- log all send/receive/announce events when true

  Announcing       = 
true
,        
-- set false to suppress all announce/depart messages

  Commands         = {},          
-- ["CommandName"] = function(Data)

  Listeners        = {},          
-- ["ChannelName"] = subscription token (nil before Start)

  AnnounceListener = 
nil
,         
-- subscription token for system.announce queries

  AnnounceHandler  = 
nil
,         
-- subscription token for system.announce responses: function(data)

}

Notifier.Handler = 
function
(notificationName, data)

  
if
 
type
(data) ~= 
"table"
 
then
 
return
 
end

  
if
 Notifier.Verbose 
then

    
print
(
string
.
format
(
"Notifier Rx: %s name=%s direction=%s\n%s"
, notificationName, 
tostring
(data.name), 
tostring
(data.direction 
or
 
"set"
), json.encode(data.data)))

  
end

  
if
 data.direction == 
"publish"
 
then

    
-- Add handling of published data (informational messages from channel members) here if used. This is outside the scope of this example

    
return

  
elseif
 data.direction == 
"query"
 
then

    
-- Add code to handle data requests here.
 

    
-- Timer.CallAfter(function() Notifier.Send(notificationName, ResponseData) end, 0.1)

    
return

  
end

  
local
 handler = Notifier.Commands[data.name]

  
if
 handler 
then
 handler(data.data) 
end

end

Notifier.Send = 
function
(address, message)

  
if
 Notifier.Verbose 
then

    
print
(
string
.
format
(
"Notifier Tx: %s name=%s"
, address, 
tostring
(
type
(message) == 
"table"
 
and
 message.name 
or
 message)))

  
end

  message.id = Notifier.Id

  Notifications.Publish(address, message)

end

Notifier.AddCommand = 
function
(name, func)

  
if
 Notifier.Verbose 
then

    
print
(
"Notifier adding: "
..name)

  
end

  Notifier.Commands[name] = func

end

-- *** Optional Announce (cross discovery) system ***

-- builds commands[] from Commands keys at call time so announced commands stay current

Notifier.Announce = 
function
(channelName)

  
if
 
not
 Notifier.Announcing 
then
 
return
 
end

  
local
 message = {

    name      = 
"announce"
,

    data      = {

      
type
         = Notifier.Type,

      id           = Notifier.Id,

      channels     = {},

      commands     = {},

    },

    direction = 
"publish"
,

  }

  
for
 CommandName 
in
 
pairs
(Notifier.Commands) 
do
 

    
table
.
insert
(message.data.commands, CommandName) 

  
end

  
for
 name,_ 
in
 
pairs
(Notifier.Listeners) 
do

    
if
 Notifier.Listeners[name] ~= 
-1
 
then

      
table
.
insert
(message.data.channels, name)

    
end

  
end

  
if
 Notifier.Verbose 
then
 
print
(
"Notifier Announce: "
 .. Notifier.Type) 
end

  Timer.CallAfter(
function
() 
Notifier.Send
("system.announce", message) 
end
 , 1+
math.random
())

end

Notifier.Depart = 
function
(channelName)

  
if
 Notifier.Verbose 
then
 
print
(
"Notifier Depart: "
 .. channelName) 
end

  
if
 Notifier.Listeners[channelName] == 
-1
 
then

    
return

  
end

  
if
 Notifier.Announcing 
then

    Notifier.Send(
"system.announce"
, {

      name = 
"depart"
, 

      channels = {channelName}, 

      direction = 
"publish"

    })

  
end

  Notifications.Unsubscribe(Notifier.Listeners[channelName])

  Notifier.Listeners[channelName] = 
-1

end

Notifier.Join = 
function
(channelName)

  
if
 channelName == 
nil
 
or
 channelName == 
""
 
then

    channelName = Notifier.Type

  
elseif
 channelName:
sub
(
0
, #Notifier.Type) ~= Notifier.Type 
then

    channelName = Notifier.Type .. 
"."
 .. channelName

  
end

  
if
 Notifier.Listeners[channelName] 
then

    Notifier.Depart(channelName)

  
end

  
if
 Notifier.Verbose 
then
 
print
(
"Notifier Join: "
 .. channelName) 
end

  Notifier.Listeners[channelName] = Notifications.Subscribe(channelName, Notifier.Handler)

  Notifier.Announce(channelName)

end

-- Start defined listeners

Notifier.Start = 
function
()

  
if
 Notifier.Listeners[Notifier.Type] 
then
 Notifier.Stop() 
end

  
if
 Notifier.Verbose 
then
 
print
(
"Notifier Start()"
) 
end

  
local
 shouldAnnounce = Notifier.Announcing

  Notifier.Announcing = 
false

  Notifier.Join()  
-- subscribe to bare Type channel

  
if
 shouldAnnounce 
then

    Notifier.AnnounceListener = Notifications.Subscribe(
"system.announce"
, 
function
(_, data)

      
if
 
type
(data) == 
"table"
 
then

        
if
 data.direction == 
"query"
 
then

          Timer.CallAfter(Notifier.Announce, 
0.5
 * 
math
.
random
())

        
elseif
 data.direction == 
"publish"
 
and
 Notifier.AnnounceHandler 
then

          Notifier.AnnounceHandler(data)

        
end
  

      
end

    
end
)

    
for
 channelName 
in
 
pairs
(Notifier.Listeners) 
do

      
if
 channelName ~= Notifier.Type 
then

        Notifier.Join(channelName)

      
end

    
end

    Notifier.Announcing = 
true

    Notifier.Announce()

  
else

    
for
 channelName 
in
 
pairs
(Notifier.Listeners) 
do

      
if
 channelName ~= Notifier.Type 
then

        Notifier.Join(channelName)

      
end

    
end

  
end

end

-- Stop all listeners

Notifier.Stop = 
function
()

  
if
 Notifier.Verbose 
then
 
print
(
"Notifier Stop()"
) 
end

  
for
 name,_ 
in
 
pairs
(Notifier.Listeners) 
do

    Notifier.Depart(name)

  
end

  
if
 Notifier.Announcing 
then

    Notifier.Send(
"system.announce"
, { name = 
"depart"
, data = { 
type
 = Notifier.Type }, direction = 
"publish"
 })

  
end

  
if
 Notifier.AnnounceListener 
then
 

    Notifications.Unsubscribe(Notifier.AnnounceListener)

    Notifier.AnnounceListener = 
nil

  
end

end

Notifier.SetType = 
function
(newType)

  
local
 oldType = Notifier.Type

  
local
 remappedListeners = {}

  Notifier.Stop()

  
for
 channelName 
in
 
pairs
(Notifier.Listeners) 
do

    
local
 channelSuffix = channelName:
match
(
"^"
 .. oldType .. 
"(%..*)$"
)

    
if
 channelSuffix ~= 
nil
 
then

      
table
.
insert
(remappedListeners, { oldName = channelName, newName = newType .. channelSuffix })

    
end

  
end

  Notifier.Listeners[oldType] = 
nil

  
for
 _, listener 
in
 
ipairs
(remappedListeners) 
do

    Notifier.Listeners[listener.oldName] = 
nil

    Notifier.Listeners[listener.newName] = 
-1

  
end

  Notifier.Type = newType

  Notifier.Start()

end
```

Initializing the Notifier framework:


```
function
 
Initialization
()

  Notifier.Type    = 
"Display"

  Notifier.Verbose = 
true

  
-- Populate the supported list of commands with handlers

  Notifier.Commands[
"PowerOn"
]   = 
function
(_) 
Controls.Power.Boolean
 = 
true
 
end

  Notifier.Commands[
"PowerOff"
]  = 
function
(_) 
Controls.Power.Boolean
 = 
false
 
end

  Notifier.Commands[
"Volume"
]    = 
function
(Data) 
Controls.Volume.Value
 = 
tonumber
(Data) 
end

  Notifier.AnnounceHandler = AnnouncementReceiverFunction    
-- Optional function to handle announcements

  Notifier.Start()

  Notifier.Join(
"UpperConf"
)   
-- will subscribe to Display.UpperConf on Start()

  Notifier.Join(
"2ndFloor"
)

end
```

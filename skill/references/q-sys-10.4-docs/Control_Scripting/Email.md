# Email

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Email.htm

Similar to the E-mailer component, the Email library allows creation of emails directly from a Lua script.

Note: Messages can be a maximum of 16 KB in size.

## Email.Send

Send an email using specified parameters.

Syntax: `Email.Send(table)`

### Table Parameters

| Parameter | Type |
|-----------|------|
| From | string |
| Subject | string |
| Body | string |
| To | array of strings |
| CC | array of strings |
| Server | string |
| Username | string |
| Password | string |
| EventHandler | function to call with status, signature is 'function(table, error)' |

Note: The Email library always attempts to use Secure Sockets Layer (SSL), if available. If a 'Username' is not specified, it will be taken from the 'From' field.

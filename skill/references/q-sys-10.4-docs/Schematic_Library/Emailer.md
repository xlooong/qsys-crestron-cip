# E-mailer
> 来源: https://help.qsys.com/Content/Schematic_Library/email.htm

Use the E-mailer component to send a message to a valid e-mail address or valid mobile phone address. You can use the E-mailer with Control Scripting to send messages when specified events take place, or use the E-mailer for routine communication. If someone replies to a message sent from Q-SYS, the reply is sent to the "From" address specified in the Configure section of the Control Panel.

## Requirements

- You must be in the Run Mode to send email. If you enter any information in the Emulate mode, it remains in the E-mailer when you go to the Run mode. E-mailer supports only one outgoing e-mail at a time.
- Messages can be a maximum of 16 KB in size.

## Inputs and Outputs

## Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from Control Scripts . Control Pin signal pins are represented by a square, and the wiring is represented by a thick blue / white line.

## Schematic Example

In this example, we are using a Status Combiner to verify the status of both our Amplifier and our Core. If the Status Combiner shows a fault in the status, a Momentary Button will trigger an outgoing E-mailer. However, first, it will go through a delay, long enough to capture the Last Entry of the Event Log , and then e-mail that information.

## Properties

> **Tip:** For additional properties that are not listed, refer to the Properties Panel help topic for more information.

## E-mailer Properties

This component has no configurable properties.

## Controls

The controls listed below are divided into sections to match the Control Panel sections.

## E-mailer

### Send

Momentary button to send the e-mail.

### To

Must be a valid e-mail address. Multiple addresses can be entered, separated by a semicolon, comma, or space. Check with the carrier for the Mobile Phone to determine the format of the e-mail address you would use to send e-mail to the phone; each carrier is different.

### Subject

Must contain some text.

### Message

Must contain some text.

### Status

Sending - Yellow

Send Succeed - Green

Error 1 - Red

1. Errors can include: (parenthesis are explanations)

- 'To' field is empty (must contain valid e-mail address)
- 'To' field is malformed (must be valid e-mail address format)
- 'Subject' field is empty (must contain some text)
- 'Message' field is empty (must contain some text)
- 'From' field is empty (must contain some text)
- from address
- Cannot send e-mail while emulating (must be in Run mode)
- IP address

## Configure

### From

Must be a valid e-mail address.

If the e-mail was undeliverable, the failure return e-mail goes to this address, not the Core. If the person to whom the e-mail was sent replies to your email, the reply goes to this email address.

### Password

If a password is required by the e-mail server, enter it in this field.

### Server

IP address of the outgoing SMTP (Simple Mail Transfer Protocol) mail server from which the email will be sent. Do not use a server name unless the core is configured to use DHCP and the DHCP server provides a name server address, then the Sever field can contain the name of the outgoing SMTP mail server rather than the IP address. For more information, see Configuring SMTP Servers .

> **Tip:** You can search the Internet for the server name, e.g. hotmail outgoing mail server , then in a command prompt window ping the server name to get the IP address.

### Server Requires Secure Sockets Layer (SSL)

If you are using a mail service that requires SSL, click this button to enable SSL. If the mail server operates on a non-standard port (it might), you must append a colon followed by the port number to the IP address.

Some organizations with their own mail servers may not require SSL for access within the company. In this case, do not use the SSL option.

## Configuring SMTP Servers

As email providers have increased security requirements for 3rd party clients, Q-SYS allows you to customize the port used for outgoing connections.

> **Note:** Nearly all services and organizations require two-factor authentication. To take advantage of SMTP configuration in QSD, you must first have two-factor authentication enabled on your email account, otherwise you will receive an error that the email could not be sent.

## Gmail

Once a Gmail account has been created and two-factor authentication is enabled, an App Password is required to be configured.

1. Create a Gmail third-party email client
2. Gmail: Create and use App Passwords
3. Open the E-mailer component in QSD and Save to Core & Run (or press F5).
4. Fill out the necessary To, Subject, Message, and From fields.
5. Enter the App Password provided by Google.
6. Either of the following examples can be used for outgoing Server addresses:
  
  - smtp.gmail.com:587
  - smtps://smtp.gmail.com:465
7. Ensure that Server Requires Secure Sockets (SSL) is highlighted.
8. Press Send and the email will be sent.

## Example

## Outlook

Once an Outlook email account has been created and two-factor authentication is enabled, an App Password is required to be configured.

1. Create an Outlook third-party email client
2. Outlook: Create and use App Passwords
3. Open the E-mailer component in QSD and Save to Core & Run (or press F5).
4. Fill out the necessary To, Subject, Message, and From fields.
5. Enter the App Password provided by Microsoft.
6. Type in the Outlook outgoing Server address: smtp.office365.com:587
7. Ensure that Server Requires Secure Sockets (SSL) is highlighted.
8. Press Send and the email will be sent.

## iCloud

Once an iCloud email account has been created and two-factor authentication is enabled, an app-specific password generation is required to be configured.

1. Create an iCloud third-party email client
2. iCloud: Create and use App Passwords
3. Open the E-mailer component in QSD and Save to Core & Run (or press F5).
4. Fill out the necessary To, Subject, Message, and From fields.
5. Enter the App-Specific Password provided by Apple.
6. Type in the iCloud outgoing Server address: smtp.mail.me.com:587
7. Ensure that Server Requires Secure Sockets (SSL) is highlighted.
8. Press Send and the email will be sent.

## Control Pins

| Pin Name | Value | String | Position | Pins Available |
|---|---|---|---|---|
| From | N / A | text | N / A | Input / Output |
| Message | N / A | text | N / A | Input / Output |
| Password | N / A | text | N / A | Input |
| Send | N / A | trigger | N / A | Input / Output |
| Server | N / A | text | N / A | Input / Output |
| Server Requires SSL | 0 1 | false true | 0 1 | Input / Output |
| Status | N / A | Sending Send Succeed < error message > | N / A | Output |
| Subject | N / A | text | N / A | Input / Output |
| To | N / A | text | N / A | Input / Output |


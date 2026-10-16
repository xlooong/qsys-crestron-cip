# HttpClient

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/HttpClient.htm

Use the following methods to add URL references to your Lua script. Transfer data over a secure HTTP connection, or encode and decode a URL, parameters, and string data into a valid ASCII format without spaces.

Tip: Both HTTP and HTTPS are supported. To use HTTPS, prefix the URL with https:// instead of http://. TLS 1.0, 1.1, 1.2, and 1.3 are supported with HTTPS.

## Methods

| Method | Description |
|--------|-------------|
| HttpClient.Download | Specify a URL from which to download data. |
| HttpClient.Upload | Specify a URL to which to upload data. |
| HttpClient.CreateUrl | Combine URL components into a complete encoded URL string. |
| HttpClient.EncodeParams | Specify a comma-separated list of parameters to encode. |
| HttpClient.EncodeString | Specify a string to encode. |
| HttpClient.DecodeString | Specify an encoded string to decode. |
| HttpClient.Get | Retrieves data from the URL specified in table using the GET request method. |
| HttpClient.Put | Transfers data to the URL specified in table using the PUT request method. |
| HttpClient.Post | Transfers data to the URL specified in table using the POST request method. |
| HttpClient.Patch | Modifies data |

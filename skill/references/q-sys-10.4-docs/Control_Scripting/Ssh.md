# Ssh

> 来源: https://help.qsys.com/q-sys_10.4/#Control_Scripting/Using_Lua_in_Q-Sys/Ssh.htm

The Ssh object allows Q-SYS cores to make secure client connections to devices on the network. It is very similar to TcpSocket, but requires additional connection arguments (host, port, user, password). Unlike TcpSocket, a standard, unified event handler function is not supported. Additionally, compared to TcpSocket, there is a LoginFailed event handler that is called if login credentials are incorrect.

Note: Supported public key algorithms: ssh-ed25519, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521, ssh-rsa, rsa-sha2-512, rsa-sha2-256, ssh-dss.

## Sections
- Methods
- PKI Authentication Methods
- Event Handlers
- Events
- Properties
- Examples

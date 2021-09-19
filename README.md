# PyKLXfil: Python Keylogger and Exfiltrator.
## Python3 toolset of a keylogger and exfiltrator.
## The toolsit contains three four main tools:
* PyKLXfil-Server: a socket server to recieve the exfiltrated data from a victem.
* PyKLXfil-Client: the agent that will perform the encoded key logging with a custome base64 table and exfiltration of data back to PyKLXfil-Server.
* PyKLXfil-Client-mail: a standalone agent that will perform encoded key logging with a custome base64 table and exfiltration to a gmail email account (more stealthy).
* PyKLXfil-Decoder: a tool to decode the key logs.

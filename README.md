# PyKLXfil: Python Keylogger and Exfiltrator.
## The toolsit contains four main tools:
* PyKLXfil-Server: a socket server to recieve the exfiltrated data from a victem.
* PyKLXfil-Client: the agent that will perform the encoded key logging with a custome base64 table and the exfiltration of data back to PyKLXfil-Server.
* PyKLXfil-Client-mail: a standalone agent that will perform encoded key logging with a custome base64 table and exfiltration to a gmail email account (more stealthy).
* PyKLXfil-Decoder: a tool to decode the key logs.
## Install:
```sh
  git clone https://github.com/iD4rksid3/PyKLXfil.git
  cd PyKLXfil
  #The tool requires only two external modules: yagmail and pynput
  pip3 install -r requirements.txt
  ```
## Usage:

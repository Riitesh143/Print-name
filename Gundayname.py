from platform import system
import sys
import os
import datetime   
from time import sleep

def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
   

 d888b  db    db d8b   db d8888b.  .d8b.  db    db      d8888b. db    db db      d88888b db    db db    db 
88' Y8b 88    88 888o  88 88  `8D d8' `8b `8b  d8'      88  `8D 88    88 88      88'     `8b  d8' `8b  d8' 
88      88    88 88V8o 88 88   88 88ooo88  `8bd8'       88oobY' 88    88 88      88ooooo  `8bd8'   `8bd8'  
88  ooo 88    88 88 V8o88 88   88 88~~~88    88         88`8b   88    88 88      88~~~~~  .dPYb.   .dPYb.  
88. ~8~ 88b  d88 88  V888 88  .8D 88   88    88         88 `88. 88b  d88 88booo. 88.     .8P  Y8. .8P  Y8. 
 Y888P  ~Y8888P' VP   V8P Y8888D' YP   YP    YP         88   YD ~Y8888P' Y88888P Y88888P YP    YP YP    YP 
                                                                                                           
                                                                                                           
                                                      
                                                      

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()

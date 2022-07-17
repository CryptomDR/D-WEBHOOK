import json
import os
import requests
from colorama import *
req = requests.session()
os.system('cls')


print(Fore.CYAN + '''


            ██████╗       ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ██╔══██╗      ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██║  ██║█████╗██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
            ██║  ██║╚════╝██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██████╔╝      ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═════╝        ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
            
                        [ - Coded by: https://github.com/CryptomDR - ]
''')

print("""
D-WEBHOOK Modules
=================
    #  Name
    _  ____
    1  Send message
    2  Send message spam
    """)

eligio = input("Module: ")

os.system('cls')

if eligio=="1":
    while True:
        print()
        print(Fore.CYAN + '[ - SEND MESSAGE - ]')
        print('====================')
        print()
        API = input("| " + "API BOT: ")
        print()
        Texto = input("| " + "Text: ")
        print()

        param = {"content": Texto}

        Post = req.post(API, data=param, json=json)
        if "The request body contains invalid JSON." in Post.text:
            print(Fore.RED + "[-] failed message")

        else:
            print(Fore.GREEN + "[+] successful message")

elif eligio=="2":
    print()
    print(Fore.CYAN + '[ - SPAM MESSAGE - ]')
    print()
    print('====================')
    API = input(" | " + "API BOT: ")
    print()
    Texto = input(" | " + "Text: ")
    print()

    param = {"content": Texto}
    while True:
        Post = req.post(API, data=param, json=json)
        if "The request body contains invalid JSON." in Post.text:
            print(Fore.RED + "[-] failed message")

        else:
            print(Fore.GREEN + "[+] successful message")





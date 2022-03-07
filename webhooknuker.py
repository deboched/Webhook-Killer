import requests
import os
import time
import colorama
from colorama import Fore, Back, Style
import os as sistema
from os import system
from discord import Webhook, RequestsWebhookAdapter

webhook = "https://discord.com/api/webhooks/949817117274951780/OvuclYO5Sx2ucJ6AO1XDAaO8E7TMhMS7TNPYll_T8XYWQ0iRyTK9_NwUcLGniUBrDA2k"

webhook2 = "https://discord.com/api/webhooks/949817117274951780/OvuclYO5Sx2ucJ6AO1XDAaO8E7TMhMS7TNPYll_T8XYWQ0iRyTK9_NwUcLGniUBrDA2k"

user = sistema.getlogin()
os.system("cls")

print(Fore.MAGENTA + Style.DIM + Style.BRIGHT + """
     __    __     _     _                 _        ___ _               _    
    / / /\ \ \___| |__ | |__   ___   ___ | | __   / __\ |__   ___  ___| | __
    \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  / /  | '_ \ / _ \/ __| |/ /
     \  /\  /  __/ |_) | | | | (_) | (_) |   <  / /___| | | |  __/ (__|   < 
      \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \____/|_| |_|\___|\___|_|\_\
                                                                        
""")
print(Style.RESET_ALL)

system("title " + '𝑫𝑩𝑶𝑿 𝓦𝓮𝓫𝓱𝓸𝓸𝓴 𝐂𝐡𝐞𝐜𝐤 - 𝐔𝐬𝐞𝐫: ' + f'[{user}]')

webhook = input(Fore.MAGENTA + Style.DIM + " [DB0X] URL: ")
print(Style.RESET_ALL)

check = requests.get(webhook)
if check.status_code == 404:
    print("")
    print(Fore.RED + Style.BRIGHT + "\n [DB0X] Webhook invalida!")
    print(Style.RESET_ALL)
    time.sleep(5)
elif check.status_code == 200:
    print("")
    print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook valida!")
    print(Style.RESET_ALL)
    time.sleep(5)
    os.system("cls")

os.system("cls")

system("title " + '𝑫𝑩𝑶𝑿 𝓦𝓮𝓫𝓱𝓸𝓸𝓴 𝐊𝐢𝐥𝐥𝐞𝐫 - 𝐔𝐬𝐞𝐫: ' + f'[{user}]')
print(Fore.BLUE + Style.DIM + Style.BRIGHT + """
 __    __     _     _                 _            _ _ _           
/ / /\ \ \___| |__ | |__   ___   ___ | | __   /\ /(_) | | ___ _ __ 
\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  / //_/ | | |/ _ \ '__|
 \  /\  /  __/ |_) | | | | (_) | (_) |   <  / __ \| | | |  __/ |   
  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \/  \/|_|_|_|\___|_|   
                                                                   
""")
print(Style.RESET_ALL)

webhook2 = input(Fore.BLUE + Style.DIM +" [DB0X] URL: ")
print(Style.RESET_ALL)

def delete():
    requests.delete(webhook2)
    checker = requests.get(webhook2)
    if checker.status_code == 404:
        print("")
        print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook destruído com sucesso!")
        print(Style.RESET_ALL)
    elif checker.status_code == 200:
        print("")
        print(Fore.RED + Style.BRIGHT + "\n [DB0X] Ocorreu uma falha ao destruir o webhook!")
        print(Style.RESET_ALL)

delete()

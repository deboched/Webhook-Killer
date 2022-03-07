import requests, os, time
from colorama import Fore, Back, Style
import os as sistema
from os import system
from discord import Webhook, RequestsWebhookAdapter

user = sistema.getlogin()
os.system("cls")

print(Fore.MAGENTA + Style.DIM + Style.BRIGHT + """
 __    __     _     _                 _            _ _ _           
/ / /\ \ \___| |__ | |__   ___   ___ | | __   /\ /(_) | | ___ _ __ 
\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  / //_/ | | |/ _ \ '__|
 \  /\  /  __/ |_) | | | | (_) | (_) |   <  / __ \| | | |  __/ |   
  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \/  \/|_|_|_|\___|_|   
                                                                   
""" + Style.RESET_ALL)

system(f"title 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: 𝐃𝐞𝐛𝐨𝐜𝐡𝐞𝐝#𝟒𝟒𝟎𝟒 - 𝑫𝑩𝑶𝑿 𝓦𝓮𝓫𝓱𝓸𝓸𝓴 𝐂𝐡𝐞𝐜𝐤 - 𝐔𝐬𝐞𝐫: [{user}]")

webhook = input(Fore.MAGENTA + Style.DIM + " [DB0X] URL: ")
print(Style.RESET_ALL)

check = requests.get(webhook)
if check.status_code == 404:
    print(Fore.RED + Style.BRIGHT + "\n [DB0X] Webhook invalida!" + Style.RESET_ALL)
    time.sleep(5)
elif check.status_code == 200:
    print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook valida!" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "\n [DB0X] Deletando a Webhook...!" + Style.RESET_ALL)
    time.sleep(1)
    requests.delete(webhook)
    checker = requests.get(webhook)
    if checker.status_code == 404:
        print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook destruído com sucesso!" + Style.RESET_ALL)
    elif checker.status_code == 200:
        print(Fore.RED + Style.BRIGHT + "\n [DB0X] Ocorreu uma falha ao destruir o webhook!" + Style.RESET_ALL)
    time.sleep(5)

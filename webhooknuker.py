import requests, time, utils
from colorama import Fore, Back, Style
from discord import Webhook, RequestsWebhookAdapter

utils.checker_intro()
webhook = input(Fore.MAGENTA + Style.DIM + " [DB0X] URL: ")
print(Style.RESET_ALL)

check = requests.get(webhook)
if check.status_code == 404:
    print(Fore.RED + Style.BRIGHT + "\n [DB0X] Webhook invalida!" + Style.RESET_ALL)
    time.sleep(5)
elif check.status_code == 200:
    print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook valida!" + Style.RESET_ALL)
    time.sleep(1)
    utils.killer_intro()
    print(Fore.YELLOW + Style.BRIGHT + "\n [DB0X] Deletando a Webhook...!" + Style.RESET_ALL)
    requests.delete(webhook)
    checker = requests.get(webhook)
    if checker.status_code == 404:
        print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook destruído com sucesso!" + Style.RESET_ALL)
    elif checker.status_code == 200:
        print(Fore.RED + Style.BRIGHT + "\n [DB0X] Ocorreu uma falha ao destruir o webhook!" + Style.RESET_ALL)
    time.sleep(5)
import os as sistema
from colorama import Fore, Back, Style

user = sistema.getlogin()

def killer_intro():
	sistema.system("cls")
	sistema.system(f"title 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: 𝐃𝐞𝐛𝐨𝐜𝐡𝐞𝐝#𝟒𝟒𝟎𝟒 - 𝑫𝑩𝑶𝑿 𝓦𝓮𝓫𝓱𝓸𝓸𝓴 𝐊𝐢𝐥𝐥𝐞𝐫 - 𝐔𝐬𝐞𝐫: [{user}]")
	print(Fore.BLUE + Style.DIM + Style.BRIGHT + """
 __    __     _     _                 _            _ _ _           
/ / /\ \ \___| |__ | |__   ___   ___ | | __   /\ /(_) | | ___ _ __ 
\ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  / //_/ | | |/ _ \ '__|
 \  /\  /  __/ |_) | | | | (_) | (_) |   <  / __ \| | | |  __/ |   
  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \/  \/|_|_|_|\___|_|   
                                                                   
""" + Style.RESET_ALL)

def checker_intro():
	sistema.system("cls")
	print(Fore.MAGENTA + Style.DIM + Style.BRIGHT + """
     __    __     _     _                 _        ___ _               _    
    / / /\ \ \___| |__ | |__   ___   ___ | | __   / __\ |__   ___  ___| | __
    \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  / /  | '_ \ / _ \/ __| |/ /
     \  /\  /  __/ |_) | | | | (_) | (_) |   <  / /___| | | |  __/ (__|   < 
      \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \____/|_| |_|\___|\___|_|\_\
                                                                        
""" + Style.RESET_ALL)
	sistema.system(f"title 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: 𝐃𝐞𝐛𝐨𝐜𝐡𝐞𝐝#𝟒𝟒𝟎𝟒 - 𝑫𝑩𝑶𝑿 𝓦𝓮𝓫𝓱𝓸𝓸𝓴 𝐂𝐡𝐞𝐜𝐤 - 𝐔𝐬𝐞𝐫: [{user}]")

import requests
from colorama import Fore, Back, Style
from ..setup import HTTP_SERVER_ADDRESS

# Iniciando colorama
import colorama
colorama.init()

url = HTTP_SERVER_ADDRESS + '/command'

def send_command(id: int):
    try:
        response = requests.post(url, data=str(id), headers={'Content-Type': 'text/plain'})
        if response.status_code == 200:
            print(Fore.GREEN + f"Sucesso: {response.text}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"\tFalha: {response.status_code} {response.text}",  + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)


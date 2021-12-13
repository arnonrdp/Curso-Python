import requests
try:
    url = requests.get('http://pudim.com.br')
except requests.exceptions.ConnectionError:
    print(f'\033[31mO site Pudim não está acessível no momento.\033[0m')
else:
    print(f'\033[32mO site Pudim está acessível.\033[0m')

"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
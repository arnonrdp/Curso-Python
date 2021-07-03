"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""
from random import randint

t = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {t}\n'
      f'O maior valor sorteado foi {max(t)}\n'
      f'O menor valor sorteado foi {min(t)}')

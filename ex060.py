"""
Daça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial
num = int(input('Digite um número: '))
print(f'O fatorial de {num} é igual a {factorial(num)}.')
"""
#  Resolução com FOR LOOP:
fat = num
for i in range(fat, 1, -1):
    fat = fat * (i - 1)
print(f'{num}! = {fat}.')

# Resolução com WHILE:
fat = num
while num > 1:
    fat = fat * (num - 1)
    num -= 1
print(f'O fatorial é igual a {fat}.')
"""
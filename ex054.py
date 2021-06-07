"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if atual - ano >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print(f'Ao todo tivemos {totalMaior} pessoas maiores de idade.\n'
      f'E também tivemos {totalMenor} pessoas menores de idade.')

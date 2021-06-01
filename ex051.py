"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
n1 = int(input('Insira o 1º termo da progressão: '))
raz = int(input('Insira a razão da progressão: '))

for c in range(n1, raz*10+n1, raz):
    print(c)

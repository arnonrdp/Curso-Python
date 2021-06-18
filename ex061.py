"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
n1 = int(input('Insira o 1º termo da progressão: '))
raz = int(input('Insira a razão da progressão: '))
n1 -= raz
cont = 0
while cont < 10:
    n1 = n1 + raz
    cont += 1
    print(n1, end=' ')
print('\nFIM')

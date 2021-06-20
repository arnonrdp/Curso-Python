"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
n1 = int(input('Insira o 1º termo da progressão: '))
raz = int(input('Insira a razão da progressão: '))
n1 -= raz
cont = 0
rep = 10
while cont < rep:
    n1 = n1 + raz
    cont += 1
    print(n1, end=' ')
    if cont == rep:
        rep = int(input('\nQuer mais quantas repetições? ')) + cont
print('FIM')

"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from pause import seconds
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
option = 0
while option != 5:
    option = int(input('''Considere:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair
O que você deseja? '''))
    if option == 1:
        print(f'A soma é igual a {n1 + n2}.')
        seconds(3)
    elif option == 2:
        print(f'O produto é igual a {n1 * n2}.')
        seconds(3)
    elif option == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior do que {n1}.')
        else:
            print('Os números são iguais.')
        seconds(3)
    elif option == 4:
        n1 = float(input('Digite o 1º número: '))
        n2 = float(input('Digite o 2º número: '))
    elif option == 5:
        print('Finalizando...')
        seconds(2)
    else:
        print('Opção inválida. Tente novamente...')
print('Programa Encerrado.')

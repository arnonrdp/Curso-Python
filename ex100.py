from random import randint
from pause import seconds


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        n.append(randint(1, 10))
        print(n[i], end=' ')
        seconds(0.4)
    print('PRONTO!')


def somapar():
    soma = 0
    for num in n:
        if num % 2 == 0:
            soma += num
    print( f'Somando os valores pares de {n}, temos {soma}')


n = list()
sorteia()
somapar()

"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
numb = 0
soma = 0
cont = 0
conf = 'S'
lista = []
while conf not in 'Nn':
    numb = int(input('Digite número que deseja somar: '))
    soma = soma + numb
    cont += 1
    lista.append(numb)
    lista = sorted(lista)
    conf = str(input('Quer continuar? [S/N] '))
media = soma / cont
print(f'A média dos números foi de {media}.\n'
      f'O maior número é {lista[-1]}.\n'
      f'O menor número é {lista[0]}.')

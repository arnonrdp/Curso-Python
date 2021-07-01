"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
print(f'{"-" * 40}\n{"LOJA SUPER BARATÃO":^40}\n{"-" * 40}')
caro = soma = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}\n'
      f'O total da compra foi de R${soma:.2f}.\n'
      f'Temos {caro} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {produto} que custa {menor:.2f}.')

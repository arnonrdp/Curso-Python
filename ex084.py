"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
temp = []
pessoas = []
gordo = magro = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        gordo = magro = temp[1]
    else:
        if temp[1] > gordo:
            gordo = temp[1]
        if temp[1] < magro:
            magro = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print(f'{"-=" * 25}\n'
      f'Ao todo, você cadastrou {len(pessoas)} pessoas.\n'
      f'O maior peso foi de {gordo}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == gordo:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {magro}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == magro:
        print(f'[{p[0]}]', end=' ')

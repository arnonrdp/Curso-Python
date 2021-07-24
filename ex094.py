"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
grupo = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    grupo.append(pessoa.copy())
    if resp in 'N':
        break
soma = media = 0
for i in grupo:
    soma += i['idade']
media = soma / len(grupo)
print(f'{"-=" * 30}\n'
      f'– O grupo tem {len(grupo)} pessoas.\n'
      f'– A média de idade é de {media} anos.\n'
      f'– As mulheres cadastradas foram: ', end='')
for m in grupo:
    if m['sexo'] in 'F':
        print(f'[ {m["nome"]} ]', end=' ')
print('\n– Lista de pessoas que estão acima da média:')

for i in grupo:
    if i['idade'] > media:
        for k, v in i.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')

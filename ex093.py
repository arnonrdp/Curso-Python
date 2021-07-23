"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
partidas = int(input(f' Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
total = 0
for i in range(partidas):
    gols.append(int(input(f'  Quantos gols na partida {i + 1}? ')))
jogador['gols'] = gols[:]
total = sum(gols)
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas:')
for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {g} gols')
print(f'Foi um total de {total} gols.')

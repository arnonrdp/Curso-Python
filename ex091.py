"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from pause import seconds
from operator import itemgetter
dados = dict()
print('Valores sorteados:')
for i in range(1, 5):
    dados[f'jogador{i}'] = randint(1, 6)
    print(f'   O jogador{i} tirou {dados[f"jogador{i}"]}')
    seconds(0.6)
ranking = dict()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    seconds(0.6)

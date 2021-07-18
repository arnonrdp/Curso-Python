"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint
from pause import seconds

print(f'{"-" * 40}\n{"JOGA NA MEGA SENA":^40}\n{"-" * 40}')
qtde = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
print(f'{"-=" * 5} SORTEANDO {qtde} JOGOS {"-=" * 5}')
for i in range(qtde):
    seconds(0.6)
    for j in range(6):
        jogos.append(randint(1, 60))
    print(f'Jogo {i + 1}: {sorted(jogos)}')
    jogos.clear()
print(f'{"-=" * 6} < BOA SORTE > {"-=" * 6}')

def ficha(jogador='', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip().capitalize()
qtde = str(input('Número de Gols: ')).strip()
if qtde.isnumeric():
    qtde = int(qtde)
else:
    qtde = 0
ficha(nome, qtde)

"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""
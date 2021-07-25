"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogador = dict()
time = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    total = 0
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
        total = sum(gols)
        jogador['gols'] = gols.copy()
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
    print('-' * 40)
print(f'{"-=" * 20}\n'
      f'{"Cód":<5}{"Nome":<12}{"Gols":<18}{"Total"}\n'
      f'{"-" * 40}')
for i in range(len(time)):
    print(f' {i:<4}{time[i]["nome"]:<12}{time[i]["gols"]}{time[i]["total"]:>16}')
print('-' * 40)
while True:
    print('-' * 40)
    resp = int(input('Mostrar dados de qual jogador? '))
    if 0 <= resp < len(time):
        print(f'-- LEVANTAMENTO DO JOGADOR {time[resp]["nome"]}:')
        for i, g in enumerate(time[resp]['gols']):
            print(f'    No jogo {i + 1}, fez {g} gols.')
    elif resp == 999:
        print('<< VOLTE SEMPRE >>')
        break
    else:
        print(f'ERRO! Não existe jogador com o código {resp}! Tente novamente.')

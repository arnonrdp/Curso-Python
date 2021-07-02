"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Avaí', 'São Paulo', 'Inter', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Botafogo')
print(f'{"-=" * 17}\nLista de times do Brasileirão 2019: {times}\n'
      f'{"-=" * 17}\nOs 5 primeiros são {times[:5]}\n'
      f'{"-=" * 17}\nOs 4 últimos são {times[-4:]}\n'
      f'{"-=" * 17}\nTimes em ordem alfabética: {sorted(times)}\n'
      f'{"-=" * 17}\nO Chapecoense está na {times.index("Chapecoense") + 1}ª posição')

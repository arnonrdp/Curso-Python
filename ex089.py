"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
boletim = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print(f'{"-=" * 20}\n'
      f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}\n'
      f'{"-" * 25}')
for i in range(len(boletim)):
    print(f'{i:<4} {boletim[i][0]:<10} {boletim[i][2]:>8.1f}')
while True:
    print(f'{"-" * 25}')
    detalhes = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if detalhes == 999:
        print('FINALIZANDO...\n')
        break
    else:
        print(f'Notas de {boletim[detalhes][0]} são {boletim[detalhes][1]}')
print('<<< VOLTE SEMPRE >>>')

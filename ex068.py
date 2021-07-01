"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('-=-=-=-=-=-=-=-=-=-=-=-=\n'
      'VAMOS JOGAR PAR OU ÍMPAR\n'
      '-=-=-=-=-=-=-=-=-=-=-=-=')
conta = 0
while True:
    PC = randint(0, 10)
    P1 = int(input('Diga um valor: '))
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    soma = PC + P1
    result = ''
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print('-----------------------------------------------------\n'
          f'Você jogou {P1} e o computador {PC}. Total de {soma} DEU {result}.\n'
          '-----------------------------------------------------')
    conta += 1
    if tipo[0] == result[0]:
        print('Você VENCEU!\n'
              'Vamos jogar novamente...\n'
              '-=-=-=-=-=-=-=-=-=-=-=-=')
    else:
        print(f'Você PERDEU!\n'
              f'GAME OVER! Você venceu {conta} vezes.')

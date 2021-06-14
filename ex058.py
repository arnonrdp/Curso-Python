"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
numPC = randint(0, 10)
acertou = False
tentativa = 0
while not acertou:
    play1 = int(input('De 0 a 10, qual seu palpite? '))
    tentativa += 1
    if play1 == numPC:
        acertou = True
    else:
        if play1 < numPC:
            print('Um pouco mais...')
        else:
            print('Um pouco menos...')
print(f'Você acertou na {tentativa}ª tentativa.')

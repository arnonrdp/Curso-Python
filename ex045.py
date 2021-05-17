from random import randint
while True:
    try:
        print('-=' * 20)
        print(f'JOKENPÔ'.center(40))
        print('-=' * 20)
        print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
        itens = ('PEDRA', 'PAPEL', 'TESOURA')
        player = int(input('Qual é a sua jogada? '))
        pc = randint(1, 2)
        if player < 0 or player > 2:
            continue
        else:
            print(f'\nVocê jogou {itens[player]}\n'
                  f'Computador jogou {itens[pc]}\n')
            if player == pc:
                print('EMPATOU!')
            elif pc == 0:
                if player == 1:
                    print('VOCÊ VENCEU!')
                elif player == 2:
                    print('COMPUTADOR VENCEU!')
            elif pc == 1:
                if player == 0:
                    print('COMPUTADOR VENCEU!')
                elif player == 2:
                    print('VOCÊ VENCEU!')
            elif pc == 2:
                if player == 0:
                    print('COMPUTADOR VENCEU!')
                elif player == 1:
                    print('VOCÊ VENCEU!')
            break
    except ValueError:
        continue

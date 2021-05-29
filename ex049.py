"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
while True:
    try:
        n = int(input('Digite um número inteiro para ver sua tabuada: '))
        if type(n) == int:
            print(f'A tabuada de {n} é:')
            for tab in range(0, 11):
                print(f'{n} x {tab} = {n * tab}')
            break
        else:
            continue
    except ValueError:
        continue

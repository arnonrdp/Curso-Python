from pause import seconds


def maior(* num):
    print(f'{"-=" * 25}\n'
          'Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        seconds(0.3)
    print(f'Foram informados {len(num)} valores ao todo.\n', end=''
          f'O maior valor informado foi {max(num) if len(num) > 0 else "0"}.\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
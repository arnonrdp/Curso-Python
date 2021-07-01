"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print(f'{"=" * 40}\n{"BANCO CEV":^40}\n{"=" * 40}')
cinq = vint = dez = um = 0
valor = int(input('Que valor você quer sacar? R$ '))
while True:
    if valor >= 50:
        cinq += 1
        valor -= 50
    elif 20 <= valor < 50:
        vint += 1
        valor -= 20
    elif 10 <= valor < 20:
        dez += 1
        valor -= 10
    elif 1 <= valor < 10:
        um += 1
        valor -= 1
    elif valor == 0:
        print(f'Total de {cinq} cédulas de R$50\n'
              f'Total de {vint} cédulas de R$20\n'
              f'Total de {dez} cédulas de R$10\n'
              f'Total de {um} cédulas de R$1\n'
              f'{"=" * 40}\nVolte sempre ao BANCO CEV! Tenha um bom dia!')
        break

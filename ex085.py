"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
num = [[], []]
for i in range(7):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'{"-=" * 25}\n'
      f'Os valores pares digitados foram: {num[0]}\n'
      f'Os valores ímpares digitados foram: {num[1]}\n')

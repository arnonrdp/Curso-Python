"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
peso = []
for p in range(1, 6):
    peso.append(input(f'Insira o peso da {p}ª pessoa: '))
    # .append colocará os números digitados em uma lista
peso = sorted(peso)
print(f'O maior peso é {peso[-1]}Kg.\n'
      f'O menor peso é {peso[0]}Kg.')

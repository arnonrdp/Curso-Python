"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        elif listanum[c] < menor:
            menor = listanum[c]

print(f'{"=-" * 30}\n'
      f'Você digitou os valores {listanum}\n'
      f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')

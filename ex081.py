"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
valores = []
while True:
    i = int(input('Digite um valor: '))
    valores.append(i)
    confirma = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if confirma in 'Nn':
        break
print(f'{"-=" * 25}\n'
      f'Você digitou {len(valores)} elementos.\n'
      f'Os valores em ordem decrescente são {valores.sort(reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista')

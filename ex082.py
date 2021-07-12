"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
listaPar = []
listaImp = []
while True:
    i = int(input('Digite um valor: '))
    lista.append(i)
    confirma = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if confirma in 'N':
        break
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImp.append(i)
print(f'{"-=" * 25}\n'
      f'A lista completa é {lista}\n'
      f'A lista de pares é {listaPar}\n'
      f'A lista de ímpares é {listaImp}')

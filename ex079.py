"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
confirma = ''
valores = []
while confirma in 'SY':
    i = int(input('Digite um valor: '))
    if i not in valores:
        valores.append(i)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    confirma = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'{"-=" * 20}\n'
      f'Você digitou os valores {sorted(valores)}')

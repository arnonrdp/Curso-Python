from pause import seconds


def contador(inicio, fim, passo):
    print(f'{"-=" * 23}\n'
          f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    for num in range(inicio, fim + passo, passo):
        print(f'{num} ', end='')
        seconds(0.25)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print(f'{"-=" * 23}\n'
      'Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: ').strip())
f = int(input('Fim: ').strip())
p = int(input('Passo: ').strip())
if p == 0:
    p = 1
if i < f:
    contador(i, f, p)
if i > f and p > 0:
    contador(i, f, -p)
if i > f and p < 0:
    contador(i, f, p)

"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
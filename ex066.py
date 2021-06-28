"""
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
s = cont = 0
while True:
    num = float(input('Digite um número [999 encerra]: '))
    if num == 999:
        break
    s += num
    cont += 1
print(f'Você digitou {cont} números.\n'
      f'A soma deles é igual a {s}.')

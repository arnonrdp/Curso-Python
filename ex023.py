num = int(input('Digite um número entre 1 e 9999: '))

print(f'Analisando o número {num}.\n'
      f'Unidade: {num // 1 % 10}\n'
      f'Dezena: {num // 10 % 10}\n'
      f'Centena: {num // 100 % 10}\n'
      f'Milhar: {num // 1000 % 10}')

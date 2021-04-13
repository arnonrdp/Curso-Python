real = float(input('Quanto você tem? '))
print(f'Com R${real:.2f} é possível comprar US${(real / 3.27):.2f}.\n'
      f'(Considerando US$1,00 = R$3,27)')
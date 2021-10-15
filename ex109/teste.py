from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade( p )}\n'
      f'O dobro de {p} é {moeda.dobro( p, False )}\n'
      f'Aumentando 10%, temos {moeda.aumentar( p, 10 )}\n'
      f'Reduzindo 13%, temos {moeda.diminuir( p, 13 )}\n' )

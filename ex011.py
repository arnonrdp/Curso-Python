lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar * alt
print(f'A área da parede é de {area:.2f} metros quadrados.\n'
      f'É necessário {(area / 2):.2f} litros de tinta para pintar a parede.')

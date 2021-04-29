vel = float(input('Digite a velocidade do veículo: '))

if vel > 80:
    print(f'Você ultrapassou o limite.\n'
          f'Calculando a multa...\n'
          f'A multa será de R$ {((vel - 80) * 7):.2f}')
else:
    print('Boa viagem.\n'
          'Se beber não dirija.')

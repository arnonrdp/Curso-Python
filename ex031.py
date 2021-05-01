while True:
    try:
        dist = int(input('Qual a distância da viagem? '))
        if dist < 0:
            continue
        else:
            if dist >= 200:
                print(f'Preço da passagem: R$ {dist * 0.45}.\n')
            else:
                print(f'Preço da passagem: R$ {dist * 0.5}.')
            break
    except ValueError:
        continue

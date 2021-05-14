while True:
    try:
        retas = input('Informe os comprimentos da três retas: ').strip().replace(',', '').split()
        r1 = int(sorted(retas, reverse=True)[0])
        r2 = int(sorted(retas, reverse=True)[1])
        r3 = int(sorted(retas, reverse=True)[2])

        if r1 < 0 or r2 < 0 or r3 < 0:
            continue
        else:
            if r1 > (r2 + r3):
                print('Não é possível formar um triângulo')
            elif r1 == r2 == r3:
                print('O triângulo formado é equilátero')
            elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
                print('O triângulo formado é isósceles.')
            else:
                print('O triângulo formado é escaleno.')
            break
    except ValueError:
        continue

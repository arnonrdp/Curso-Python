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
                print('Não será possível formar um triângulo')
            else:
                print('É possível formar um triângulo')
            break
    except ValueError:
        continue

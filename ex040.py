while True:
    try:
        nota1 = float(input('Insira a nota 1: '))
        nota2 = float(input('Insira a nota 2: '))
        media = (nota1 + nota2) / 2
        if media < 0:
            continue
        elif 0 <= media < 5:
            print(f'Media: {media:.1f}\nREPROVADO!')
            break
        elif 5 <= media < 7:
            print(f'Média: {media:.1f}\nRECUPERAÇÃO')
            break
        elif media >= 7:
            print(f'Média: {media:.1f}\nAPROVADO')
            break
        else:
            continue
    except ValueError:
        continue

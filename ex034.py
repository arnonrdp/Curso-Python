while True:
    try:
        salario = float(input('Qual é seu salário? ').strip())
        if salario <= 0:
            continue
        else:
            if salario >= 1250:
                print(f'Seu novo salário será de R$ {(salario * 1.1):.2f}')
            else:
                print(f'Seu novo salário será de R$ {(salario * 1.15):.2f}')
            break
    except ValueError:
        continue

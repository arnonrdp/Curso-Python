from datetime import date

while True:
    try:
        ano = int(input('Informe seu ano de nascimento: '))
        idade = date.today().year - ano
        if idade < 0:
            continue
        else:
            if idade <= 9:
                print(f'Idade: {idade} anos.\nCategoria MIRIM')
            elif idade <= 14:
                print(f'Idade: {idade} anos.\nCategoria INFANTIL')
            elif idade <= 19:
                print(f'Idade: {idade} anos.\nCategoria JUNIOR')
            elif idade <= 25:
                print(f'Idade: {idade} anos.\nCategoria SÊNIOR')
            elif idade > 25:
                print(f'Idade: {idade} anos.\nCategoria MASTER')
            break
    except ValueError:
        continue

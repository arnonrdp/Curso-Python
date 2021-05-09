from datetime import date

while True:
    try:
        ano = int(input('Informe seu ano de nascimento: '))
        idade = date.today().year - ano
        if idade < 18:
            print(f'Você tem {idade} anos e precisa esperar mais {18 - idade} anos para se alistar.')
            break
        elif idade == 18:
            print(f'Você tem 18 anos. Vá já se alistar.\nO Brasil precisa de você!!!')
            break
        elif idade > 18:
            print(f'Você tem {idade} anos e deveria ter se alistado há {idade - 18} anos.')
            break
        else:
            continue
    except ValueError:
        continue

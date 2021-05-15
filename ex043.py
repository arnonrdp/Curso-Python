while True:
    try:
        altura = float(input('Qual sua altura? '))
        peso = float(input('Qual seu peso? '))
        imc = peso / altura ** 2
        if imc < 0:
            print('Insira valores válidos')
            continue
        else:
            if imc < 18.5:
                print(f'Seu IMC é de {imc:.1f}\nABAIXO DO PESO')
            elif 18.5 <= imc < 25:
                print(f'Seu IMC é de {imc:.1f}\nPESO IDEAL')
            elif 25 <= imc < 30:
                print(f'Seu IMC é de {imc:.1f}\nSOBREPESO')
            elif 30 <= imc < 40:
                print(f'Seu IMC é de {imc:.1f}\nOBESIDADE')
            elif 40 <= imc:
                print(f'Seu IMC é de {imc:.1f}\nOBESIDADE MÓRBIDA')
            break
    except ValueError:
        continue

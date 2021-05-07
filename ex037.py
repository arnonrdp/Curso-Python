while True:
    try:
        num = int(input('Insira um número inteiro: '))
        base = int(input('Considerando:\n'
                         '1 para binário\n'
                         '2 para octal\n'
                         '3 para hexadecimal\n'
                         'Escolha a base de conversão: '))
        if base < 1 or base > 3:
            continue
        elif base == 1:
            print(bin(num)[2:])
            break
        elif base == 2:
            print(oct(num)[2:])
            break
        elif base == 3:
            print(hex(num)[2:])
            break
    except ValueError:
        continue

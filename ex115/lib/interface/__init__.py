def leiaint(msg):
    while True:
        try:
            num = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[031mUsuário preferiu não digitar esse número.\033[0m')
            continue
        else:
            return int(num)


def linha(tam=42):
    return '-' * tam


def header(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    header('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc

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


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[031mUsuário preferiu não digitar esse número.\033[0m')
            continue
        else:
            return num


inteiro = leiaint('Digite um Inteiro: ')
real = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de
um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
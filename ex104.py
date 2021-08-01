def leiaint(txt):
    print('-' * 25)
    ok = False
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""
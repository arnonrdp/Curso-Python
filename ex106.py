from pause import seconds
c = ('\033[m',      # 0 - Sem cores
     '\033[40m',    # 1 - Preto
     '\033[41m',    # 2 - Vermelho
     '\033[42m',    # 3 - verde
     '\033[43m',    # 4 - amarelo
     '\033[44m',    # 5 - azul
     '\033[45m',    # 6 - magenta
     '\033[46m',    # 7 - ciano
     '\033[47m',    # 8 - branco
     )


def helping():
    while True:
        title('SISTEMA DE AJUDA PyHELP', 3)
        user = input('Função ou Biblioteca > ')
        if user.upper() == 'FIM':
            title('ATÉ LOGO!', 2)
            break
        title(f"Acessando o manual do comando '{user}'", 4)
        print(c[8], end='')
        help(user)
        print(c[8], end='')


def title(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(f'{"~" * tam}\n'
          f'  {msg}  \n'
          f'{"~" * tam}')
    print(c[0], end='')
    seconds(1)


helping()

"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
"""
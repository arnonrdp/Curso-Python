def metade(n=0, monet=True):
    if monet:
        return f'R${(n / 2):.2f}'.replace('.', ',')
    else:
        return n / 2


def dobro(n=0, monet=True):
    if monet:
        return f'R${(n * 2):.2f}'.replace('.', ',')
    else:
        return n * 2


def aumentar(n=0, v=0, monet=True):
    if monet:
        return f'R${(n + n * v / 100):.2f}'.replace('.', ',')
    else:
        return n + n * v / 100


def diminuir(n=0, v=0, monet=True):
    if monet:
        return f'R${(n - n * v / 100):.2f}'.replace('.', ',')
    else:
        return n - n * v / 100


"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
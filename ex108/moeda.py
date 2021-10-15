def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, v=0):
    return n + n * v / 100


def diminuir(n=0, v=0):
    return n - n * v / 100


def moeda(n=0, monet='R$'):
    return f'{monet}{n:.2f}'.replace('.', ',')


"""
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""
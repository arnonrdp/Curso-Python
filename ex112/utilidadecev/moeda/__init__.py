def resumo(price, juro=0, desc=0):
    print(f'{"-" * 30}\n'
          f'{"RESUMO DO VALOR".center(30)}\n'
          f'{"-" * 30}\n'
          f'Preço analisado: \t{moeda(price)}\n'
          f'Dobro do preço: \t{dobro(price)}\n'
          f'Metade do preço: \t{metade(price)}\n'
          f'{juro}% de aumento: \t{aumentar(price, juro)}\n'
          f'{desc}% de redução: \t{diminuir(price, desc)}\n'
          f'{"-" * 30}')


def metade(price=0, monet=True):
    result = price / 2
    return result if monet is False else moeda(result)


def dobro(price=0, monet=True):
    result = price * 2
    return result if monet is False else moeda(result)


def aumentar(price=0, v=0, monet=True):
    result = price + price * v / 100
    return result if monet is False else moeda(result)


def diminuir(price=0, v=0, monet=True):
    result = price - price * v / 100
    return result if monet is False else moeda(result)


def moeda(price=0.0, monet='R$'):
    return f'{monet}{price:.2f}'.replace('.', ',')

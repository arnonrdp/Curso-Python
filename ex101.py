def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 0 <= idade <= 150:
        if 0 < idade < 16:
            return f'Com {idade} anos: NÃO VOTA.'
        elif 16 <= idade < 18 or idade >= 65:
            return f'Com {idade} anos: VOTO OPCIONAL'
        elif 18 <= idade < 65:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'ERRO! Idade Inválida.\nCom {idade} anos, já morreu.'


print('-' * 30)
ano = int(input('Em que ano você nasceu? ').strip())
print(voto(ano))

"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
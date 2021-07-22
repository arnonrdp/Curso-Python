"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
ano = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - ano
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - date.today().year)
print('-=' * 25)
# print(dados)
for k, v in dados.items():
    print(f'  – {k} tem o valor {v}')

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from pause import seconds

arq = 'dados.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        header('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        header('Saindo do sistema... Até logo')
        break
    else:
        header('\033[31mERRO! Digite uma opção válida!\033[m')
    seconds(2)


"""
a. Vamos criar um menu em Python, usando modularização.
b. Vamos ver como fazer acesso a arquivos usando o Python.
c. Vamos finalizar o projeto de acesso a arquivos em Python.
"""
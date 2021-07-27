def escreva(txt):
    print(f'~~{"~" * len(txt)}~~\n'
          f'  {txt}  \n'
          f'~~{"~" * len(txt)}~~')


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')

"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável. Ex:
escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""
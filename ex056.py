"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
nome = []
idade = []
sexo = []
somaIdade = 0
maisVelho = 0
nomeVelho = ''
totalF20 = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalF20 += 1

print(f'A idade média do grupo é de {somaIdade / 4}\n'
      f'O {nomeVelho} é o mais velho com {maisVelho} anos.\n'
      f'O grupo tem {totalF20} mulheres com menos de 20 anos.')

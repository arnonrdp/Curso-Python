"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
maiorIdade = 0
sexoMasc = 0
sexoFmenor = 0
while True:
    print(f'{"-" * 25}\nCADASTRE UMA PESSOA\n{"-" * 25}')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiorIdade += 1
    if sexo[0] == 'M':
        sexoMasc += 1
    if idade < 20 and sexo[0] == 'F':
        sexoFmenor += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input(f'{"-" * 25}\nQuer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        print('====== FIM DO PROGRAMA ======\n'
              f'Total de pessoas com mais de 18 anos: {maiorIdade}\n'
              f'Ao todo temos {sexoMasc} homens cadastrados.\n'
              f'E temos {sexoFmenor} mulheres com menos de 20 anos.')
        break

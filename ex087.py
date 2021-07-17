"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col3 = lin1 = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
        while coluna == 2:
            col3 += matriz[linha][coluna]
            break
print(f'{"-=" * 25}')
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'{"-=" * 25}\n'
      f'A soma dos valores pares é {par}.\n'
      f'A soma dos valores da terceira coluna é {col3}\n'
      f'O maior valor da segunda linha é {max(matriz[1])}')

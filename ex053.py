"""
Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
frase = str(input('Escreva a frase: ')).strip().replace(' ', '').lower()
esarf = list(frase)
esarf.reverse()

if frase == ''.join(esarf):
    print('É um palindromo!')
else:
    print('Não é um palindromo!')

print(frase)
print(''.join(esarf))
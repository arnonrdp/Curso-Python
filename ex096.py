def area(largura, comprimento):
    return largura * comprimento


print(' Controle de Terrenos \n'
      '----------------------')
larg = float(input('LARGURA (m): ').strip())
comp = float(input('COMPRIMENTO (m): ').strip())
print(f'A área de um terreno {larg}x{comp} é de {area(larg, comp):.2f}m².')

"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""
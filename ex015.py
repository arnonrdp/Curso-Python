dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = 60 * dias + 0.15 * km
print(f'O total a pagar é de R${(preco):.2f}.')

while True:
    try:
        preco = float(input('Insira o preço do produto: '))
        cond = int(input('Considere:\n'
                         '1. À vista no dinheiro (-10%)\n'
                         '2. À vista no cartão (-5%)\n'
                         '3. Em 2x no cartão (sem juros)\n'
                         '4. Em 3x ou mais no cartão (20% de juros)\n'
                         'Informe a condição de pagamento: '))
        if preco <= 0 or cond < 1 or cond > 4:
            continue
        else:
            if cond == 1:
                total = preco * 0.9
            elif cond == 2:
                total = preco * 0.95
            elif cond == 3:
                total = preco
                parcela = preco / 2
                print(f'Sua compra será parcelada em 2x de R${parcela} sem juros.')
            elif cond == 4:
                total = preco * 1.2
                prazo = int(input('Quantas parcelas? '))
                parcela = total / prazo
                print(f'Sua compra será parcelada em {prazo}x de R${parcela:.2f} com juros.')
            print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
            break
    except ValueError:
        continue

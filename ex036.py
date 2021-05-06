casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o salário do comprador? '))
prazo = int(input('Em quantos anos ele vai pagar? ')) * 12

if casa / prazo > salario * 30 / 100:
    print(f'Empréstimo negado!\n'
          f'Mensalidade (R$ {(casa / prazo):.2f}) ultrapassa 30% do salário ({(salario * 30 / 100):.2f})')
else:
    print('Empréstimo aprovado!')

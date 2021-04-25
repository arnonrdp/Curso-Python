cidade = input('Digite o nome da cidade: ')


if cidade.lower().strip().split()[0].find('santo') == 0:
    print('Essa cidade começa com Santo')
else:
    print('Essa cidade NÃO começa com Santo')

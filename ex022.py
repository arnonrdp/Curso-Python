nome = input('Digite seu nome completo: ')

print(f'Analisando seu nome...\n'
      f'Seu nome em maiúsculas é: {nome.upper()}.\n'
      f'Seu nome em minúsculas é: {nome.lower()}.\n'
      f'Seu nome completo tem {len(nome.replace(" ", ""))} letras.\n'
      f'Seu primeiro nome ({nome.split()[0]}) tem {len(nome.split()[0])} letras.')

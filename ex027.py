nome = str(input('Digite seu nome completo: ')).strip().split()

print(f"Primeiro nome: {nome[0]}.\n"
      f"Último nome: {nome[len(nome) - 1]}.")

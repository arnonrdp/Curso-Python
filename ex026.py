frase = str(input('Digite uma frase: ')).strip()

print(f'A letra "A" aparece {frase.lower().count("a")} vezes na frase.\n'
      f'Primeiro ela aparece na posição {frase.lower().find("a") + 1}.\n'
      f'Por último aparece na posição {frase.lower().rfind("a") + 1}.')

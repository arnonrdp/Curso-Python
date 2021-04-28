import random
num = int(input('Digite um número de 1 a 5: '))
numPC = random.randrange(0, 6)
if num == numPC:
    print(f'Você acertou! O número era {numPC} mesmo.')
else:
    print(f'Você errou! O número era {numPC}.')

import random

alunos = list(map(str, input("Digite os nomes dos alunos: ").strip().split(',')))

print(random.choice(alunos))

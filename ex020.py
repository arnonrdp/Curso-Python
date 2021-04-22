import random

alunos = list(map(str, input("Digite os nomes dos alunos: ").strip().split(',')))
random.shuffle(alunos)
print(alunos)

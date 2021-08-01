def notas(* nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-' * 30)
    boletim = dict()
    boletim['total'] = len(nota)
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    boletim['média'] = sum(nota) / len(nota)
    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        elif 5 <= boletim['média'] < 7:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""
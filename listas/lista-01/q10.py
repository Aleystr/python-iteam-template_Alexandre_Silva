# Lista 01 — Questão 10: Análise Crítica de Código
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q10.py: reescreva a função corrigindo os 3 problemas encontrados.
# 
#   def processar_alunos(alunos=[]):
#       aprovados = []
#       for i in range(len(alunos)):
#           if alunos[i]['nota'] >= 7.0:
#               aprovados = aprovados + [alunos[i]['nome']]
#       print(aprovados)
# 
# Em q10_resposta.txt: identifique cada problema e explique por que é um problema.
# Dica: há um problema em: (1) definição da função, (2) como o loop é escrito, (3) como a lista é construída.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def processar_alunos(alunos=[]):
    aprovados = []
    for aluno in alunos:
        if aluno['nota'] >= 7.0:
            aprovados.append(aluno['nome'])
    print(aprovados)

lista_alunos = [
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'Carlos', 'nota': 6.0},
    {'nome': 'Marina', 'nota': 7.2},
    {'nome': 'João', 'nota': 5.5}
]

lista_alunos2 = [
    {'nome': 'rafael', 'nota': 8.5},
    {'nome': 'Luiz', 'nota': 6.0},
    {'nome': 'Caio', 'nota': 7.2},
    {'nome': 'carlinhos', 'nota': 5.5}
]
processar_alunos(lista_alunos)
processar_alunos(lista_alunos2)


# Lista 02 — Questão 06: Módulo de Estatísticas (programa principal)
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
import q06_estatisticas as est

notas = []

print("Digite 10 notas: ")

for i in range(10):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)

print("\nResultados:" )

print("Media: ", est.media(notas))
print("Mediana: ", est.mediana(notas))
print("moda: ", est.moda(notas))
print("Desvio padrao: ", est.desvio_padrao(notas))
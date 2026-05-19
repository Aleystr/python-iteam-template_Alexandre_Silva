# Desafio 02 — Calculadora de IMC
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
peso = float(input("Informe seu peso(kg):"))
altura = float(input("Informe sua altura(m):"))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
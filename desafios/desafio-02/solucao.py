# Desafio 02 — Calculadora de IMC
# Aluno: (Alexandre Silva da conceição)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
peso = float(input("Informe seu peso(kg):")) # --- Força o input do peso para float, para evitar erros de tipo
altura = float(input("Informe sua altura(m):")) # --- Força o input da altura para float, para evitar erros de tipo
imc = peso / (altura ** 2)# --- Calcula o IMC usando a fórmula: peso dividido pela altura ao quadrado
print(f"Seu IMC é: {imc:.2f}") #--- Imprime o resultado do IMC formatado para 2 casas decimais
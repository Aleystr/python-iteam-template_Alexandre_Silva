# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

nome = input("Digite seu nome completo: ")
ano_nascimento = input("Digite seu ano de nascimento: ")    
cpf = str(input("Digite seu CPF: "))
altura = float(input("Digite sua altura (em metros): "))
if not ano_nascimento.isdigit():
    print("Erro: O ano de nascimento deve ser um número inteiro.")
    exit()
idade = 2026 - int(ano_nascimento)
print(f"Nome: {nome}")
print(f"CPF: {cpf}")    
print(f"Ano de nascimento: {ano_nascimento}")
print(f"Altura: {altura:.2f} metros")
print(f"Idade em 2026: {idade} anos")
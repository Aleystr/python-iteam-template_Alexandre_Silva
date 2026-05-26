# Lista 01 — Questão 06: Validador de Senha
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────

while True:
    senha = input('Digite uma senha: ')
    if len(senha) < 8:
        print('Senha deve ter no mínimo 8 caracteres.')
        continue
    if not any(char.isdigit() for char in senha):
        print('Senha deve conter pelo menos um dígito especial.')
        continue
    if not any(char.isupper() for char in senha):
        print('Senha deve conter pelo menos uma letra maiúscula.')
        continue
    print('Senha válida após X tentativa(s).')

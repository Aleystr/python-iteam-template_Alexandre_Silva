# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
notas = []
for i in range(10):
    while True:
        try:
            nota =float(input("Informe a nota (0.0–10.0): "))
            if nota < 0.0 or nota > 10.0:
                print("Nota inválida. Digite um valor entre 0.0 e 10.0.")
            else:
                notas.append(nota)
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
        
maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas)/len(notas)

acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1

for nota in notas:
    if nota >= 7.0:
        print(f"Nota: {nota} - Classificação: Aprovado")
    elif nota >= 5.0:
        print(f"Nota: {nota} - Classificação: Recuperação")
    else:
        print(f"Nota: {nota} - Classificação: Reprovado")

print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média: {media:.2f}")
print(f"Quantidade acima da média: {acima_media}")
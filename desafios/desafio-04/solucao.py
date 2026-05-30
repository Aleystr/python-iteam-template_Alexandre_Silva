# Desafio 04 — Tabuada Personalizada
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# Loop principal para permitir várias tabuadas sem reiniciar o script
while True:
    print("\n--- Gerador de Tabuada ---")
    entrada = input("Digite um número de 1 a 10 (ou 0 para sair): ")

    # Validação simples para evitar que o programa quebre se o usuário digitar letras
    if not entrada.strip().isdigit():
        print("Por favor, digite apenas números inteiros.")
        continue

    numero = int(entrada)

    # 3. Garanta que o programa pare se o usuário digitar 0
    if numero == 0:
        print("Programa encerrado. Até mais!")
        break

    # Validação do intervalo solicitado (1 a 10)
    if numero < 1 or numero > 10:
        print("Número inválido! O número deve estar entre 1 e 10.")
        continue

    # 2. Utilize um laço for para exibir a tabuada desse número
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2d} = {resultado}")

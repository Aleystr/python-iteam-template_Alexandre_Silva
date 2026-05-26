# Desafio 03 — Sistema de Multas
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

velocidade = float(input("Informe a velocidade do veículo (km/h):")) # --- Força o input da velocidade para float, para evitar erros de tipo

if isinstance(velocidade,float):
    if velocidade > 80:
        print("Multado! Você excedeu o limite de 80km/h")
        multa = (velocidade - 80) * 7
        print(f"Valor da multa: R${multa:.2f}")
    elif velocidade <= 80:
        print("Boa viagem! Dirija com segurança")
else:
    print("Entrada inválida. Por favor, informe um número para a velocidade.")

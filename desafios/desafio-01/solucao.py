# Desafio 01 — Seu Primeiro Script
# Aluno: (Alexandre Silva da Conceição)
# Data:  (19-05-2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

import re # --- Import do "re" para o uso da funcão re.split() para separar a data de nascimento do usuário em dia, mês e ano. ---
from datetime import datetime # --- Import datetime para usar data atualizada
dt_nascimento_usuario = input ("Informe sua data de nascimento(dd-mm-YYYY): ")# --- Pede a Idade do Usuário e armazena a data de nascimento em uma variável. ---
dt_formatada = re.split(r"[-./_ ]", dt_nascimento_usuario)# --- Separa a data de nascimento do usuário em dia, mês e ano usando a função re.split() e armazena cada parte em uma variável. ---
dt_now = datetime.now() # -- Armazena na variável a data atual
dt_split = re.split(r"[-./_ ]", (dt_now.strftime("%d-%m-%Y"))) # --- Separa a data atual em dia, mês e ano usando a função re.split() e armazena cada parte em uma variável. ---
dia = int(dt_split[0])       - int(dt_formatada[0]) # --- Faz  a conversão da data para dias para poder ser convertido em anos -------- 

if (int(dt_formatada[1]) < int(dt_split[1])): # --- Verifica se o mês de nascimento é menor que o mês atual para calcular a idade corretamente. ---
    mes = 30 *(int(dt_split[1]) - int(dt_formatada[1])) 
else:
    mes = 30 * (int(dt_formatada[1]) - int(dt_split[1]))

ano = 365*(int(dt_split[2])  - int(dt_formatada[2]))
idade = int((dia + mes + ano)/365) # --- Calcula a idade do usuário em anos e exibe o resultado. ---
print("A idade do usuario é de:", idade, "anos")
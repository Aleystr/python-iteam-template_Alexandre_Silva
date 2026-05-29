# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
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
import math

def media(dados):
    if not dados:
        raise ValueError("A lista nao pode estar vazia")
    
    resultado = sum(dados)/len(dados)
    return round(resultado, 2)

def mediana(dados):
    if not dados:
        raise ValueError ("A lista nao pode estar vazia")
    
    dados_ordenados =sorted(dados)
    n = len(dados_ordenados)
    meio =  n//2

    if n % 2 == 0:
        resultado = (dados_ordenados[meio -1] + dados_ordenados[meio]) / 2
    else:
        resultado = dados_ordenados[meio]

    return round(resultado, 2)

def moda(dados):
    if not dados:
        raise ValueError("A lista nao pode estar vazia.")
    
    frequencia = {}

    for valor in dados:
        frequencia[valor] = frequencia.get(valor,0) + 1

    maior_freq = max(frequencia.values())

    for valor, freq in frequencia.items():
        if freq == maior_freq:
            return round(valor, 2)
        
def desvio_padrao(dados):
    if not dados:
        raise ValueError("A lista nao pode estar vazia.")
    
    m = media(dados)

    soma = 0
    for valor in dados:
        soma += (valor -m) ** 2

    variancia = soma/ len(dados)
    resultado = math.sqrt(variancia)

    return round(resultado, 2)
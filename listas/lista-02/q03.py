# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        'nome': nome,
        'codigo': codigo,
        'quantidade': quantidade,
        'preco': preco
    }
    inventario.append(produto)

def buscar_por_codigo(inventario, codigo):
    for produto in inventario:
        if produto['codigo'] == codigo:
            return produto
    return None

def listar_abaixo_minimo(inventario, minimo):
    produtos_abaixo = []
    for produto in inventario:
        if produto['quantidade'] < minimo:
            produtos_abaixo.append(produto)
    return produtos_abaixo

def valor_total(inventario):
    total = 0
    for produto in inventario:
        total += produto['quantidade'] * produto['preco']
    return total

# Código principal para demonstração
inventario = []
adicionar_produto(inventario, 'Caneta', 'C001', 50, 1.5)
adicionar_produto(inventario, 'Lápis', 'L001', 30, 0.5)
adicionar_produto(inventario, 'Caderno', 'C002', 20, 5.0)

# Buscar por código
produto = buscar_por_codigo(inventario, 'C001')
print('Produto encontrado:', produto)
# Listar produtos abaixo do mínimo
produtos_abaixo = listar_abaixo_minimo(inventario, 25) 
print('Produtos abaixo do mínimo:', produtos_abaixo)
# Valor total do inventário
total = valor_total(inventario)
print('Valor total do inventário:', total)


    
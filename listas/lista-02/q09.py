# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.
# 
# Em q09_resposta.txt: explique a diferença entre _atributo e __atributo em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
class produto():
    def __init__ (self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.__estoque = 0
        self.repor(estoque)

    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def  preco(self, novo_preco: float):
        if novo_preco <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        self.__preco = novo_preco

    @property 
    def estoque(self) -> int:
        return self.__estoque
    
    def repor(self, quantidade: int):
        if quantidade < 0:
            raise ValueError("A quantidade de reposição não pode ser negativada.")
        self.__estoque += quantidade

    def vender(self, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade de venda deve ser maior que zero")
        if quantidade > self.__estoque:
            raise ValueError(f"Estoque insuficiente. Tentativa de vender {quantidade}, mas ha apenas {self.__estoque} em estoque.")
        self.__estoque -= quantidade

    def __str(self) -> str:
        return f"produto: {self.nome} | preco: R$ {self.preco:.2f} | estoque:  {self.estoque} unid."

    def __repr__ (self) -> str:
        return f"Produto(nome = {self.nome!r}, preco = {self.preco}, estoque = {self.estoque})"

if __name__ == "__main__":
    p = produto("Notebook", 3500, 10)
    print(p)
    print(repr(p))

    p.vender(3)
    print(f"Venda de tres unidades realizadas com sucesso.")
    print(f"Estoque atual: {p.estoque}")
    
    p.repor(5)
    print(f"reposicao de 5 unidades realizada.")
    print(f"Estoque atual: {p.estoque}")

    try:
        print(f"Tentando vender 15 unidades (Estoque disponivel: {p.estoque} )...")
        p.vender(15)
    except ValueError as e:
        print(f"Erro Capturado: {e}")

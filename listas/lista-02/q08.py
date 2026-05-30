# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
class Funcionario ():
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 10

class Gerente(Funcionario):
    def __init__ (self, nome, salario, departamento):
        super().__init__(nome,salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return super().calcular_bonus()

class Estagiario(Funcionario):
    def __init__ (self, nome, salario, curso):
        super().__init__(nome,salario)
        self.curso = curso

    def calcular_bonus(self):
        return super().calcular_bonus()
    
funcionarios = [ Funcionario("Alice Souza", 4000),
                 Gerente("Carlo Lima", 9000, "Tecnologia"),
                 Estagiario("Beatriz Reis", 1500, "Engenharia de Software")]


print("----- Relatorio de bonus ------")
for f in funcionarios:
    bonus = f.calcular_bonus()
    print(f"Nome: {f.nome} | Bonus: R$ {bonus:.2f}")  
        
"""
 Em python ao referenciar a propria classe o interpretador
 faz a busca diretamente na classe real daquele objeto 
 especifico, se a classefilha implementou o metodo, ela 
 sobrescreve (@override)
""" 
from Pessoa import Pessoa

class Eleitor(Pessoa):
    def __init__ (self, nome, id_voto, ja_votou):
        super().__init__(nome)
        self.id_voto = id_voto
        self.ja_votou = False

    def ja_votou(self):
        return self.__ja_votou

    def participacao(self):
        self.__ja_votou = True

    def __str__(self) -> str:
        return f"{self.nome} (ID: {self.id_eleitor})"


# candidato.py
from Pessoa import Pessoa

class Candidato(Pessoa):
    """Representa um candidato a eleicao."""
    
    def __init__(self, numero: int, nome: str, partido: str):
        super().__init__(nome)
        self.numero = numero
        self.partido = partido
        self.__votos = 0
    
    def registrar_voto(self) -> None:
        """Registra um voto para o candidato."""
        self.__votos += 1
    
    @property
    def votos(self) -> int:
        """Retorna o total de votos do candidato."""
        return self.__votos
    
    def __str__(self) -> str:
        return f"[{self.numero}] {self.nome} - {self.partido}"
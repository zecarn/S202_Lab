class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, corridas: list, nota: int):
        self.corridas = corridas
        self.nota = nota

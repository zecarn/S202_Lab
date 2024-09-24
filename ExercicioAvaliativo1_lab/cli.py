from classes import Passageiro, Motorista, Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "sair":
                print("Até mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []
        repeat = 1

        while(repeat == 1):
            print("===========================================================")
            print("Entre com os dados do passageiro: ")
            nome = input("Nome: ")
            documento = input("Documento: ")
            passageiro = Passageiro(nome, documento)
            
            print("===========================================================")
            print("Entre com os dados da corrida: ")
            nota = int(input("Nota da corrida: "))
            distancia = float(input("Distância: "))
            valor = float(input("Valor: "))
            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)

            print("===========================================================")
            repeat = int(input("Deseja adicionar mais corridas? (1-Sim  0-Não): "))
        
        nota = int(input("Nota do motorista: "))
        motorista = Motorista(corridas, nota)
        
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nota: {motorista['nota']}")
            for numero, corrida in enumerate(motorista['corridas'], start=1):
                print(f"Corrida {numero}: {corrida}")
 

    def update_motorista(self):
        id = input("Entre com o id: ")
        corridas = []
        repeat = 1

        while(repeat == 1):
            print("Entre com os dados do passageiro: ")
            nome = input("Nome: ")
            documento = input("Documento: ")
            passageiro = Passageiro(nome, documento)

            print("Entre com os dados da corrida: ")
            nota = int(input("Nota: "))
            distancia = float(input("Distância: "))
            valor = float(input("Valor: "))
            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)

            repeat = int(input("Deseja adicionar mais corridas? (1-Sim  0-Não): "))
     
        nota = int(input("Nota do motorista: "))
        motorista = Motorista(corridas, nota)

        self.motorista_model.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Entre com o id: ")
        self.motorista_model.delete_motorista(id)
        
    def run(self):
        print("Bem vindo ao Motorista CLI!")
        print("Possíveis comandos: create, read, update, delete, sair")
        super().run()
        
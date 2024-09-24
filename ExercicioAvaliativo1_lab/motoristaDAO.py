from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import Motorista, Passageiro, Corrida

class MotoristaModel:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            data = {
                'Nota do motorista': motorista.nota,
                'Corridas': [
                    {
                        'Nota da corrida': corrida.nota,
                        'Distância': corrida.distancia,
                        'Valor': corrida.valor,
                        'Passageiro': {
                            'Nome': corrida.passageiro.nome,
                            'Documento': corrida.passageiro.documento
                        }
                    } for corrida in motorista.corridas
                ]
            }

            res = self.db.collection.insert_one(data)
            print(f"ID do motorista {res.inserted_id}")
            return res.inserted_id

        except Exception as e:
            print(f"Ocorreu um erro ao criar motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            data = self.db.collection.find_one({"_id": ObjectId(id)})
            nota = data['Nota do motorista']
            corridas = data['Corridas']
            print(f"Motorista encontrado: {data}")
            return data #Motorista(corridas, nota)
        except Exception as e:
            print(f"Ocorreu um erro ao procurar motorista: {e}")
            return None

    def update_motorista(self, id: str, motorista):
        try:
            data = {
                'Nota do motorista': motorista.nota,
                'Corridas': [
                    {
                        'Nota da corrida': corrida.nota,
                        'Distância': corrida.distancia,
                        'Valor': corrida.valor,
                        'Passageiro': {
                            'Nome': passageiro.nome,
                            'Documento': passageiro.documento
                        }
                    } for corrida in motorista.corrida
                ]
            }

            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
            print(f"Motorista atualizado: {res.modified_count} documento modificado")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar documento: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar motorista: {e}")
            return None
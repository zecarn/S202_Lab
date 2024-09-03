from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, data, colle):
        self.db = Database(database= data, collection= colle)

    def resetarDatabase(self):
        self.db.resetDatabase()

    def totalDeVendasPorDia(self):
        self.dados = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id": 1}}
        ]) 
        writeAJson(self.dados, "Total_de_vendas_por_dia")

    def produtoMaisVendido(self):
        self.dados = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade_total": -1}},
            {"$limit": 1}
        ])
        writeAJson(self.dados, "Produto_mais_vendido")

    def clienteQueMaisGastou(self):
        self.dados = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$_id", "preco_total":{"$sum": "$produtos.preco"}}},
            {"$sort": {"preco_total": -1}},
            {"$limit": 1}
        ])
        writeAJson(self.dados, "Cliente_que_mais_gastou")

    def produtoAcimaDeUm(self):
        self.dados = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade":{"$gt": 1}}}
        ])
        writeAJson(self.dados, "Produtos_vendidos_acima_de_um")
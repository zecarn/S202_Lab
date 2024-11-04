from database import Database

data = Database("bolt://44.212.47.113:7687", "neo4j", "spear-hardcopies-nurse")

class QueryData:
    def __init__(self, database):
        self.db = database

    # Questão 1
    def teacherRenzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc as nasc, t.cpf as cpf"
        results = self.db.execute_query(query)
        return [(result["nasc"], result["cpf"]) for result in results]

    def teacherM(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["name"], result["cpf"]) for result in results]

    def cityAll(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def schoolNumber(self):
        query = "MATCH (s:School) WHERE s.number >= 150 OR s.number = 550 RETURN s.name AS name, s.address AS address, s.number AS number"
        results = self.db.execute_query(query)
        return [(result["name"], result["address"], result["number"]) for result in results]

    # Questão 2
    def teacherOldYoung(self):
        query1 = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS min"
        query2 = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS max"
        results1 = self.db.execute_query(query1)
        results2 = self.db.execute_query(query2)
        oldest = results1[0]["min"] if results1 else None
        youngest = results2[0]["max"] if results2 else None
        return oldest, youngest

    def populationAverage(self):
        query = "MATCH (c:City) RETURN avg(c.population) AS average"
        results = self.db.execute_query(query)
        return [result["average"] for result in results]

    def cityCep(self):
        query = "MATCH (c:City {cep:'37540-000'}) RETURN replace(c.name, 'a', 'A') AS place "
        results = self.db.execute_query(query)
        return [result["place"] for result in results]

    def teacherThird(self):
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS third"
        results = self.db.execute_query(query)
        return [result["third"] for result in results]

query_db = QueryData(data)

# Questão 1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Prof Renzo: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for nasc, cpf in query_db.teacherRenzo():
    print(f"Ano de nascimento: {nasc}")
    print(f"CPF: {cpf}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Professores que começam com M:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for name, cpf in query_db.teacherM():
    print(f"Nome: {name}")
    print(f"CPF: {cpf}")
    print("-----------------------------")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Nome das cidades:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for name in query_db.cityAll():
    print(f"Cidade: {name}")
    print("-----------------------------")

# Questão 2
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Professor mais novo e mais velho:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
oldest, youngest = query_db.teacherOldYoung()
print(f"Mais velho: {oldest}")
print(f"Mais novo: {youngest}")
print("-----------------------------")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("População:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for average in query_db.populationAverage():
    print(f"Média: {average}")
    print("-----------------------------")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Cidade de CEP=37540-000:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for place in query_db.cityCep():
    print(f"Nome: {place}")
    print("-----------------------------")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Terceiro caractere dos porfessores:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for third in query_db.teacherThird():
    print(f"Caractere: {third}")
    print("-----------------------------")

data.close()

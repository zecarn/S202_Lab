class TeacherCRUD():
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (t: Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print(f"Professor {name} inserido!")

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query, {"name": name})
        for result in results:
            
            print(f"Professor {name}")
            print(f"Ano de nascimento: {result['ano_nasc']}")
            print(f"CPF: {result['cpf']}")
        
    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DELETE t"
        self.db.execute_query(query, {"name": name})
        print(f"Professor {name} deletado!")

    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)
        print(f"CPF de {name} alterado")



    



    


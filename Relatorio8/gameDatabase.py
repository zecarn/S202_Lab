
class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, old, points):
        query = "CREATE (:Jogador {name: $name, old: $old, points: $points})"
        parameters = {"name": name, "old": old, "points": points}
        self.db.execute_query(query, parameters)

    def create_match(self, name):
        query = "CREATE (:Partida {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_player(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self):
        query = "MATCH (p:Partida) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_participa(self):
        query = "MATCH (p:Partida)<-[:PARTICIPA]-(j:Jogador) RETURN p.name AS name, j.name AS match_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["match_name"]) for result in results]

    def update_playerPoints(self, name, points):
        query = "MATCH (j:Jogador {name: name}) SET j.points = $points"
        parameters = {"name": name, "points": points}
        self.db.execute_query(query, parameters)
        
    def insert_player_match(self, player_name, match_name):
        query = "MATCH (j:Jogador {name: $player_name}) MATCH (p:Partida {name: $match_name}) CREATE (j)-[:PARTICIPA]->(p)"
        parameters = {"player_name": player_name, "match_name": match_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (j:Jogador {name: $name}) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, name):
        query = "MATCH (p:Partida {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_participacao(self, name, match_name):
        query = "MATCH (j:Jogador {name: $name})-[:PARTICIPA]->(p:Partida {name: $match_name}) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

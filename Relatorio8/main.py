from database import Database
from gameDatabase import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.83.79.61:7687", "neo4j", "cry-firefighting-stuff")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("Vitor", 20, 0)
game_db.create_player("João", 21, 4)
game_db.create_player("Mario", 35, 0)
game_db.create_player("Cristiano Ronaldo", 30, 6)
game_db.create_player("Messi", 27, 9)
game_db.create_player("Neymar", 38, 11)
game_db.create_player("Pelé", 98, 100)

# Criando algumas partidas
game_db.create_match("Morumbi")
game_db.create_match("LaLiga")

# Inserindo jogadores nas partidas
game_db.insert_player_match("Vitor", "Morumbi")
game_db.insert_player_match("João", "Morumbi")
game_db.insert_player_match("Mario", "Morumbi")
game_db.insert_player_match("Cristiano Ronaldo", "LaLiga")
game_db.insert_player_match("Messi", "LaLiga")
game_db.insert_player_match("Neymar", "LaLiga")
game_db.insert_player_match("Pelé", "LaLiga")


# Atualizando pontuação dos jogadores
game_db.update_playerPoints("Cristiano Ronaldo", 7)
game_db.update_playerPoints("Vitor", 5)



# Deletando uma partida e um jogador
game_db.delete_match("Morumbi")
game_db.delete_player("João")
game_db.delete_participacao("Pelé", "Laliga")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_player())
print("Partidas:")
print(game_db.get_match())

# Fechando a conexão com o banco de dados
db.close()
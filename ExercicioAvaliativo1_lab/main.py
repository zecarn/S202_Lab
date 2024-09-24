from database import Database
from motoristaDAO import MotoristaModel
from cli import MotoristaCLI

db = Database(database="ExercicioAv1", collection="Motoristas")
motoristaDAO = MotoristaModel(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()

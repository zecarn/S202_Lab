from database import Database
from teacher_crud import TeacherCRUD
from query import data
from teacher_cli import TeacherCLI

teacher_db = TeacherCRUD(data)
teacherCLI = TeacherCLI(teacher_db)
teacherCLI.run()

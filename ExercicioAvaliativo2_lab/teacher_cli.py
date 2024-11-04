from teacher_crud import TeacherCRUD

class SimpleCLI():
    def __init__(self):
        self.commands = {}
    
    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        valor = True
        while valor:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Até mais!")
                valor = False
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando Inválido. Tente novamente!")

class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCrud):
        super().__init__()
        self.teacher = teacherCrud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        name = input("Entre com nome: ")
        ano_nasc = input("Entre com o ano de nascimento: ")
        cpf = input("Entre com o cpf: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.teacher.create(name, ano_nasc, cpf)
        self.run()

    def read_teacher(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        name = input("Entre com o nome: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        teacher = self.teacher.read(name)
        self.run()

    def update_teacher(self): 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        name = input("Entre com o nome: ") 
        new_cpf = input("Entre com o novo cpf: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.teacher.update(name, new_cpf)
        self.run()

    def delete_teacher(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        name = input("Entre com o nome: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.teacher.delete(name)
        self.run()
        
    def run(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Bem-vindo ao Teacher CLI!")
        print("Comandos possiveis: create | read | update | delete | quit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        super().run()
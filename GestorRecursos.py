import Usuario

class GestorRecursos:

    def __init__(self):
        self.login = str
        self.senha = str
        self.nome = str
        self.email = str
        self.cod = 'admin'

        cadastroGr = {}

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getCod(self):
        return self.cod

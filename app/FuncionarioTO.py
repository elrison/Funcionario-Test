class FuncionarioTO:

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getNasc(self):
        return self.nasc

    def getSalario(self):
        return self.salario

    def getFoto(self):
        return self.foto

    def __init__(self, nome,nasc,salario,foto,id):
        self.id = id
        self.nome = nome
        self.nasc = nasc
        self.salario = salario
        self.foto = foto
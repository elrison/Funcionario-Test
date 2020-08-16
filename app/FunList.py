from app.FuncionarioDAO import FuncionarioDAO


class FunList:

    def getList(self):
        d = FuncionarioDAO()
        d.list()

    def getById(self):
        d =  FuncionarioDAO()
        d.finById()
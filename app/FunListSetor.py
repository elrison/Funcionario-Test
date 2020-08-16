from app.FuncionarioDAO import FuncionarioDAO


class FunListSetor:

    def getListSetor(self):
        setor = input("Digite o Setor: ")
        d = FuncionarioDAO()
        d.listSetor(setor)
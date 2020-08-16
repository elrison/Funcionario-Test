from app.FuncionarioTO import FuncionarioTO
from app.FuncionarioDAO import FuncionarioDAO


class FunUpdate:

    def getUp(self):
        id = input("Digite ID: ")

        print("Digite os valores a atualizar. Caso não queria atualizar o que pede, pressione ENTER.")
        print()

        nome = input("Digite o nome: ")
        nasc = input("Digite a data de nascimento (ano(4)-mês-dia): ")
        salario = input("Digite o salario: ")
        foto = input("Digite arquivo da foto: ")

        f = FuncionarioTO(nome, nasc, salario, foto, id)
        d = FuncionarioDAO()
        d.update(f)

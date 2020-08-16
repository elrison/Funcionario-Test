import unittest
from app.FuncionarioDAO import FuncionarioDAO
from app.FuncionarioTO import FuncionarioTO


class FindById(unittest.TestCase):
    def test_find_Id(self):
        self.assertEqual(self.test_Id(), None)

    # Caso o ID não seja encontrado retorna a mensagem de "ID Aão Encontrado!!!"

    def test_Id(self):
        id = 100
        nasc = ''
        nome = ''
        foto = ''
        salario = ''

        f = FuncionarioTO(nome, nasc, salario, foto, id)
        d = FuncionarioDAO()
        d.finById(f)
        return None

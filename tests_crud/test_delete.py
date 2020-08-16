import unittest

from app.FuncionarioDAO import FuncionarioDAO
from app.FuncionarioTO import FuncionarioTO


class TesteFunDelete(unittest.TestCase):
    def test_delete(self):
        self.assertEqual(test_Delete(), 100)


# Verifica se o id  é exixtente para exclusao


def test_Delete():
    id = 100
    nasc = ''
    nome = ''
    foto = ''
    salario = ''

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.delete(f)
    return id


if __name__ == '__main__':
    unittest.main()

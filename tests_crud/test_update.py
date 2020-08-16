import unittest
from app.FuncionarioDAO import FuncionarioDAO
from app.FuncionarioTO import FuncionarioTO


class FuncionarioTesteUpdate(unittest.TestCase):
    def test_update(self):
        # Quando se testa um ID inexistente e impresso a mensagem de 'ID Não Existe !!!

        # self.assertEqual(test_UpdateTest(), 40)

        # Quando é testado  o nome com mais de 20 caracteres retorna mensagem de que não pode ser ser maior que 20.

        # self.assertEqual(test_UpdateNome(), None)

        # self.assertEqual(test_UpdateTest(), None)

        # Quando a data de nascimento for maior que a data atual retorna a Mensagem:
        # "A data de nascimento não pode ser maior do que a data atual"
        self.assertEqual(test_UpdateNasc(), None)


# Quando é testado  o nome com mais de 20 caracteres retorna mensagem de que não pode ser ser maior que 20.
def test_UpdateNome():
    id = 100
    nome = 'TRIPLO - X'
    nasc = '1965-3-7'
    salario = 120
    foto = 'TESTE.PNG'

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.update(f)


# Quando a data de nascimento for maior que a data atual retorna a Mensagem:
# "A data de nascimento não pode ser maior do que a data atual"
def test_UpdateNasc():
    id = 6
    nome = 'RAMBO III'
    nasc = '2021-3-9'
    salario = 1290
    foto = 'TESTE.PNG'

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.update(f)


def test_UpdateTest():
    id = 6
    nome = 'Elvis Presley Menphis Sotero Lopes da Silva'
    nasc = '1937-5-7'
    salario = 1200
    foto = 'TESTE.PNG'

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.update(f)

    # return id


if __name__ == '__main__':
    unittest.main()

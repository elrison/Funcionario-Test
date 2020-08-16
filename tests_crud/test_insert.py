import unittest
from app.FuncionarioDAO import FuncionarioDAO
from app.FuncionarioTO import FuncionarioTO


class FuncionarioTest(unittest.TestCase):
    def test_Insert(self):
        # Quando se testa um ID inexistente e impresso a mensagem de 'ID Não Existe !!!

        self.assertEqual(test_FunNome(), 'Eduardo Sergio Amaral')

        # self.assertEqual(test_FunNasc(), None)

        # self.assertEqual(test_InsertTest(), 'Raul Santos Seixas')


# Quando a data de nascimento for maior que a data atual retorna a Mensagem:
# "A data de nascimento não pode ser maior do que a data atual"
def test_FunNasc():
    nome = 'Mario Olinto'
    nasc = '2020-09-09'
    salario = 700
    foto = 'Jrao.png'
    id = None

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.insert(f)


# Quando é testado  o nome com mais de 20 caracteres retorna mensagem de que não pode ser ser maior que 20.
def test_FunNome():
    nome = 'Eduardo Sergio Amaral'
    nasc = '1944-12-4'
    salario = 700
    foto = 'Jrao.png'
    id = None

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.insert(f)

    return nome


def test_InsertTest():
    nome = 'Jim Morrison'
    nasc = '1944-12-4'
    salario = 700
    foto = 'Jrao.png'
    id = None

    f = FuncionarioTO(nome, nasc, salario, foto, id)
    d = FuncionarioDAO()
    d.insert(f)


# return nome

if __name__ == '__main__':
    unittest.main()

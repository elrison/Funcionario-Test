import pymysql
from datetime import *
class FuncionarioDAO:

    def conect(self):
        db = pymysql.connect("localhost", "root", "", "projeto")
        return db

    def insert(self, FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "SELECT * FROM funcionario WHERE nome = '"
        sql += str(FuncionarioTO.getNome())
        sql += "';"
        cursor.execute(sql)

        if cursor.rowcount>0: # Quando é feito a busca por algum id que ja esta cadastrado retorna a mensagem
          print('Funcionario Já Cadastrado!')
        else:
           if len(FuncionarioTO.getNome())>20: # Se a quantidade de caracteres for maior que 20 retorna a MSG.
               print('Nome do Funcionario não Pode Conter mais que 20 caracteres!')
           else:
            print(FuncionarioTO.getNasc()) # imprime a data
            if str(FuncionarioTO.getNasc()) != "" and str(FuncionarioTO.getNasc()) != None:
                date_object = datetime.strptime(str(FuncionarioTO.getNasc()), '%Y-%m-%d').date()
            else:
                date_object = date.today() # se na comparação das datas a data de nascimento for maior que a data atua.
            if date_object > date.today(): # retorna a mensagem
                print('A data de nascimento nao pode ser maior que a data atual')
            else:
                sql = "INSERT INTO funcionario (nome, nasc, salario, foto) VALUES ('"
                sql += str(FuncionarioTO.getNome())
                sql += "','"
                sql += str(FuncionarioTO.getNasc())
                sql += "','"
                sql += str(FuncionarioTO.getSalario())
                sql += "','"
                sql += str(FuncionarioTO.getFoto())
                sql += ".jpeg');"

                print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
                print(type(sql))  # ver se é string

                cursor.execute(sql)
                db.commit()
                db.close()


    def list(self):
        db = self.conect()
        cursor = db.cursor()

        sql = "SELECT * FROM funcionario;"

        cursor.execute(sql)
        for row in cursor:
            print(row)

    def listSetor(self, setor): # criado um setor para verificar a vinculação de tabelas
        db = self.conect()
        cursor = db.cursor()

        # Seleciona as tabelas que os respectivos id's estão vinculados.
        sql = "SELECT * FROM funcionario inner join setor on funcionario.idsetor = setor.id WHERE setor.nome = '"
        sql += str(setor)
        sql += "';"

        cursor.execute(sql)
        for row in cursor:
            print(row)

    def delete(self, FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "SELECT * from funcionario WHERE id= "
        sql += str(FuncionarioTO.getId())
        sql += ";"
        print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
        cursor.execute(sql)

        if cursor.rowcount == 0:
            print('ID Inexistente')
        else:
            sql = "DELETE from funcionario WHERE id= "
            sql += str(FuncionarioTO.getId())
            sql += ";"

            print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
            print(type(sql))  # ver se é string

            cursor.execute(sql)
            db.commit()
            db.close()

    def update(self, FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "SELECT * FROM funcionario WHERE id= "
        sql += str(FuncionarioTO.getId())
        sql += ";"
        cursor.execute(sql)
        print('AQUI!')

        if cursor.rowcount==0: # Verifica se o id é válido
          print('Id  Não Existe !!!')
        else:
           if len(FuncionarioTO.getNome())>20:
               print('Nome do Funcionario não Pode conter mais do que 20 caracteres!')
           else:
            print(FuncionarioTO.getNasc())
            if str(FuncionarioTO.getNasc()) != "" and str(FuncionarioTO.getNasc()) != None:
                date_object = datetime.strptime(str(FuncionarioTO.getNasc()), '%Y-%m-%d').date()
            else:
                date_object = date.today()
            if date_object > date.today():
                print('A data de nascimento nao pode ser maior do que a data atual')
            else:
                sql = "UPDATE funcionario SET "
                sql += "nome ='"
                sql += str(FuncionarioTO.getNome())
                sql += "', nasc='"
                sql += str(FuncionarioTO.getNasc())
                sql += "', salario='"
                sql += str(FuncionarioTO.getSalario())
                sql += "',foto='"
                sql += str(FuncionarioTO.getFoto())
                sql += "'"
                sql += " WHERE id="
                sql += str(FuncionarioTO.getId())
                sql += ";"

                print(sql)  # imprimir o SQL para visualizar e verificar se tem erros
                print(type(sql))  # ver se é string
                cursor.execute(sql)
                db.commit()
                db.close()

    def finById(self,FuncionarioTO):
        db = self.conect()
        cursor = db.cursor()

        sql = "SELECT * FROM funcionario WHERE id= "  #Verifica se o id existe.
        sql += str(FuncionarioTO.getId())
        sql += ";"

        cursor.execute(sql)

        if cursor.rowcount == 0:  # Verifica se o id é válido
            print('Id  Não Encontrado !!!')


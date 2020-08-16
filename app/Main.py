

from app.FunInsert import FunInsert
from app.FunDelete import FunDelete
from app.FunUpdate import FunUpdate
from app.FunList import FunList
from app.FunListSetor import FunListSetor


class Main:
    flistSetor = FunListSetor()

    fins = FunInsert()

    fdel = FunDelete()

    fupd = FunUpdate()

    flist = FunList()

    fins.getIns()

    flist.getList()

    flistSetor.getListSetor()

    fupd.getUp()  # Aqui é a chamada da função Update

    fdel.getDel() # Aqui é a função que irá deletar o usuario




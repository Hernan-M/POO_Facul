import pymysql.cursors


class BdFunctions:
    def __init__(self, functions_bd: [str], function_bd: str):
        self.__functions_bd = functions_bd
        self.__function_bd = function_bd

    @property
    def functions_bd(self):
        return self.__functions_bd

    @functions_bd.setter
    def functions_bd(self, functions: []):
        self.__functions_bd = functions

    @property
    def function_bd(self):
        return self.__function_bd

    @function_bd.setter
    def get_function_bd(self, function: str):
        self.__function_bd = function


def connect_db():
    global connection
    connection = pymysql.connect(host='localhost', user='root', password='santos11', database='prova03',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


def has_some(table):
    with connection.cursor() as c:
        sql = "SELECT * FROM %s" % (table)
        c.execute(sql)
        data = c.fetchall()
        return len(data)

def find_some(table, column, value):
    global res_all
    with connection.cursor() as c:
        sql = "SELECT * FROM %s WHERE %s = %s" % (table, column, value)
        c.execute(sql)
        res_all = c.fetchall()
        print(res_all)
        print(len(res_all))
        return res_all



def send_function(funcao):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `funcao` (`cod`,`nome`) VALUES (%s, %s)"
        cursor.execute(sql, (funcao.cod, funcao.name))

    connection.commit()



def send_functionary(funcionario):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `funcionario` (`nome`,`cpf`, `funcao`, `salario`, `telefone`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (funcionario.name, funcionario.cpf, funcionario.function, funcionario.salary, funcionario.tel))

    connection.commit()

def change(table, column, value, update_column, update_value):
    with connection.cursor() as cursor:
        sql = "UPDATE %s SET %s = %s WHERE %s = %s" % (table, column, value,  update_column, update_value)
        cursor.execute(sql)

    connection.commit()


def delete_some(table, column, value):
    with connection.cursor() as cursor:
        sql = "DELETE FROM %s WHERE %s = %s" % (table, column, value)
        cursor.execute(sql)

    connection.commit()
    print('item deletado!!!')



connect_db()




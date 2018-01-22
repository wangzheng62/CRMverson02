from test__mysqlmetaclass import Mysqlserver,MysqlDB,MysqlTable


class DBserver(Mysqlserver):
    pass


class Crm(MysqlDB, DBserver):
    pass


class Employee(MysqlTable, Crm):
    pass
class Orderlist(MysqlTable, Crm):
    pass
class Product(MysqlTable, Crm):
    pass
class Customer(MysqlTable, Crm):
    pass

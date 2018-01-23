from test__mysqlmetaclass import Mysqlserver,MysqlDB,MysqlTable


class DBserver(Mysqlserver):
    pass


class Crm(MysqlDB, DBserver):
    pass


class Employee(MysqlTable, Crm):
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		return self.search()
class Orderlist(MysqlTable, Crm):
    pass
class Product(MysqlTable, Crm):
    pass
class Customer(MysqlTable, Crm):
    pass

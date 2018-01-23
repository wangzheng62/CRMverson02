import CONFIG
import mysql.connector


# 元类
class Mysqlservermetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs['DBSERVER'] = CONFIG.MYSQLDBSERVER
        return type.__new__(mcs, name, bases, attrs)


class MysqlDBmetaclass(Mysqlservermetaclass):
    def __new__(mcs, name, bases, attrs):
        attrs['db_name'] = name
        attrs['dbconn'] = {'database': name}
        return type.__new__(mcs, name, bases, attrs)


class MysqlTableMetaclass(MysqlDBmetaclass):
    def __new__(mcs, name, bases, attrs):
        attrs['table_name'] = name
        return type.__new__(mcs, name, bases, attrs)


# 基类
class MysqlserverBase(metaclass=Mysqlservermetaclass):
    @classmethod
    def __getconn(cls):
        conn = mysql.connector.connect(**cls.DBSERVER)
        return conn

    @classmethod
    def databases(cls):
        conn = cls.__getconn()
        cr = conn.cursor()
        sql = 'show databases;'
        cr.execute(sql)
        t = cr.fetchall()
        __databases = []
        for tp in t:
            __databases.append(tp[0])
        return __databases


class MysqlDBBase(metaclass=MysqlDBmetaclass):
    @classmethod
    def __getconn(cls):
        LOCAL_DB = dict(cls.DBSERVER, **cls.dbconn)
        conn = mysql.connector.connect(**LOCAL_DB)
        return conn

    @classmethod
    def getdata(cls, sql):
        conn = cls.__getconn()
        cr = conn.cursor()
        cr.execute(sql)
        t = cr.fetchall()
        return t

    @classmethod
    def changedata(cls, sql):
        conn = cls.__getconn()
        cr = conn.cursor()
        cr.execute(sql)
        conn.commit()

    @classmethod
    def tables(cls):
        conn = cls.__getconn()
        cr = conn.cursor()
        sql = 'show tables;'
        cr.execute(sql)
        t = cr.fetchall()
        __tables = []
        for tp in t:
            __tables.append(tp[0])
        return __tables


class MysqlTableBase(metaclass=MysqlTableMetaclass):
    @classmethod
    def desc(cls):
        t0 = ('Field', 'Type', 'Null', 'Key', 'Default', 'Extra')
        sql = 'desc %s;' % cls.table_name
        __desc = cls.getdata(sql)
        __desc.insert(0, t0)
        return __desc

    # 获取列名
    @classmethod
    def colnames(cls):
        sql = 'desc %s;' % cls.table_name
        t = cls.getdata(sql)
        __colnames = []
        for tp in t:
            __colnames.append(tp[0])
        return __colnames

    # 增删改查
    @classmethod
    def select(cls, DISTINCT='', COLNAMES='', TABLES='', WHERE='', LIMIT='', ORDER_BY=''):
        __SELECT = "select {} {} from {} {} {} {};".format(DISTINCT, COLNAMES, TABLES, WHERE, LIMIT, ORDER_BY)
        return __SELECT

    @classmethod
    def insert(cls, TABLES='', COLNAMES='', VALUES=''):
        __INSERT = "insert into {} {} values {};".format(TABLES, COLNAMES, VALUES)
        return __INSERT

    @classmethod
    def update(cls, TABLES='', KEYWORDS='', WHERE=''):
        __UPDATE = "update {} set {} {};".format(TABLES, KEYWORDS, WHERE)
        return __UPDATE

    @classmethod
    def delete(cls, TABLES='', WHERE=''):
        __DELECT = "delete from {} {};".format(TABLES, WHERE)
        return __DELECT

    # 列出表内总数
    @classmethod
    def fetchall(cls, NUM=0):
        if NUM == 0:
            __SQL = cls.select(COLNAMES='*', TABLES=cls.table_name)
        else:
            __SQL = cls.select(COLNAMES='*', TABLES=cls.table_name, LIMIT='LIMIT {}'.format(NUM))
        return cls.getdata(__SQL)

    @classmethod
    def colnum(cls):
        __SQL = cls.select(COLNAMES='count(*)', TABLES=cls.table_name)
        print(__SQL)
        __NUM = cls.getdata(__SQL)
        return __NUM[0][0]


# 类
class Mysqlserver(MysqlserverBase):
    pass


class MysqlDB(MysqlDBBase):
    pass


class MysqlTable(MysqlTableBase):
    def __init__(self, **kw):
        for key in kw:
            assert key in self.colnames(), "当前表中没有->{}<-列".format(key)
        self.info = kw

    def count(self):
        __condition = 'where'
        for key in self.info:
            __condition = __condition + ' {}=\'{}\' and'.format(key, self.info[key])
        __condition = __condition[:-4]
        __SQL = self.select(COLNAMES='count(*)', TABLES=self.table_name, WHERE=__condition)
        __NUM = self.getdata(__SQL)
        return __NUM[0][0]

    def search(self, NUM=0):
        __condition = 'where'
        for key in self.info:
            if self.info[key]=='':
                pass
            else:
                __condition = __condition + ' {}=\'{}\' and'.format(key, self.info[key])
        if len(__condition)<=6:
            return []
        else:
            __condition = __condition[:-4]
            if NUM == 0:
                __SQL = self.select(COLNAMES='*', TABLES=self.table_name, WHERE=__condition)
            else:
                __SQL = self.select(COLNAMES='*', TABLES=self.table_name, WHERE=__condition, LIMIT='LIMIT {}'.format(NUM))
            return self.getdata(__SQL)

    def save(self):
        __COLNAME='( '
        __VALUES='( '
        for key in self.info:
            if self.info[key]=='':
                pass
            else:
                __COLNAME=__COLNAME+key+','
                __VALUES=__VALUES+'\''+self.info[key]+'\''+','
        __COLNAME=__COLNAME[:-1]+')'
        __VALUES=__VALUES[:-1]+')'
        __SQL=self.insert(TABLES=self.table_name,COLNAMES=__COLNAME,VALUES=__VALUES)
        print(__SQL)
        try:
            self.changedata(__SQL)
            return True
        except Exception as e:
            print(e)
            return False


        pass

    # 辅助功能


if __name__ == '__main__':
    class DBserver(Mysqlserver):
        pass


    class Groupdata1(MysqlDB, DBserver):
        pass


    class Group10(MysqlTable, Groupdata1):
        pass


    db = DBserver()
    l = Group10(**{'QunNum': 900002})
    print(l.info)
    print(db.databases())
    print(l.DBSERVER)
    print(l.db_name)
    print(l.table_name)
    print(l.databases())
    print(l.tables())
    print(l.colnames())
    print(l.desc())
    print(l.count())
    print(l.search())

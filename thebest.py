# 全数据模板
d = {
    'jinjia':{"id":'employeelist',
              "name": 'employeelist',
              "css":'table table-hover table-bordered',},
    'route':{},
    'data':{},

    "colnames": [],
    "lang":[],
    "step": 5,
    "pages": 1,
    "data":[]
}
import sys,os
e=os.getcwd()
e3=os.walk(e)
d=next(e3)
os.path.join(d[0],d[1][3])
class Thebest():
    Jinjiadir=os.path.join(d[0],d[1][3])
    Routedir=e
    Database=e
    def __init__(self):
        pass
        method='GET'
        host='127.0.0.1'
        path='/'.join(e.split('\\'))
        file='testData.py'
        self.url='{} {}/{}/{}'.format(method,host,path,file)
    def createJinjia(self):
        n=1
        head='{{% block body{:02d} %}}'.format(n)
        last='{% endblock %}'
        print(head)
        text='测试资源'
        default='<a href="{}">{}</a>'.format(self.url,text)
        with open(os.path.join(self.Jinjiadir,'testjinjia.html'),'a',encoding='utf8') as f:
            f.write(head+default+last)
    def createRoute(self):
        with open(os.path.join(self.Routedir,'api.py'),'a',encoding='utf8') as f:
            f.write('')
    def createDatabase(self):
        with open(os.path.join(self.Database,'testDate.py'),'a',encoding='utf8') as f:
            f.write('')

if __name__=='__main__':
    print(Thebest.Jinjiadir)
    print(Thebest.Routedir)
    print(Thebest.Database)
    t=Thebest()
    t.createDatabase()
    t.createJinjia()
    t.createRoute()

from flask import Flask, redirect, url_for, render_template, request, flash
from func import DBserver, Crm, Product, Orderlist, Employee, Customer
from flask_login import LoginManager, login_user, login_required, logout_user
from flask.views import View
import func,time
app = Flask(__name__)
app.secret_key = 'some_secret'
login_manager = LoginManager()
login_manager.init_app(app)
#
class Baseview(View):
    temp='data01.html'
    def __init__(self,**kw):
        self.kw=kw
        print(kw)
    def dispatch_request(self):
        return render_template(self.temp, **self.kw)
view=Baseview.as_view('base01',topclass='navbar navbar-inverse')
app.add_url_rule('/',view_func=view)
#
chi=['员工ID','员工姓名','手机','权限','所属部门','职位','状态','备注','用户ID','密码','用户状态','创建时间','更新时间']
# 员工页
def getdata():
    data = Employee.fetchall()
    colnames=Employee.colnames()


    d = {
        "id":'employeelist',
        "name": 'employeelist',
        "css":'table table-hover table-bordered',
        "colnames": colnames,
        "lang":chi,
        "step": 5,
        "pages": 1,
        "data":data
    }
    return d
#测试起点
#数据定义区
rootpath='/'
employeenow={'text':'今日待办','url':'employeenow','welcome':'本功能尚未开放'}
employeesearch={'text':'员工查询','url':'employeesearch','welcome':'','employeelist':getdata()}
employeeadd={'text':'员工录入','url':'employeeadd','welcome':'','employeeform':getdata()["colnames"]}
employeeanalyze={'text':'员工分析','url':'employeeanalyze','welcome':'本功能尚未开放'}
employeelock={'text':'今日','url':'employeelock','welcome':'本功能尚未开放'}

#data test
#设计一个可递归的页面数据结构
#页面数据,本地元素
ordermain={'url':'/ordermain',
           'text':'订单管理'}
custommain={'url':'/custommain',
            'text':'客户管理'}
employeemain={'url':'/employeemain',
              'text':'人事管理',
              'subpages':[employeenow,employeesearch,employeeadd,employeeanalyze,employeelock]}
productionmain={'url':'/productionmain',
                'text':'产品管理'}
index={'url':'/index',
       'title':'index',
    'subpages':[ordermain,custommain
,employeemain,productionmain]}

#功能定义区
#视图定义
class Employeeview(View):
    temp='employeemain.html'
    def __init__(self,**kw):
        self.kw=kw
        print(kw)
    def dispatch_request(self):
        return render_template(self.temp, **self.kw)

#视图渲染


#testfunc
class Indexview(View):
    temp='index.html'
    def __init__(self,**kw):
        self.kw=kw
        print(kw)
    def dispatch_request(self):
        return render_template(self.temp, **self.kw)


view=Indexview.as_view('ppp',**index)
app.add_url_rule("/index",view_func=view)
if index['subpages']:
    for d in index['subpages']:
        print(d)
        view1=Employeeview.as_view(d['url'],**d)
        app.add_url_rule(rootpath+d['url'],view_func=view1)
        if 'subpages'in d:
            for d1 in d['subpages']:
                print(d1)
                view2=Employeeview.as_view(d1['url'],**d1)
                app.add_url_rule(rootpath+d1['url'],view_func=view2)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

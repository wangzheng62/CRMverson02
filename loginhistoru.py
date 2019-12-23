from flask import Flask, redirect, url_for, render_template, request, flash
from func import DBserver, Crm, Product, Orderlist, Employee, Customer
from flask_login import LoginManager, login_user, login_required, logout_user
from flask.views import View
import func,time
import json
app = Flask(__name__)
app.secret_key = 'some_secret'
@app.route('/',methods=['get'])
def mainpage():
    clientIP=request.remote_addr
    with app.test_client() as c:
        rv=c.get('/api/DC/em?host={}'.format(clientIP))
        res=rv.data.decode(encoding='utf8')
        print(type(res))
        print(res)
        re=json.loads(res)
        print(re)

    if re['res']:
        return '快捷登录页面'
    else:
        return redirect('/loginfirst')

class LoginView(View):
    #methods = ['get']
    def __init__(self,**kw):
        self.kw=kw
    def dispatch_request(self,):
        return render_template('loginfirst.html',**self.kw)
view=LoginView.as_view('loginfirst',url='/api/DC/em')
app.add_url_rule('/loginfirst',view_func=view)
if __name__ == '__main__':
    from api import api,DC
    view=LoginView.as_view('loginfirst',url='/api/DC/em')
    api.add_resource(DC, '/DC/<table>')
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.add_url_rule('/loginfirst',view_func=view)
    app.run(host='0.0.0.0', debug=True)

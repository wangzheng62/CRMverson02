from flask import Flask, redirect, url_for, render_template, request, flash
from func import DBserver, Crm, Product, Orderlist, Employee, Customer
from flask_login import LoginManager, login_user, login_required, logout_user
from flask.views import View
import func,time
app = Flask(__name__)
app.secret_key = 'some_secret'
ips=[]
@app.route('/',methods=['get'])
def mainpage():
    clientIP=request.remote_addr
    res=redirect('/')
    print(res)



    if clientIP in ips:
        return '快捷登录页面'
    else:
        return render_template('base01.html')
if __name__ == '__main__':
    from api import api,DC
    api.add_resource(DC, '/DC/<table>')
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.run(host='0.0.0.0', debug=True)

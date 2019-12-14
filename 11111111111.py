from flask import Flask, redirect, url_for, render_template, request, flash
from func import DBserver, Crm, Product, Orderlist, Employee, Customer
from flask_login import LoginManager, login_user, login_required, logout_user
from flask.views import View
import func,time
from flask_restful import Resource,Api
from viewsnew import app
api=Api(app,prefix='/api')

todos={'a':1,1:2,'b':3}
class H(Resource):
    def get(self,table):
        temp='select * from {} WHERE {}={};'
        d=request.args.to_dict()
        return temp.format(table,d.keys(),d.values())
    def put(self,todo_id):
        todos[todo_id]=request.form['data']
        return {todo_id:todos[todo_id]}


api.add_resource(H, '/125/<table>')

class Employee(Resource):
    def get(self):
        print(self.__class__.__name__)
        return {}
    def put(self):
        return {}
api.add_resource(Employee,'/employee')
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
    print(Employee.__name__)

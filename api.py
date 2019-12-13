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
    def get(self,todo_id):
        return {todo_id:todos[todo_id]}
    def put(self,todo_id):
        todos[todo_id]=request.form['data']
        return {todo_id:todos[todo_id]}

api.add_resource(H, '/123/<todo_id>')

class Employee(Resource):
    def get(self):
        print(self.__class__.__name__)
        return {}
    def put(self):
        return {}
api.add_resource(Employee,'/employee')
if __name__ == '__main__':
    print(Employee.__name__)

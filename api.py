from flask import Flask, redirect, url_for, render_template, request, flash
from func import DBserver, Crm, Product, Orderlist, Employee, Customer
from flask_login import LoginManager, login_user, login_required, logout_user
from flask.views import View
import func,time
from  jsondata import exm
from flask_restful import Resource,Api
from loginhistoru import app
api=Api(app,prefix='/api')
from testldap import testpw
from ldap3 import Server,ALL
import jsondata
todos={'a':1,1:2,'b':3}
class HR(Resource):
    #select
    def get(self,table):
        res=jsondata.exm

        return res
    #update
    def put(self,todo_id):
        todos[todo_id]=request.form['data']
        return {todo_id:todos[todo_id]}
    #delete
    def delete(self):
        pass
    #create
    def post(self,table):
        d=request.form.to_dict()
        print(d)
        host='192.168.70.109'
        server=Server(host,port=636,use_ssl=True,get_info=ALL)
        if testpw(server,user=d['username'],password=d['password']):
            return '验证成功'
        else:
            return {'res':'验证失败'}



ips=['127.0.10.1']
class DB(Resource):
    def get(self,table):
        d=request.args.to_dict()
        if d['host'] in ips:
            return {'res':True}
        else:
            return {'res':False}
    def put(self,todo_id):

        return 'put'
    #delete
    def delete(self):
        return 'del'
    #create
    def post(self,table):
        d=request.form.to_dict()
        print(d)
        host='192.168.70.109'
        server=Server(host,port=636,use_ssl=True,get_info=ALL)
        if testpw(server,user=d['username'],password=d['password']):
            return '验证成功'
        else:
            return {'res':'验证失败'}
api.add_resource(HR, '/HR/<table>')
api.add_resource(DB, '/DB/<table>')
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)


from flask import Flask, redirect, url_for, render_template, request, flash
from func import DBserver, Crm, Product, Orderlist, Employee, Customer
from flask_login import LoginManager, login_user, login_required, logout_user
from flask.views import View
import func,time
from flask_restful import Resource,Api
app = Flask(__name__)
api=Api(app)
class H(Resource):
    def get(self):
        return {'hello':'word'}

api.add_resource(H, '/')
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
from api import api,HR
from viewsnew import app
if __name__ == '__main__':
    api.add_resource(HR, '/HR/<table>')
    app.run(host='127.0.0.1', debug=True)
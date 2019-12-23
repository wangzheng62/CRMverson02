from api import api,HR,DC
from loginhistoru import app
if __name__ == '__main__':
    api.add_resource(HR, '/HR/<table>')
    api.add_resource(DC, '/DC/<table>')
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.run(host='127.0.0.1', debug=True)
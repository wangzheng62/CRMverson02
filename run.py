
from loginhistoru import app
import api
if __name__ == '__main__':
    #view=LoginView.as_view('loginfirst',url='/api/DC/em')
    #app.add_url_rule('/loginfirst',view_func=view)

    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.run(host='127.0.0.1', debug=True)
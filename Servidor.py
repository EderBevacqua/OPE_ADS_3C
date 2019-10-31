from flask import Flask, jsonify, request, render_template
from equipamentos_api import equipamentos_app
#from professores_api import professores_app
import requests as Req
import infra.equipamentos_db as equipamentos_db
#import infra.professores_db as professores_db
app = Flask(__name__)
app.register_blueprint(equipamentos_app)
#app.register_blueprint(professores_app)
@app.route('/')
def all():
    equipamentos = Req.get("http://localhost:5000/equipamentos").json()
    #professores = Req.get("http://localhost:5000/professores").json()
    return render_template("index.html", equipamentos=equipamentos)

equipamentos_db.init()
#professores_db.init()
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

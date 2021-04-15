"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Persona, Padres
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/all', methods=['GET'])
def getAllbyAge():
    #  Retorna los miembros ordenados por edad
    personas = Persona.getAllbyAge()
    #Persona.query.order_by(Persona.age.desc()).all()
    print(personas)
    return jsonify(personas), 200

@app.route('/member/<int:id>', methods=['GET'])
def getMember(id):
    padres = Padres.query.filter_by(id_hijo=id)
    return jsonify(serialize(user)), 200      

@app.route('/persona/relacion', methods=['POST'])
def crearRelacion():
    body = request.get_json() # get the request body content
    nuevaRelacion = Padres(id_padre=body['id_padre'], id_hijo=body['id_hijo'])
    db.session.add(nuevaRelacion)
    db.session.commit()
    return jsonify(serialize(nuevaRelacion)), 200    


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

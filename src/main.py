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
from models import db, User
from models import db, People
from models import db, Planets
from models import db, Favorites
# from models import Person

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


@app.route('/user', methods=['GET'])
def handle_hello():

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200


@app.route('/user', methods=['POST'])
def create_user():

    request_body_user = request.get_json()
    new_user = User(first_name=request_body_user["first_name"],
                    email=request_body_user["email"], password=request_body_user["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(request_body_user), 200


@app.route('/user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    request_body_user = request.get_json()
    new_user = User.query.get(user_id)
    if new_user is None:
        raise APIException("User not found", status_code=404)
    if "username" in request_body_user:
        new_user.username = body["username"]
    if "email" in request_body_user:
        new_user.email = body["email"]
    if "first_name" in request_body_user:
        new_user.first_name = request_body_user["first_name"]
    db.session.commit()

    return jsonify(request_body_user), 200


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    user1 = User.query.get(user_id)
    if user1 is None:
        raise APIException("user not found", status_code=404)
    db.session.delete(user1)
    db.session.commit()

    return jsonify("deleted"), 200


@app.route('/people', methods=['GET'])
def handle_people():

    people = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people))

    return jsonify(all_people), 200


@app.route('/people', methods=['POST'])
def create_person():

    request_body_user = request.get_json()
    new_person = People(name=request_body_user["name"], hair_color=request_body_user["hair_color"],
                        height=request_body_user["height"], mass=request_body_user["mass"])
    db.session.add(new_person)
    db.session.commit()
    return jsonify(request_body_user), 200


@app.route('/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = People.query.get(person_id)
    if person is None:
        raise APIException("user not found", status_code=404)
    one_person = person.serialize()

    db.session.commit()

    return(jsonify(one_person)), 200


@app.route('/planets', methods=['GET'])
def handle_planets():

    planets = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))

    return jsonify(all_planets), 200


@app.route('/planets', methods=['POST'])
def create_planet():

    request_body_user = request.get_json()
    new_planet = Planets(planet_name=request_body_user["planet_name"],
                         population=request_body_user["population"], planet_mass=request_body_user["planet_mass"])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(request_body_user), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException("planet not found", status_code=404)
    one_planet = planet.serialize()

    db.session.commit()

    return(jsonify(one_planet)), 200


@app.route('/user/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorites.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorites))

    return jsonify(all_favorites), 200


@app.route('/user/favorites', methods=['POST'])
def create_favorites():
    request_body_user = request.get_json()
    new_favorite = Favorites(
        person_id=request_body_user["person_id"], planet_id=request_body_user["planet_id"])
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(request_body_user), 200


@app.route('/user/favorites/<int:favorites_id>', methods=['DELETE'])
def delete_favorite(favorites_id):
    favorite = Favorites.query.get(favorites_id)
    if favorite is None:
        raise APIException("user not found", status_code=404)
    db.session.delete(favorite)
    db.session.commit()

    return jsonify("deleted"), 200
     



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

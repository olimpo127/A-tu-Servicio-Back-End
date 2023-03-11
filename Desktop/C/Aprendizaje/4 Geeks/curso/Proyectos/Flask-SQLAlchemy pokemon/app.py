from flask import Flask,request, jsonify
from models import db, User, Pokemon, Favorite, Stat #, Feature

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "Hello SQLAlchemy y Flask OJEDA HERE"


@app.route("/users", methods=["POST"])
def create_user():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    user.age = request.json.get("age")
    user.nickname = request.json.get("nickname")

    db.session.add(user)
    db.session.commit()

    return "User created"

@app.route("/pokemon", methods=["POST"])
def create_pokemon():
    pokemon = Pokemon()
    pokemon.pokemon_id = request.json.get("pokemon_id")
    pokemon.name = request.json.get("name")
    pokemon.is_favorite = request.json.get("is_favorite")

    db.session.add(pokemon)
    db.session.commit()

    return "Pokemon created"

@app.route("/favorites", methods=["POST"])
def create_favorite():
    favorite = Favorite()
    favorite.pokemon_id = request.json.get("pokemon_id")
    favorite.name = request.json.get("name")

    db.session.add(favorite)
    db.session.commit()

    return "Favorite Pokemon added"

#@app.route("/feature", methods=["POST"])
#def create_feature():
    #feature = Feature()
    #feature.pokemon_id = request.json.get("pokemon_id")
    #feature.name = request.json.get("name")
    #feature.type1 = request.json.get("type1")
    #feature.type2 = request.json.get("type2")
    #feature.height = request.json.get("height")
    #feature.weight = request.json.get("weight")
    #feature.ability1 = request.json.get("ability1")
    #feature.ability2 = request.json.get("ability2")
    #feature.ability3 = request.json.get("ability3")

    #db.session.add(feature)
    #db.session.commit()

    #return "Pokemon features added"

@app.route("/stats", methods=["POST"])
def create_stats():
    stat = Stat()
    stat.pokemon_id = request.json.get("pokemon_id")
    stat.name = request.json.get("name")
    stat.hp = request.json.get("hp")
    stat.attack = request.json.get("attack")
    stat.defense = request.json.get("defense")
    stat.special_atk = request.json.get("special_atk")
    stat.special_def = request.json.get("special_def")
    stat.speed = request.json.get("speed")

    db.session.add(stat)
    db.session.commit()

    return "Pokemon stats added"

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@app.route("/pokemon/list", methods=["GET"])
def get_pokemons():
    pokemons = Pokemon.query.all()
    result = []
    for pokemon in pokemons:
        result.append(pokemon.serialize())
    return jsonify(result)

@app.route("/favorites/list", methods=["GET"])
def get_favorites():
    favorites = Favorite.query.all()
    result = []
    for favorite in favorites:
        result.append(favorite.serialize())
    return jsonify(result)

#feature get method pending, first sove the post method
#@app.route("/favorites/list", methods=["GET"])
#def get_favorites():
    #favorites = Favorite.query.all()
    #result = []
    #for favorite in favorites:
        #result.append(favorite.serialize())
    #return jsonify(result)

@app.route("/stats/list", methods=["GET"])
def get_stats():
    stats = Stat.query.all()
    result = []
    for stat in stats:
        result.append(stat.serialize())
    return jsonify(result)


@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            user.username = request.json.get("username")
            user.password = request.json.get("password")
            user.age = request.json.get("age")
            user.nickname = request.json.get("nickname")
            
            db.session.commit()
            
            return jsonify("User updated"), 200
    
    return jsonify("User not found"), 418

@app.route("/pokemon/<int:id>", methods=["PUT", "DELETE"])
def update_pokemon(id):
    pokemon = Pokemon.query.get(id)
    if pokemon is not None:
        if request.method == "DELETE":
            db.session.delete(pokemon)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            pokemon.pokemon_id = request.json.get("pokemon_id")
            pokemon.name = request.json.get("name")
            pokemon.is_favorite = request.json.get("is_favorite")
            
            db.session.commit()
            
            return jsonify("Pokemon updated"), 200
    
    return jsonify("Pokemon not found"), 418

@app.route("/favorites/<int:id>", methods=["PUT", "DELETE"])
def update_favorites(id):
    favorite = Favorite.query.get(id)
    if favorite is not None:
        if request.method == "DELETE":
            db.session.delete(favorite)
            db.session.commit()

            return jsonify("Favorite deleted"), 204
        else:
            favorite.pokemon_id = request.json.get("pokemon_id")
            favorite.name = request.json.get("name")
            
            db.session.commit()
            
            return jsonify("Favorite updated"), 200
    
    return jsonify("Favorite not found"), 418

@app.route("/stats/<int:id>", methods=["PUT", "DELETE"])
def update_stats(id):
    stat = Stat.query.get(id)
    if stat is not None:
        if request.method == "DELETE":
            db.session.delete(stat)
            db.session.commit()

            return jsonify("Stats deleted"), 204
        else:
            stat.pokemon_id = request.json.get("pokemon_id")
            stat.name = request.json.get("name")
            stat.hp = request.json.get("hp")
            stat.attack = request.json.get("attack")
            stat.defense = request.json.get("defense")
            stat.special_atk = request.json.get("special_atk")
            stat.special_def = request.json.get("special_def")
            stat.speed = request.json.get("speed")
            
            db.session.commit()
            
            return jsonify("Stats updated"), 200
    
    return jsonify("Stats not found"), 418


with app.app_context():
    db.create_all()



app.run(host="localhost", port="5000")
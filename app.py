from flask import Flask, request, jsonify
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "OJEDA HERE"


@app.route("/users", methods=["POST"])
def create_user():
    user = User()
    user.name = request.json.get("name")
    user.lastname = request.json.get("lastname")
    user.username = request.json.get("username")
    user.email = request.json.get("email")
    user.password = request.json.get("password")
    user.picture = request.json.get("picture")

    db.session.add(user)
    db.session.commit()

    return "User created"

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if user is not None:
        return jsonify({
            "name": user.name,
            "lastname": user.lastname,
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "picture": user.picture
            })
    else:
        return jsonify({"message": f"User with ID {id} not found."}), 404



@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            user.name = request.json.get("name")
            user.lastname = request.json.get("lastname")
            user.username = request.json.get("username")
            user.email = request.json.get("email")
            user.password = request.json.get("password")
            user.picture = request.json.get("picture")
            
            db.session.commit()
            
            return jsonify("User updated"), 200
    
    return jsonify("User not found"), 418

with app.app_context():
    db.create_all()

app.run(host="localhost", port="5000")
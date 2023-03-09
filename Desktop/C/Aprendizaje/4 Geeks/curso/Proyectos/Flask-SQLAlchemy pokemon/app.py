from flask import Flask,request, jsonify
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "Hello SQLAlchemy y Flask"

@app.route("/users", methods=["POST"])
def create_user():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    user.age = request.json.get("age")

    db.session.add(user)
    db.session.commit()

    return "Usuario guardado"

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            user.age = request.json.get("age")
            
            db.session.commit()
            
            return jsonify("Usuario actualizado"), 200
    
    return jsonify("Usuario no encontrado"), 418


with app.app_context():
    db.create_all()


app.run(host="localhost", port="8080")
from flask import Flask, request, jsonify
from models import db, User, Service, History

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "OJEDA HERE!!"

#------------------------------------#USERS---------------------------------------------------------
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

    return "User created!"

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@app.route("/users/<int:id>", methods=["GET"])
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



#------------------------------------#Services---------------------------------------------------------
@app.route("/services", methods=["POST"])
def create_service():
    service = Service()
    service.user_id = request.json.get("user_id")
    service.service_description = request.json.get("service_description")
    service.price = request.json.get("price")
    service.mobileNumber = request.json.get("mobileNumber")
    service.city = request.json.get("city")
    service.comuna = request.json.get("comuna")
    service.street = request.json.get("street")
    service.socialNetworks = request.json.get("socialNetworks")
    service.image = request.json.get("image")

    db.session.add(service)
    db.session.commit()

    return "Service created!"    

@app.route("/services/list", methods=["GET"])
def get_services():
    services = Service.query.all()
    result = []
    for service in services:
        result.append(service.serialize())
    return jsonify(result)

@app.route("/services/<int:id>", methods=["GET"])
def get_service(id):
    service = Service.query.get(id)
    if service is not None:
        return jsonify({
            "service_id": service.service_id,
            "service_description": service.service_description,
            "price": service.price,
            "mobileNumber": service.mobileNumber,
            "city": service.city,
            "comuna": service.comuna,
            "street": service.street,
            "socialNetworks": service.socialNetworks,
            "image": service.image
            })
    else:
        return jsonify({"message": f"Service with ID {id} not found."}), 404

@app.route("/services/<int:id>", methods=["PUT", "DELETE"])
def update_service(id):
    service = Service.query.get(id)
    if service is not None:
        if request.method == "DELETE":
            db.session.delete(service)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            service.user_id = request.json.get("user_id")
            service.service_description = request.json.get("service_description")
            service.price = request.json.get("price")
            service.mobileNumber = request.json.get("mobileNumber")
            service.city = request.json.get("city")
            service.comuna = request.json.get("comuna")
            service.street = request.json.get("street")
            service.socialNetworks = request.json.get("socialNetworks")
            service.image = request.json.get("image")
            
            db.session.commit()
            
            return jsonify("Service updated"), 200
    
    return jsonify("Service not found"), 418
    


#------------------------------------#History---------------------------------------------------------
@app.route("/histories", methods=["POST"])
def create_history():
    history = History()
    history.user_id_seller = request.json.get("user_id_seller")
    history.user_id_buyer = request.json.get("user_id_buyer")
    history.transaction_id = request.json.get("transaction_id")
   
    db.session.add(history)
    db.session.commit()

    return "History created!"

@app.route("/histories/list", methods=["GET"])
def get_histories():
    histories = History.query.all()
    result = []
    for history in histories:
        result.append(history.serialize())
    return jsonify(result)

@app.route("/histories/<int:id>", methods=["GET"])
def get_history(id):
    history = History.query.get(id)
    if history is not None:
        return jsonify({
            "user_id_seller": history.user_id_seller,
            "user_id_buyer": history.user_id_buyer,
            "transaction_id": history.transaction_id
            })
    else:
        return jsonify({"message": f"History with ID {id} not found."}), 404


@app.route("/histories/<int:id>", methods=["PUT", "DELETE"])
def update_history(id):
    history = History.query.get(id)
    if history is not None:
        if request.method == "DELETE":
            db.session.delete(history)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            history.user_id_seller = request.json.get("user_id_seller")
            history.user_id_buyer = request.json.get("user_id_buyer")
            history.transaction_id = request.json.get("transaction_id")
           
            
            db.session.commit()
            
            return jsonify("History updated"), 200
    
    return jsonify("Service not found"), 418

with app.app_context():
    db.create_all()

app.run(host="localhost", port="5000")
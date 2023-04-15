import os
from flask import Flask, request, jsonify, send_from_directory
from models import db, User, Service, History, Message, Transaction
from flask_cors import  CORS
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt, generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_cors import CORS

upload_folder = os.path.join('static', 'uploads')
app = Flask(__name__)
app.config ['UPLOAD'] = upload_folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['JWT_SECRET_KEY'] = "atuservicio"
db.init_app(app)

migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt = Bcrypt(app) 
CORS(app)

CORS(app)
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
    password = request.json.get("password")
    password_hash = generate_password_hash(password)
    user.password = password_hash
    user.picture = request.json.get("picture")

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User Created"}), 200

@app.route("/users/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    user = User.query.filter_by(username=username).first()
    is_valid=None 
    if user is not None:
        is_valid = check_password_hash(user.password, password)
        
    if is_valid:
            access_token = create_access_token(identity=username)
            return jsonify({
                "token":access_token,
                "id":user.id 
            }),200
    else:
            return jsonify({
                "msg":"User or password not exist or not valid"
            }), 400

@app.route("/users/avatar/<int:id>",methods=["POST", "GET"])
def upload_file(id):
    if request.method =="GET":
        user = User.query.get(id)
        avatar = user.picture
        return send_from_directory(app.config['UPLOAD'],avatar)
    else:
        if 'file' not in request.files:
            return jsonify({'error':'no files selected'}), 400
        else:
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD'],filename))
            user = User.query.get(id)
            user.picture = filename
            db.session.commit()
            return jsonify({
                "msg": "image saved"
            }),200

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
    print(user.name)
    if user is not None:
        return jsonify({
           "id": user.id,
            "name": user.name,
            "lastname": user.lastname,
            "username": user.username,
            "email": user.email,
            "picture": user.picture
            })
    else:
        return jsonify({"message": "User with ID {id} not found."}), 404



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
    service.title = request.json.get("title")
    service.price = request.json.get("price")
    service.category = request.json.get("category")
    service.availability = request.json.get("availability")
    service.adress = request.json.get("adress")
    service.mobile_number =request.json.get("mobile_number")
    service.service_description = request.json.get("service_description")
    

    db.session.add(service)
    db.session.commit()

    return ({"message": "service Created"}), 200    

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
            "mobile_number": service.mobile_number,
            "adress": service.adress,
            "title": service.title,
           
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
            service.mobile_number = request.json.get("mobile_number")
            service.adress = request.json.get("adress")
            service.title = request.json.get("title")
              
          
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
    
    return jsonify("History not found"), 418


#------------------------------------#Messages---------------------------------------------------------

@app.route("/messages", methods=["POST"])
def create_message():
    message = Message()
    message.user_id_seller = request.json.get("user_id_seller")
    message.user_id_buyer = request.json.get("user_id_buyer")
    message.service_id = request.json.get("service_id")
    message.text = request.json.get("text")
   
    db.session.add(message)
    db.session.commit()

    return "Message created!"

@app.route("/messages/list", methods=["GET"])
def get_messages():
    messages = Message.query.all()
    result = []
    for message in messages:
        result.append(message.serialize())
    return jsonify(result)

@app.route("/messages/<int:id>", methods=["GET"])
def get_message(id):
    message = Message.query.get(id)
    if message is not None:
        return jsonify({
            "user_id_seller": message.user_id_seller,
            "user_id_buyer": message.user_id_buyer,
            "service_id": message.service_id,
            "text": message.text
            })
    else:
        return jsonify({"message": f"Message with ID {id} not found."}), 404


@app.route("/messages/<int:id>", methods=["PUT", "DELETE"])
def update_message(id):
    message = Message.query.get(id)
    if message is not None:
        if request.method == "DELETE":
            db.session.delete(message)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            message.user_id_seller = request.json.get("user_id_seller")
            message.user_id_buyer = request.json.get("user_id_buyer")
            message.service_id = request.json.get("service_id")
            message.text = request.json.get("text")
            
            db.session.commit()
            
            return jsonify("Message updated"), 200
    
    return jsonify("Message not found"), 418

#------------------------------------#Transactions---------------------------------------------------------

@app.route("/transactions", methods=["POST"])
def create_transaction():
    transaction = Transaction()
    transaction.user_id_seller = request.json.get("user_id_seller")
    transaction.user_id_buyer = request.json.get("user_id_buyer")
    transaction.service_id = request.json.get("service_id")
    transaction.status = request.json.get("status")
    transaction.rating = request.json.get("rating")
    transaction.rating_text = request.json.get("rating_text")
   
    db.session.add(transaction)
    db.session.commit()

    return "Transaction created!"

@app.route("/transactions/list", methods=["GET"])
def get_transactions():
    transactions = Transaction.query.all()
    result = []
    for transaction in transactions:
        result.append(transaction.serialize())
    return jsonify(result)

@app.route("/transactions/<int:id>", methods=["GET"])
def get_transaction(id):
    transaction = Transaction.query.get(id)
    if transaction is not None:
        return jsonify({
            "user_id_seller": transaction.user_id_seller,
            "user_id_buyer": transaction.user_id_buyer,
            "service_id": transaction.service_id,
            "status": transaction.status,
            "rating": transaction.rating,
            "rating_text": transaction.rating_text
            })
    else:
        return jsonify({"message": f"Transaction with ID {id} not found."}), 404

@app.route("/transactions/<int:id>", methods=["PUT", "DELETE"])
def update_transaction(id):
    transaction = Transaction.query.get(id)
    if transaction is not None:
        if request.method == "DELETE":
            db.session.delete(transaction)
            db.session.commit()

            return jsonify("Deleted"), 204
        else:
            transaction.user_id_seller = request.json.get("user_id_seller")
            transaction.user_id_buyer = request.json.get("user_id_buyer")
            transaction.service_id = request.json.get("service_id")
            transaction.status = request.json.get("status")
            transaction.rating = request.json.get("rating")
            transaction.rating_text = request.json.get("rating_text")

            db.session.commit()
            
            return jsonify("Transaction updated"), 200
    
    return jsonify("Transaction not found"), 418

#with app.app_context():
 #   db.create_all()

#------------------------------------#Actualizar Profile---------------------------------------------------------

@app.route("/actualizar_user/<int:id>" , methods=["PUT"])
def actualizar_user(id):
    #hola = request.get_json()
    #usuario = User.query.filter(email=)
    user=User.query.get(id)
    if user is not None:
        user.name=request.json.get("name")
        user.username=request.json.get("username")
        user.email=request.json.get("email")
        db.session.commit()
        return jsonify("Perfil Actualizado!")

    return "Perfil No Encontrado"

@app.route("/actualizar_password/<int:id>" , methods=["PUT"])
def actualizar_password(id):
    #hola = request.get_json()
    #usuario = User.query.filter(email=)
    user=User.query.get(id)
    password=request.get_json()
    print(password)
    if user is not None:
        user.password=request.json.get("contraseña")
        #user.password=request.get_json()
        db.session.commit()
        return jsonify("Contraseña Actualizada!")

    return "Perfil No Encontrado"



@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    #hola = request.get_json()
    #usuario = User.query.filter(email=)
    user=User.query.get(id)
    if user is not None:
       db.session.delete(user)
       db.session.commit()
       return "Perfil Eliminado"

    return "Perfil No Encontrado"




if __name__== "__main__":
    app.run(host="localhost", port="5000", debug=True)
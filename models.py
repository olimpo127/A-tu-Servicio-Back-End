from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email =db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    picture = db.Column(db.String(10000))
    def serialize(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "picture": self.picture
        }

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, foreign_key=True)
    title =db.Column(db.String(200))
    service_description = db.Column(db.String(200))
    price = db.Column(db.String(20))
    mobileNumber = db.Column(db.String(20))
    adress = db.Column(db.String(20))
    image = db.Column(db.String(20))
    def serialize(self):
        return {
            "service_id": self.service_id,
            "title": self.title,
            "service_description": self.service_description,
            "price": self.price,
            "mobileNumber": self.mobileNumber,
            "adress": self.adress,
            "image": self.image
         }

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    user_id_seller = db.Column(db.Integer, foreign_key=True)
    user_id_buyer = db.Column(db.Integer, foreign_key=True)
    transaction_id = db.Column(db.String(50), nullable=False)
    def serialize(self):
        return {
            "user_id_seller": self.user_id_seller,
            "user_id_buyer": self.user_id_buyer,
            "transaction_id": self.transaction_id
        }

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    user_id_seller = db.Column(db.Integer, foreign_key=True)
    user_id_buyer = db.Column(db.Integer, foreign_key=True)
    service_id = db.Column(db.Integer, foreign_key=True)
    text = db.Column(db.String(200))
    def serialize(self):
        return {
            "user_id_seller": self.user_id_seller,
            "user_id_buyer": self.user_id_buyer,
            "service_id": self.service_id,
            "text": self.text
        }

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id_seller = db.Column(db.Integer, foreign_key=True)
    user_id_buyer = db.Column(db.Integer, foreign_key=True)
    service_id = db.Column(db.Integer, foreign_key=True)
    status = db.Column(db.String(20))
    rating  = db.Column(db.Integer)
    rating_text = db.Column(db.String(200))
    def serialize(self):
        return {
            "user_id_seller": self.user_id_seller,
            "user_id_buyer": self.user_id_buyer,
            "service_id": self.service_id,
            "status": self.status,
            "rating": self.rating,
            "rating_text": self.rating_text
        }
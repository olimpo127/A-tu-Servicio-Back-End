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
    service_description = db.Column(db.String(200))
    price = db.Column(db.String(20))
    mobileNumber = db.Column(db.String(20))
    city = db.Column(db.String(20))
    comuna = db.Column(db.String(20))
    street = db.Column(db.String(20))
    socialNetworks = db.Column(db.String(50))
    image = db.Column(db.String(20))
    def serialize(self):
        return {
            "service_id": self.service_id,
            "service_description": self.service_description,
            "price": self.price,
            "mobileNumber": self.mobileNumber,
            "city": self.city,
            "comuna": self.comuna,
            "street": self.street,
            "socialNetworks": self.socialNetworks,
            "image": self.image
         }


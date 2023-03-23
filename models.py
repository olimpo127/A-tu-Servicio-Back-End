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




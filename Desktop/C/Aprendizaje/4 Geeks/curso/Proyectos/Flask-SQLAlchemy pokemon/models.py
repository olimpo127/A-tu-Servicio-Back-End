from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)

    def serialize(self):
        return {
            "username": self.username,
            "id": self.id,
            "age": self.age
        }
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    nickname = db.Column(db.String(20))
    favorite = db.relationship("Favorite")
    def serialize(self):
        return {
            "username": self.username,
            "id": self.id,
            "age": self.age,
            "nickname": self.nickname
        }

class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer)
    name = db.Column(db.String(50), nullable=False)
    is_favorite = db.Column(db.Boolean)
    #feature = db.relationship("Feature")
    stat = db.relationship("Stat")
    favorite = db.relationship("Favorite")
    def serialize(self):
        return {
            "pokemon_id": self.pokemon_id,
            "name": self.name,
            "is_favorite": self.is_favorite
        }

class Favorite(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.pokemon_id"))
    name = db.Column(db.String(50), nullable=False) 
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    def serialize(self):
        return {
            "pokemon_id": self.pokemon_id,
            "name": self.name,
        }

#class Feature(db.Model):
    #__tablename__ = "feature"
    #id = db.Column(db.Integer, primary_key=True)
    #pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.pokemon_id"))
    #name = db.Column(db.String(50), nullable=False)
    #type1 = db.Column(db.String(20), nullable=False)
    #type2 = db.Column(db.String(20))
    #height = db.Column(db.Integer)
    #weight = db.Column(db.Integer)
    #ability1 = db.Column(db.String(50), nullable=False)
    #ability2 = db.Column(db.String(50))
    #ability3 = db.Column(db.String(50))
    #def serialize(self):
        #return {
            #"pokemon_id": self.pokemon_id,
            #"name": self.name,
            #"type1": self.type1,
            #"type2": self.type2,
            #"height": self.height,
            #"weight": self.weight,
            #"ability1": self.ability1,
            #"ability2": self.ability2,
            #"ability3": self.ability3
        #}

class Stat(db.Model):
    __tablename__ = "stat"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.pokemon_id"))
    name = db.Column(db.String(50), nullable=False) 
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_atk = db.Column(db.Integer, nullable=False)
    special_def = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    def serialize(self):
        return {
            "pokemon_id": self.pokemon_id,
            "name": self.name,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "special_atk": self.special_atk,
            "special_def": self.special_def,
            "speed": self.speed
        }


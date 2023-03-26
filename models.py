
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
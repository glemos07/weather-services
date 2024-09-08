from app import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())
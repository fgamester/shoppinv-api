from .db import db

class Tier(db.Model):
    __tablename__ = 'tiers'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
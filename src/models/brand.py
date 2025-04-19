from .db import db

class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=True)
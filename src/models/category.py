from .db import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
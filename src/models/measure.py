from .db import db

class Measure(db.Model):
    __tablename__ = 'measures'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    integer = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String(100), nullable=True)
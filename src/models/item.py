from .db import db

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    category_id = db.Column(db.String, db.ForeignKey('categories.id'), nullable=False)
    measure_id = db.Column(db.String, db.ForeignKey('measures.id'), nullable=False)
    min_stock = db.Column(db.Numeric(10,3), nullable=True)
    name = db.Column(db.String(100), nullable=False)
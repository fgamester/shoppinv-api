from .db import db

class Presentation(db.Model):
    __tablename__ = 'presentations'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    item_id = db.Column(db.String, db.ForeignKey('items.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    brand_id = db.Column(db.String, db.ForeignKey('brands.id'), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String, nullable=True)
    min_stock = db.Column(db.Numeric(10,3), nullable=True)
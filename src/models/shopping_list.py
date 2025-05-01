from datetime import datetime
from .db import db

class ShoppingList(db.Model):
    __tablename__ = 'shopping_lists'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    done = db.Column(db.Boolean, nullable=False, default=False)
    shopping_date = db.Column(db.Date, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
from datetime import datetime
from .db import db

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    inventory_id = db.Column(db.String, db.ForeignKey('inventories.id'), nullable=False, primary_key=True)
    item_id = db.Column(db.String, db.ForeignKey('items.id'), nullable=False, primary_key=True)
    quantity = db.Column(db.Numeric(10, 3), nullable=False, default=1.000)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.now)
    active = db.Column(db.Boolean, nullable=False, default=True)
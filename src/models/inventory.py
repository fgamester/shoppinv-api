from datetime import datetime
from .db import db

class Inventory(db.Model):
    __tablename__ = 'inventories'
    id = db.Column(db.String, nullable=False, primary_key=True)
    entity_id = db.Column(db.String, db.ForeignKey('entities.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    open = db.Column(db.Boolean, nullable=False, default=True)
    end_date = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
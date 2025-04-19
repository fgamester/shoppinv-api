from datetime import datetime
from .db import db

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.String, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    sync_token = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
from datetime import datetime
from .db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, nullable=False, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    sync_token = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
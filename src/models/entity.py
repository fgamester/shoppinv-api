from .db import db

class Entity(db.Model):
    __tablename__ = 'entities'
    id = db.Column(db.String, nullable=False, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=True)
    group_id = db.Column(db.String, db.ForeignKey('groups.id'), nullable=True)
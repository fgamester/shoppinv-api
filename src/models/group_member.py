from datetime import datetime
from .db import db

class GroupMember(db.Model):
    __tablename__ = 'group_members'
    group_id = db.Column(db.String, db.ForeignKey('groups.id'), nullable=False, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    tier_id = db.Column(db.Integer, db.ForeignKey('tiers.id'), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    active = db.Column(db.Boolean, nullable=False, default=True)
    kicked_by = db.Column(db.String, db.ForeignKey('users.id'), nullable=True)
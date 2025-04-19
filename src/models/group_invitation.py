from .db import db

class Group_Invitation(db.Model):
    __tablename__ = 'group_invitations'
    group_id = db.Column(db.String, db.ForeignKey('groups.id'), nullable=False, primary_key=True )
    to_user = db.Column(db.String, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    from_user = db.Column(db.String, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    tier_id = db.Column(db.Integer, db.ForeignKey('tiers.id'), nullable=False)
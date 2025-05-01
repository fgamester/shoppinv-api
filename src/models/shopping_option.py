from .db import db

class ShoppingOption(db.Model):
    __tablename__ = 'shopping_options'
    list_id = db.Column(db.String, db.ForeignKey('shopping_lists.id'), nullable=False, primary_key=True)
    item_id = db.Column(db.String, db.ForeignKey('items.id'), nullable=False, primary_key=True)
    option_id = db.Column(db.String, db.ForeignKey('presentations.id'), nullable=False, primary_key=True)
    option_number = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Numeric(10, 3), nullable=True)
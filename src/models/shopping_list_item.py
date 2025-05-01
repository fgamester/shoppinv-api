from .db import db

class ShoppingListItem(db.Model):
    __tablename__ = 'shopping_list_items'
    list_id = db.Column(db.String, db.ForeignKey('shopping_lists.id'), nullable=False, primary_key=True)
    item_id = db.Column(db.String, db.ForeignKey('items.id'), nullable=False, primary_key=True)
    recommended_quantity = db.Column(db.Numeric(10, 3), nullable=False, default=1.000)
    quantity = db.Column(db.Numeric(10, 3), nullable=True)
    first_option = db.Column(db.String, db.ForeignKey('presentations.id'), nullable=True)
    second_option = db.Column(db.String, db.ForeignKey('presentations.id'), nullable=True)
    third_option = db.Column(db.String, db.ForeignKey('presentations.id'), nullable=True)
    ready = db.Column(db.Boolean, nullable=False, default=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model

class Item(Model):
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    orders = relationship('Order', secondary='order_item', backref='items') # many to many

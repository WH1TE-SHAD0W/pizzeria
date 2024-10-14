from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model


class Order(Model):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    user = relationship('User', back_populates='orders')
    items = relationship('Item', secondary='item_order', backref='orders') # many to many

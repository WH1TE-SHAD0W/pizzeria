from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model


class Topping(Model):
    __tablename__ = 'toppings'
    topping_id = Column(Integer, primary_key=True)
    pizza_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    pizza = relationship('Pizza', back_populates='toppings')

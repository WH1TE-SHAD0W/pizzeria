from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model


class Pizza(Model):
    __tablename__ = 'pizzas'
    pizza_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    order = relationship('Order', back_populates='pizzas')

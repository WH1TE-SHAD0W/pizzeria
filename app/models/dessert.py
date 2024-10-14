from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model


class Dessert(Model):
    __tablename__ = 'desserts'
    dessert_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    order = relationship('Order', back_populates='desserts')

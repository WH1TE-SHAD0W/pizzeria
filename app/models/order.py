from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship

from app.models.model import Model


class Order(Model):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, nullable=False)
    # foods = relationship('Food', secondary=order_food, backref='orders')

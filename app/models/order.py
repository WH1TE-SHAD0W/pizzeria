from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model


class Order(Model):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    # user = relationship('User', back_populates='orders')
    def __init__(self, order_id):
        super().__init__(datetime.now())
        self.order_id = order_id


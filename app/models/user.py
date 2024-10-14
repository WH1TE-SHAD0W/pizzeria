from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.model import Model


class User(Model):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    orders = relationship('Order', back_populates='user')

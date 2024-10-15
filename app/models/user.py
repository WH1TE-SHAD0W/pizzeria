from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.model import Model


class User(Model):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    orders = relationship('Order', back_populates='user')

    def __init__(self, user_id, email, password, is_active, is_authenticated):
        super().__init__(datetime.now())
        self.user_id = user_id
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_authenticated = is_authenticated

    def get_id(self):
        return self.user_id


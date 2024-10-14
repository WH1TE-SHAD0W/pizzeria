from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship

from app.models.model import Model

class Item(Model):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)

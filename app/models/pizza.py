from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Model



class Pizza(Model):
    from app.models.topping import Topping
    __tablename__ = 'pizzas'
    pizza_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    size = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    toppings = relationship('Topping', secondary='pizza_toppings', back_populates='pizzas')

    def __init__(self, name, size, price):
        super().__init__(datetime.now())

        self.name = name
        self.size = size
        self.price = price


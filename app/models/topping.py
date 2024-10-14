from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.model import Model
from app.models.pizza_topping import PizzaTopping

class Topping(Model):
    __tablename__ = 'toppings'
    topping_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    pizzas = relationship('Pizza', secondary='pizza_toppings', back_populates='toppings')
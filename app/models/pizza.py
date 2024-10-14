from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Model
from app.models.pizza_topping import PizzaTopping



class Pizza(Model):
    __tablename__ = 'pizzas'
    pizza_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    size = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    toppings = relationship('Topping', secondary='pizza_toppings', back_populates='pizzas')
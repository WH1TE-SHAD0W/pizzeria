from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Model

# Association table
# pizza_toppings = Table(
#     'pizza_toppings', Model.metadata,
#     Column('pizza_id', Integer, ForeignKey('pizzas.pizza_id'), primary_key=True),
#     Column('topping_id', Integer, ForeignKey('toppings.topping_id'), primary_key=True)
# )

class PizzaTopping(Model):
    __tablename__ = 'pizza_toppings'
    pizza_id = Column(Integer, ForeignKey('pizzas.pizza_id'), primary_key=True)
    topping_id = Column(Integer, ForeignKey('toppings.topping_id'), primary_key=True)
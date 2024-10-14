from datetime import datetime

from sqlalchemy.orm import sessionmaker

from app.models.drink import Drink
from app.models.topping import Topping
from app.models.pizza import Pizza
from database.migration import engine

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

def seed_drinks():
    # Clear the toppings table
    session.query(Drink).delete()
    session.commit()

if __name__ == '__main__':
    seed_drinks()
    print("Drinks seeded successfully.")
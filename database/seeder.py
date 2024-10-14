from datetime import datetime

from sqlalchemy.orm import sessionmaker
from app.models.topping import Topping
from app.models.pizza import Pizza
from database.migration import engine

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

def seed_toppings():
    # Clear the toppings table
    session.query(Topping).delete()
    session.commit()

    # Define a list of toppings
    toppings = [
        'Pepperoni', 'Mushrooms', 'Onions', 'Sausage', 'Bacon',
        'Extra cheese', 'Black olives', 'Green peppers', 'Pineapple', 'Spinach'
    ]

    # Seed the toppings
    for index, topping_name in enumerate(toppings, start=1):
        topping = Topping(
            topping_id=index,
            name=topping_name,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        session.add(topping)

    # Commit the session
    session.commit()
    print("Toppings seeded successfully.")

if __name__ == '__main__':
    seed_toppings()
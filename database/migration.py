import sqlalchemy.orm
from sqlalchemy import create_engine
import dotenvfile
import os

# Load environment variables from .env file
dotenvfile.loadfile('../.env')

print("Environment variables loaded successfully.")
# Retrieve environment variables
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')


# Create the SQLAlchemy engine
# engine = create_engine(f'mysql://{user}:{password}@{host}/{database}')
engine = create_engine(f'mysql://root:password@localhost:99/pizzeria')

print("Engine created successfully.")
print("Base created successfully.")
Base = sqlalchemy.orm.declarative_base()
def migrate_fresh():
    Base.metadata.drop_all(engine)
    from app.model import Model
    from app.models.user import User
    from app.models.order import Order
    from app.models.item import Item
    from app.models.item_order import ItemOrder
    print(Model.metadata.tables.keys())
    for table_name in Model.metadata.tables.keys():
        Base.metadata.create_all(engine, tables=[Model.metadata.tables[table_name]])
    print("Tables created successfully.")


if __name__ == '__main__':
    migrate_fresh()
    print("Migration successful.")


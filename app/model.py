from sqlalchemy import Column, Integer, DateTime

from database.migration import Base


class Model(Base):
    __abstract__ = True
    # id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

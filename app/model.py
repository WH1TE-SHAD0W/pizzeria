from sqlalchemy import Column, Integer, DateTime

from database.migration import Base


class Model(Base):
    __abstract__ = True
    # id = Column(Integer, primary_key=True)
    def __init__(self, created_at):
        self.created_at = created_at
        self.updated_at = created_at
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

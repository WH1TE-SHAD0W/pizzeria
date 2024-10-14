from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.model import Model


class ItemOrder(Model):
    __tablename__ = 'order_item'
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)

    order = relationship('Order', backref='order_item')
    item = relationship('Item', backref='order_item')
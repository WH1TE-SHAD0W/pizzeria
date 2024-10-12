import unittest
from order import Order
from orders import Orders

class TestOrders:
    def test_order_at_time(self):
        orders = Orders()
        order = Order()
        orders.add_order(order)
        assert orders.order_at_time(order.date_created) == order


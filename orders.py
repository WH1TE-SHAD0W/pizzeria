from typing import List

from order import Order


class Orders:
    def __init__(self):
        self.orders: List[Order] = []

    def order_at_time(self, date):
        for order in self.orders:
            if order.date_created == date:
                return order

    def last(self):
        return self.orders[-1]

    def add_order(self, order: Order):
        self.orders.append(order)

    def count_orders(self):
        return len(self.orders)

    def show_orders(self):
        return self.orders
from datetime import datetime

from order import Order
from pizza import Pizza


class TestOrder:

    def create_order(self):
        order = Order()
        order.add_pizza(Pizza(
            'margherita',
            'm',
            ['cheese', 'garlic', 'ham', 'corn']))
        return order

    def test_show_date(self):
        order = Order()
        assert order.show_date() == datetime.today().date()

    def test_show_pizzas(self):
        order = self.create_order()
        expected_pizzas = [('margherita', 'm', ['cheese', 'garlic', 'ham', 'corn'])]
        assert order.show_pizzas() == expected_pizzas

    def test_total_bill(self):
        order = self.create_order()
        assert order.total_bill() == 15.4

    def test_get_pizza_by_name(self):
        order = self.create_order()
        expected_string = "('margherita', 'm', ['cheese', 'garlic', 'ham', 'corn'])"
        assert order.get_pizza_by_name('margherita') == expected_string

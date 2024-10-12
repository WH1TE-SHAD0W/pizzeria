import pytest

from pizza import Pizza


class TestPizza:

    @staticmethod
    def create_pizza():
        pizza = Pizza(
            'margherita',
            'm',
            ['cheese', 'garlic', 'ham', 'corn'])
        return pizza

    # @pytest.fixture
    def test_validate_size_valid(self):
        size = 'm'
        assert Pizza.validate_size(size)

    def test_validate_size_invalid(self):
        size = 't'
        assert not Pizza.validate_size(size)

    def test_set_size_valid(self):
        pizza = Pizza('margherita')
        assert Pizza.set_size(pizza, 's')
        Pizza.set_size(pizza, 's')
        assert pizza.size == 's'

    def test_set_size_invalid(self):
        pizza = Pizza('margherita')
        assert not Pizza.set_size(pizza, 'f')

    def test_get_size(self):
        pizza = Pizza('margherita')
        expected_size = 'm'
        assert expected_size == pizza.get_size()

    def test_get_toppings_count_4(self):
        pizza = self.create_pizza()
        assert Pizza.get_toppings_count(pizza) == 4

    def test_add_topping_peperoni(self):
        pizza = self.create_pizza()
        assert pizza.add_topping('peperoni')

    def test_add_topping_duplicate(self):
        pizza = self.create_pizza()
        assert pizza.add_topping('cheese')

    def test_add_topping_over_10(self):
        pizza = Pizza(
            'margherita',
            'm',
            ['cheese', 'garlic', 'ham', 'corn', 'egg', 'peperoni', 'chips', 'chicken', 'beef', 'fungi', 'salami'])
        assert pizza.add_topping('bbq')

    def test_remove_topping_in(self):
        pizza = self.create_pizza()
        assert pizza.remove_topping('cheese')

    def test_remove_topping_not_in(self):
        pizza = self.create_pizza()
        assert not pizza.remove_topping('chese')

    def test_calc_price(self):
        pizza = self.create_pizza()
        expected_price = 15.4
        assert pizza.calc_price() == expected_price

    def test_details(self):
        pizza = self.create_pizza()
        print(pizza.details())


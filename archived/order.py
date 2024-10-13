from datetime import datetime

from pizza import Pizza


class Order:
    def __init__(self):
        self.date_created = datetime.now()
        self.pizzas = []

    def show_date(self):
        return self.date_created.date()

    def show_pizzas(self):
        return self.pizzas

    def add_pizza(self, pizza: Pizza) -> None:
        self.pizzas.append(pizza)

    def total_bill(self):
        total_bill = 0
        for pizza in self.pizzas:
            total_bill += pizza.calc_price()
        return total_bill

    def most_expensive_pizza(self) -> Pizza:
        return max(self.pizzas, key=lambda pizza: pizza.calc_price())

    def count_pizzas(self):
        return len(self.pizzas)

    def remove_pizza(self, pizza: Pizza) -> None:
        self.pizzas.remove(pizza)

    def get_pizza_by_name(self, pizza_name: str) -> Pizza:
        for pizza in self.pizzas:
            if pizza_name.lower() == pizza.name.lower():
                return pizza


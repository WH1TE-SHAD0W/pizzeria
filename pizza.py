from typing import List


class Pizza:
    def __init__(self, name: str, size: str = 'm', toppings=None):
        if toppings is None:
            toppings = ['no toppings']
        if not self.set_size(size):
            self.size = 'm'
            self.print_wrong_size()
        self.toppings: List = toppings
        self.name: str = name

    @staticmethod
    def validate_size(size):
        sizes = ['s', 'm', 'l', 'xl']
        if size in sizes:
            return True
        else:
            return False

    def set_size(self, size: str):
        if self.validate_size(size):
            self.size = size
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def get_toppings_count(self):
        return len(self.toppings)

    def add_topping(self, topping: str):
        if len(self.toppings) < 11 and topping not in self.toppings:
            self.toppings.append(topping)
            return True
        else:
            return False

    def remove_topping(self, topping: str):
        if topping in self.toppings:
            self.toppings.remove(topping)
            return True
        else:
            return False

    def calc_price(self):
        pricing: dict = {
            's': 10,
            'm': 12,
            'l': 15,
            'x': 18,
            't': 0.85,
        }
        price: float = pricing[self.size] + pricing['t']*(len(self.toppings))
        return price

    def details(self):
        return (f'Pizza named: {self.name} has toppings: {", ".join(self.toppings)} with a price-tag: {self.calc_price()} based '
                f'on a size: {self.size}')

    @staticmethod
    def print_wrong_size():
        print('This is an inappropriate size')

    def __repr__(self):
        return f'{self.name, self.size, self.toppings}'

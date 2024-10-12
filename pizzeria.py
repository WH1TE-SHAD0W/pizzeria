from datetime import date
from orders import Orders
from pizza import Pizza
from order import Order


def order_pizza(the_order):
    name = input('What name of a pizza you want?')
    size = input('What size of a pizza you want?')
    while not Pizza.validate_size(size):
        size = input('Please provide a correct size of the pizza you want, choose from (s, m, l, xl)')

    if input('Do you want any toppings?').lower() == 'yes':
        toppings = input('Write down which toppings you want').lower().split()
        pizza_to_order = Pizza(name, size, toppings)
        the_order.add_pizza(pizza_to_order)
    else:
        pizza_to_order = Pizza(name, size)
        the_order.add_pizza(pizza_to_order)


def menu():
    return ("To order a pizza type: order\n"
            "To edit an order type: edit\n"
            "To finish ordering type: finish\n"
            "To show today order details: show\n"
            )


def edit_menu():
    return ("To add a pizza topping type: add\n"
            "To edit a pizza size: size\n"
            "To change a pizza name: name\n"
            "To remove a pizza from the order type: remove\n"
            "To finish a pizza order: order\n")


def edit_pizza_from_order(order: Order):
    print('editing')
    show_details(order)
    pizza = order.get_pizza_by_name(input('What pizza you want to edit?'))
    user_input = input(edit_menu())
    while user_input != 'finish':
        match user_input:
            case "add":
                pizza.add_topping(input('What topping you want?'))
                match input('Do you want to add more toppings? if so type "y"'):
                    case 'y':
                        pizza.add_topping(input('What topping you want?'))
                    case _:
                        pass
            case "name":
                pizza.name = input('What name do you want?')
            case "size":
                size = input('What size do you want?')
                while not Pizza.validate_size(size):
                    size = input('Please provide a correct size of the pizza you want, choose from (s, m, l, xl)')
                pizza.size = size
            case "remove":
                order.remove_pizza(pizza)
            case "finish":
                pass
            case _:
                pass
        user_input = input(edit_menu())


def show_details(today_order):
    for pizza in today_order.show_pizzas():
        if len(pizza.toppings) > 1:
            print(f'You just ordered: {pizza.name} of a size '
                  f'{pizza.size.upper()} with toppings: {pizza.toppings}')
        else:
            print(f'You just ordered: {pizza.name} of a size '
                  f'{pizza.size.upper()} without toppings')


def show_price(today_order):
    for pizza in today_order.show_pizzas():
        print(f'Price of {pizza.name}, is {pizza.calc_price()}')
    print(f'The most expensive pizza name is: {today_order.most_expensive_pizza().name} '
          f'and costs {today_order.most_expensive_pizza().calc_price()}'
          )


def ordering_program(all_orders: Orders):
    while True:
        today = date.today()
        if all_orders.order_at_time(today):
            today_order = all_orders.order_at_time(today)
        else:
            today_order = Order()
        match input(menu()):
            case "order":
                order_pizza(today_order)
            case "edit":
                if today_order:
                    edit_pizza_from_order(all_orders.order_at_time(today))
                else:
                    print("No pizzas ordered today yet")
            case "show":    
                if today_order:
                    show_details(today_order)
                else:
                    print("No pizzas ordered today yet")
            case "price":
                if today_order:
                    show_price(today_order)
                else:
                    print("No pizzas ordered today yet")

            case "finish":
                all_orders.add_order(today_order)
                break
            case _:
                pass


if __name__ == '__main__':
    margarita = Pizza('margarita', 's')
    pizza1 = Pizza('quatro', 's')
    pizza2 = Pizza('fungi', 's')
    order1 = Order()
    order1.add_pizza(margarita)
    order1.add_pizza(pizza2)
    order1.add_pizza(pizza1)
    all_orders = Orders()
    all_orders.add_order(order1)
    ordering_program(all_orders)
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:

    options = menu.get_items()
    order = input(f"What would you like to drink? {options}: ")

    if order == "off":
        is_on = False

    elif order == "report":
        coffee_maker.report()

    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

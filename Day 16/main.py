from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
is_on = True


while is_on is True:
    options = menu.get_items()
    choice = input(f"What Would you like to Order? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker.report()
        money.report()
    else:
        order = menu.find_drink(choice)
        if maker.is_resource_sufficient(order):
            if money.make_payment(order.cost) is True:
                maker.make_coffee(order)




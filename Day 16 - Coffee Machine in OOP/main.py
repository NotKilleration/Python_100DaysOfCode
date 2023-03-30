from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

while is_on:
    user_input = input(f"What would you like? {Menu.get_items()} ")
    if user_input == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    elif user_input == "off":
        is_on = False
    # elif Menu.find_drink(user_input) == user_input:
    #     drink = Menu.find_drink()
    #     if CoffeeMaker.is_resource_sufficient(drink["ingredients"]):
    #         if  MoneyMachine.make_payment(drink["cost"]):
    #             CoffeeMaker.make_coffee(user_input, drink["ingredients"])
    # else:
    #    print("Something went wrong. Please try again.")
    else:
        drink = Menu.find_item(user_input)
        if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)
    
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

def is_resource_sufficient(order_ingredients):
    """Returns True if sufficient else False."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def coin_process():
    """Returns the sum of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * quarter
    total += int(input("How many Dimes?: ")) * dime
    total += int(input("How many Nickles?: ")) * nickle
    total += int(input("How many Pennies?: ")) * penny
    return total


def transaction_status(up_money, cost):
    """Returns true if transaction was Successful, else False if insufficient money"""
    if up_money >= cost:
        change = round(up_money - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

is_on = True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappucino): ")
    if user_input == "report":
        report()
    elif user_input == "off":
        is_on = False
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin_process()
            if  transaction_status(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])

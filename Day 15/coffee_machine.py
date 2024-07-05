# Seeing Already Have Resources
Total_amount = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Setting the Menu for all the coffee and the Recipe
MENU = {
    "espresso": {
        "resources": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "resources": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "resources": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "black coffee": {
        "resources": {
            "water": 150,
            "milk": 0,
            "coffee": 30,
        },
        "cost": 1.75,
     }
}


def insert_money():
    print("Please Insert Coins!")
    quart = float(input("How Many Quarters?"))
    dime = float(input("How Many Dimes?"))
    nick = float(input("How Many Nickles?"))
    penn = float(input("How Many Pennies?"))
    money_calculated = 0.01 * penn + 0.05 * nick + 0.1 * dime + 0.25 * quart
    return money_calculated


def is_resource_okay(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${Total_amount}")
    else:
        drink = MENU[choice]
        if is_resource_okay(drink["resources"]):
            payment = insert_money()
            if payment >= drink["cost"]:
                change = payment - drink["cost"]
                print(f"Here is ${change} in change.")
                Total_amount += drink["cost"]
                make_coffee(choice, drink["resources"])
            else:
                print("Sorry that's not enough money. Money refunded.")


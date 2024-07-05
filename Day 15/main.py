water = 300
milk = 200
coffee = 100
total_money = 0
turn_on = True


def insert_money():
    print("Please Insert Coins!")
    quart = float(input("How Many Quarters?"))
    dime = float(input("How Many Dimes?"))
    nick = float(input("How Many Nickles?"))
    penn = float(input("How Many Pennies?"))
    money_calculated = 0.01 * penn + 0.05 * nick + 0.1 * dime + 0.25 * quart
    return money_calculated


while turn_on is True:
    type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if type_of_coffee == "espresso":
        if water >= 50:
            water -= 50
            if coffee >= 18:
                coffee -= 18
                money = insert_money()
                if money >= 1.50:
                    change = money - 1.50
                    print(f"Here is your Change: {change.__round__(2)}")
                    print("Here is your Espresso ☕ Enjoy!")
                    total_money += 1.50

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough Coffee.")
        else:
            print("Sorry there is not enough water.")
    elif type_of_coffee == "latte":
        if water >= 200:
            water -= 200
            if coffee >= 24:
                coffee -= 24
                if milk >= 150:
                    milk -= 150
                    money = insert_money()
                    if money >= 2.50:
                        change = money - 2.50
                        print(f"Here is your Change: {change.__round__(2)}")
                        print("Here is your Latte ☕ Enjoy!")
                        total_money += 2.50
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough Milk.")
            else:
                print("Sorry there is not enough Coffee.")
        else:
            print("Sorry there is not enough Water.")
    elif type_of_coffee == "cappuccino":
        if water >= 250:
            water -= 250
            if coffee >= 24:
                coffee -= 24
                if milk >= 100:
                    milk -= 100
                    money = insert_money()
                    if money >= 3.00:
                        change = money - 3.00
                        print(f"Here is your Change: {change.__round__(2)}")
                        print("Here is your Cappuccino ☕ Enjoy!")
                        total_money += 3.00
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough Milk.")
            else:
                print("Sorry there is not enough Coffee.")
        else:
            print("Sorry there is not enough Water.")

    elif type_of_coffee == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}gm")
        print(f"Money: ${total_money}")

    elif type_of_coffee == "off":
        turn_on = False

    else:
        print("Please Enter Correct Coffee Name!!")

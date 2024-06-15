print("Welcome to the Tip Amount Calculator")

amount = float(input("How Much is your Total Bill?\n$"))
perc = int(input("How much of the Tip you want to give?\n10%, 12%, 15%?\n"))
people = int(input("How many people are splitting the Bill?\n"))
tip = round(((perc / 100 * amount) + amount) / people, 2)

print(f"Total tip amount for each customer is {tip}" )

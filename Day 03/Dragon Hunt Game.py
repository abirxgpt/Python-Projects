print("Welcome to the Dragon Hunt Game!!")
print(r'''

       ^                       ^
       |\   \        /        /|
      /  \  |\__  __/|       /  \
     / /\ \ \ _ \/ _ /      /    \
    / / /\ \ {*}\/{*}      /  / \ \
    | | | \ \( (00) )     /  // |\ \
    | | | |\ \(V""V)\    /  / | || \|
    | | | | \ |^--^| \  /  / || || ||
   / / /  | |( WWWW__ \/  /| || || ||
  | | | | | |  \______\  / / || || ||
  | | | / | | )|______\ ) | / | || ||
  / / /  / /  /______/   /| \ \ || ||
 / / /  / /  /\_____/  |/ /__\ \ \ \ \
 | | | / /  /\______/    \   \__| \ \ \
 | | | | | |\______ __    \_    \__|_| \
 | | ,___ /\______ _  _     \_       \  |
 | |/    /\_____  /    \      \__     \ |    /\
 |/ |   |\______ |      |        \___  \ |__/  \
 v  |   |\______ |      |            \___/     |
    |   |\______ |      |                    __/
     \   \________\_    _\               ____/
   __/   /\_____ __/   /   )\_,      _____/
  /  ___/  \uuuu/  ___/___)    \______/
  VVV  V        VVV  V

''')

print("Welcome to the Dragon Hunt Game!!\nYour Goal is to Kill the Dragon and Save the Princes")
armour = input('\nDo you want to Grab an Armor "Y" or "N" ')
sword = input('\nDo you want to Want to get a Sword "Y" or "N" ')
if armour == "Y":
  Health = 100
else:
  Health = 50
if sword == "Y":
  Damage = 15
else:
  Damage = 10
print(f"Health = {Health} & Damage = {Damage}")
power = input('Choose your Power Type "Fire" "Water" or "Wind"')
if power == "Fire":
  Damage += 5
elif power == "Water":
  Health += 10
else:
  Health += 5
  Damage += 3
print(f"Your Upgrades After Power \n Health = {Health} & Damage = {Damage}")

print("\nRules:\n 1. You Cannot Attack Dragon at 3rd Time \n 2. Defending will Defend your Health but Recover 10 of Dragon Health \n 3. Dragon Life at Start is 100 \n 4. If Dragon Life = 0 you will win the Game \n 5. Stand Won't Affect Anything")

DragonL = 100
count = 1
while DragonL > 0:
  pose = input('What to do? "Attack" or "Defend" or "Stand"')

  if pose == "Attack" and (count % 3) != 0:
    Health -= 10
    DragonL = DragonL - Damage
    count += 1
    print(f"\nYour Health: {Health} \nDragon's Life: {DragonL} \nNo of Chances: {count}")
  elif pose == "Defend":
    Health += 7
    DragonL += 10
    count += 1
    print(f"\nYour Health: {Health} \nDragon's Life: {DragonL}")
  elif pose == "Attack" and (count % 3) == 0:
    Health -= 50
    count = 0
    print(f"\nYour Health: {Health} \nDragon's Life: {DragonL}")
  if Health < 0:
    break
if Health < 0:
  print("You Lose!!")
elif DragonL < 0:
  print("You Won!!")
else:
  print("Game Suspended")

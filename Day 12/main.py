import random
import art
import rules

print(art.logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
is_rules = input("If you want to read rules press 'R': ")

if is_rules == "R":
    print(rules.Rules)

Number_Generated = random.randint(1,100)
Chance = 11 if difficulty == "easy" else 6

print(Number_Generated)

def easy_game(Chances):
    Guess = 0
    while Guess != Number_Generated and Chances > 1:
        print(f"You have {Chances-1} attempts remaining to guess the number.")
        Guess = int(input("Make a guess: "))
        if (Guess - Number_Generated) > 25:
            print ("Too High!!")
        elif (Guess - Number_Generated) < -25:
            print ("Too Low!!")
        elif (Guess - Number_Generated) <= 25 and (Guess - Number_Generated) > 10:
            print ("High!!")
        elif (Guess - Number_Generated) >= -25 and (Guess - Number_Generated) < -10:
            print ("Low!!")
        elif (Guess - Number_Generated) <= 10 and (Guess - Number_Generated) > 5:
            print("High, Close!!!!")
        elif (Guess - Number_Generated) >= -10 and (Guess - Number_Generated) < -5:
            print("Low, Close!!!!")
        elif (Guess - Number_Generated) <= 5 and (Guess - Number_Generated) > 0:
            print("High, So Close!!!!")
        elif (Guess - Number_Generated) >= -5 and (Guess - Number_Generated) < 0:
            print("Low, So Close!!!!")
        Chances -= 1
    
    if Chances == 0:
        print("\nYou've run out of guesses, you lose.")
        print(f"\nThe Answer was {Number_Generated}")
    else:
        print(f"You got it! The answer was {Number_Generated}")

def hard_game(Chances):
    Guess = 0
    while Guess != Number_Generated and Chances > 1:
        print(f"You have {Chances-1} attempts remaining to guess the number.")
        Guess = int(input("Make a guess: "))
        if (Guess - Number_Generated) > 10:
            print ("High!!")
        elif (Guess - Number_Generated) < -10:
            print ("Low!!")
        elif (Guess - Number_Generated) <= 10 and (Guess - Number_Generated) > 0:
            print("High, Close!!!!")
        elif (Guess - Number_Generated) >= -10 and (Guess - Number_Generated) < 0:
            print("Low, Close!!!!")
        Chances -= 1

    if Chances == 0:
        print("\nYou've run out of guesses, you lose.")
        print(f"The Answer was {Number_Generated}")
    else:
        print(f"\nYou got it! The answer was {Number_Generated}")

if difficulty == "easy":
    easy_game(Chances=Chance)
else:
    hard_game(Chances=Chance)

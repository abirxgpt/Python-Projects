import game_data
import random
import logo
import clear

print(logo.logo)

game_on = True

Final_Score = 0
y = random.randint(0, (len(game_data.data)-1))
person_A = game_data.data[y]
z = random.randint(0, (len(game_data.data)-1))
person_B = game_data.data[z]

print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']} ")
print(logo.vs)
print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']} ")
answer = input("Who has more followers? Type 'A' or 'B': ")
if answer == "A":
    if person_A['follower_count'] > person_B['follower_count']:
        game_on = True
        Final_Score += 1
        person_A = person_B
        clear()
        print(logo.logo)
        print(f"You're right! Current score: {Final_Score}")
    else:
        game_on = False
elif answer == "B":
    if person_A['follower_count'] < person_B['follower_count']:
        game_on = True
        Final_Score += 1
        person_A = person_B
        clear()
        print(logo.logo)
        print(f"You're right! Current score: {Final_Score}")
    else:
        game_on = False

while game_on == True:
               
    z = random.randint(0, (len(game_data.data)-1))
    person_B = game_data.data[z]
    if person_A['follower_count'] == person_B['follower_count']:
        z = random.randint(0, (len(game_data.data)-1))
        person_B = game_data.data[z]
    else:
        print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']} ")
        print(logo.vs)
        print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']} ")
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == "A":
            if person_A['follower_count'] > person_B['follower_count']:
                game_on = True
                Final_Score += 1
                person_A = person_B
                clear()
                print(logo.logo)
                print(f"You're right! Current score: {Final_Score}")
            else:
                game_on = False
        elif answer == "B":
            if person_A['follower_count'] < person_B['follower_count']:
                game_on = True
                Final_Score += 1
                person_A = person_B
                clear()
                print(logo.logo)
                print(f"You're right! Current score: {Final_Score}")
            else:
                game_on = False
    
clear()
print(logo.logo)
print(f"Sorry, that's wrong. Final score: {Final_Score}")


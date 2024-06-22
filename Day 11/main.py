import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
User_1 = []
User_2 = []

for i in range(2):
    x = random.sample(cards,2)
    User_1.append(x[0])
    User_2.append(x[1])
    
def win_or_lose(Score1, Score2):
    if Score1 > Score2:
        print(f"\nYour Hands: {User_1}, Your Score {Score1}")
        print(f"Computer Hands: {User_2}, Computer Score {Score2}")
    
        print("You were the Closest. You Win 🤩")
    elif Score2 < Score1:
        print(f"\nYour Hands: {User_1}, Your Score {Score1}")
        print(f"Computer Hands: {User_2}, Computer Score {Score2}")
    
        print("Game Draw, Same Score. Nobody Wins 🙃")
    else:
        print(f"\nYour Hands: {User_1}, Your Score {Score1}")
        print(f"Computer Hands: {User_2}, Computer Score {Score2}")
    
        print("Computer was the Closest. You lose 😭")

def calculate_score():
    Score1 = 0
    Score2 = 0
    for i in range(len(User_1)):
        if User_1[i] == "J" or User_1[i] == "Q" or User_1[i] == "K":
            Score1 += 10
        else:
            Score1 += User_1[i]
    if Score1 > 21 and (11 in User_1):
        Score1 -= 10
    
    for i in range(len(User_2)):
        if User_2[i] == "J" or User_2[i] == "Q" or User_2[i] == "K":
            Score2 += 10
        else:
            Score2 += User_2[i]
    if Score2 > 21 and (11 in User_2):
        Score2 -= 10
        
    return [Score1, Score2]

Game_on = True
while Game_on:
    scores = calculate_score()
    Score_user1 = scores[0]
    Score_user2 = scores[1]
    print(f"\nThe Cards you're Dealt with are {User_1}, Your Total Score: {Score_user1}")
    print(f"Computer First Card: {User_2[0]}")
    condition = input("Type 'y' to get another card, type 'n' to pass: ")
    if Score_user2 < 17:
        x = random.choice(cards)
        User_2.append(x)
        scores = calculate_score()
        Score_user1 = scores[0]
        Score_user2 = scores[1]
    
    if condition == 'n':
        Game_on = False
        # Win or Lose from who's the Closest to the 21.
        win_or_lose(Score1=Score_user1, Score2=Score_user2)
        
    elif condition == 'y':
        x = random.choice(cards)
        User_1.append(x)
        scores = calculate_score()
        Score_user1 = scores[0]
        Score_user2 = scores[1]
        
    if Score_user1 > 21:
        print(f"\nYour Hands: {User_1}, Your Score {Score_user1}")
        print(f"Computer Hands: {User_2}, Computer Score {Score_user2}")
        
        print("You went over. You lose 😭")
        Game_on = False
    elif Score_user2 > 21:
        print(f"\nYour Hands: {User_1}, Your Score {Score_user1}")
        print(f"Computer Hands: {User_2}, Computer Score {Score_user2}")
        
        print("Computer went over. You Win 🤩")
        Game_on = False

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


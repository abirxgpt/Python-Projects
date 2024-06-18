import random
import hangman_pattern
import hangman_word

print('''
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba,   
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a        `Y8  88P'   `"8a  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88 
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88 
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88 
                                    aa,    ,88                                
                                     "Y8bbdP"                                 

'''
)
print("Welcome to the Hangman Word Guess Game!\nChoose your Type of Dictionary! \n1. Normal\n2. Science \n3. Disney \n4. Music")
Theme = input().lower()

if Theme == "science":
    chosen_word = random.choice(hangman_word.Science_Words)
elif Theme == "music":
    chosen_word = random.choice(hangman_word.Music_Words)
elif Theme == "disney":
    chosen_word = random.choice(hangman_word.Disney_Words)
else:
    chosen_word = random.choice(hangman_word.General_Words)

lives = 6
prev_guess = ""
display = []
for i in range(len(chosen_word)):
    display += "_"
count = len(chosen_word)
print(f"{display} \n")

while count > 0 and lives > 0:
    guess = input("Guess a Letter!: ")
    guess = guess.lower()
    prev_count = count
    if guess in prev_guess:
        print(f"You've already guessed {guess}")
        count += 1
    else:
        prev_guess += guess
    
    #if Player is Right
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            count -= 1
            
    # If Player is Wrong        
    if prev_count == count:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(hangman_pattern.stages[lives])
    else:
        print(hangman_pattern.stages[lives])
    print(display)
    print("-------------------------------------")

if count == 0:
    print("You Win !")
else:
    print("You Lose. \nMan Died")



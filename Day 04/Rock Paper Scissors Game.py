import random

print("Welcome to the Rock, Paper, Scissor Game")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_pose = random.randint(0,2)

pose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
pose = int(pose)
if pose == 0:
    print("You Choose Rock!!")
    print(rock)
elif pose == 1:
    print("You Choose Paper!!")
    print(paper)
else:
    print("You Choose Scissors!!")
    print(scissors)

if computer_pose == 0:
    print("Computer Chose Rock!!")
    print(rock)
elif computer_pose == 1:
    print("Computer Chose Paper!!")
    print(paper)
else:
    print("Computer Chose Scissors!!")
    print(scissors)

Result0 = ["Draw Game!!\nNobody Wins", "Computer Wins!!\nYou Lost", "You Wins!!\nCongratulations"]
Result1 = ["You Wins!!\nCongratulations", "Draw Game!!\nNobody Wins", "Computer Wins!!\nYou Lost"]
Result2 = ["Computer Wins!!\nYou Lost", "You Wins!!\nCongratulations", "Draw Game!!\nNobody Wins"]
Result = [Result0, Result1, Result2]
print(Result[pose][computer_pose])

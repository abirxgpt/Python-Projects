import random

fname = input("Enter your First Name: ")
sname = input("Enter your Last Name: ")
Date_of_Birth = input("Enter your Date of Birth in DD/MM/YY format: ")
Mobile_No = input("Enter your Contact Number: ")

Login_Pin = Mobile_No[-6] + Mobile_No[-5] + Mobile_No[-4] + Mobile_No[-3] + Mobile_No[-2] + Mobile_No[-1]

usr = Date_of_Birth.split("/",1)
Username = fname + sname[0] + usr[0]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passd = ""
password = ""
trgt = 8
Number_of_letters = 4
Number_of_numbers = 2
Number_of_Symbols = 2
for n in range(1, Number_of_letters + 1):
  x = random.choice(letters)
  passd += x + " "
for n in range(1, Number_of_numbers + 1):
  x = random.choice(numbers)
  passd += x + " "
for n in range(1, Number_of_Symbols + 1):
  x = random.choice(symbols)
  passd += x + " "
temp = passd.split()
random.shuffle(temp)
for n in range(0, trgt):
  password += temp[n]

print(f"\n\nWelcome {fname} to the DashBoard!\nHere are your Credentials\nYour Login ID PIN: {Login_Pin}\nYour Login Username: {Username}\nYour Password: {password}")

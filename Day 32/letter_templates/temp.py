# Define the folder where the files will be saved
folder_path = '.'  # Replace with the actual path to your folder

# List of birthday messages
messages = [
    "Dear [NAME],\n\nHappy birthday!\n\nAll the best for the year!\n\nAbir",
    "Dear [NAME],\n\nIt's your birthday! Have a great day!\n\nAll my love,\n\nAbir",
    "Hey [NAME],\n\nHappy birthday! Have a wonderful time today and eat lots of cake!\n\nLots of love,\n\nAbir",
    "Dear [NAME],\n\nWishing you a fantastic birthday filled with joy and happiness!\n\nBest wishes,\n\nAbir",
    "Dear [NAME],\n\nHappy birthday! May your day be as amazing as you are.\n\nWarm regards,\n\nAbir",
    "Hey [NAME],\n\nIt's your special day! Celebrate, enjoy, and have a blast!\n\nCheers,\n\nAbir",
    "Dear [NAME],\n\nMany happy returns on your birthday! Hope it's a memorable one.\n\nSincerely,\n\nAbir",
    "Hey [NAME],\n\nHappy birthday! May your year ahead be filled with success and happiness.\n\nTake care,\n\nAbir",
    "Dear [NAME],\n\nWishing you a very happy birthday! Hope your day is full of fun and laughter.\n\nBest,\n\nAbir",
    "Hey [NAME],\n\nHappy birthday! Celebrate big and enjoy every moment.\n\nMuch love,\n\nAbir"
]

# Save each message to a text file
for i, message in enumerate(messages[1:], start=4):  # Start from the 4th message
    file_name = f'letter_{i}.txt'
    file_path = f'{folder_path}/{file_name}'
    with open(file_path, 'w') as file:
        file.write(message)

print("Birthday messages have been saved successfully.")

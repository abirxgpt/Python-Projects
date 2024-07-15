with open("./Input/Names/invited_names.txt") as names:
    Invitee_names = names.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    Letter = letter.read()

for names in Invitee_names:
    name = names.strip("\n")
    completed_letter = Letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as edit:
        edit.write(completed_letter)

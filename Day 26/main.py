import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}

actual_word = input("Enter a Word: ").upper()

phonetic_words = [nato_dictionary[letter] for letter in actual_word]

print(phonetic_words)

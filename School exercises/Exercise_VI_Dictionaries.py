svk_to_eng = {"Pero": "Pen", "Auto": "Car", "Ryba": "Fish", "Pes": "Dog"}

print("Welcome to the Slovak to English translator")
print("What kind of word would you like me to translate?")
word_to_translate = input("> ")

if word_to_translate in svk_to_eng:
    print(f"The translation of the word {word_to_translate} is {svk_to_eng.get(word_to_translate)}.")
else:
    print("There is no such word in a dictionary.")

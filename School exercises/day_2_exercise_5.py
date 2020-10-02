dictionary = {'cat': 'macka', 'dog': 'pes', 'hamster': 'skrecok', 'your_mom': 'tvoja mama'}

print("Welcome to the English to Slovak translator.")
print("---------------------------------------------")
print("English\t - \tSlovak")
print("---------------------------------------------")

for key,value in dictionary.items():
    print(str(key) + "\t is \t" + str(value))

word = input(str('Which word to translate?'))

for key,value in dictionary.items():
    if word in dictionary:
        translation = dictionary[word] 
        print('The translation for', word, 'is', translation)
        exit()
    if word not in dictionary:
        print("Sorry I cannot translate the word.")
        exit()


#how to invert the dictionary --> inverted = {v: k for k,v in dictionary.items()}       

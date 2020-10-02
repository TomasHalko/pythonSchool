fruit = {"Apple": 1, "Banana": 0.5, "Grapefruit": 2, "Watermelon": 10}

class CC():
    def __init__(self, name, ccnum, ccv):
        self.name = name
        self.ccnum = ccnum
        self.ccv = ccv

card1 = CC("Tomas", 4405778244562345, 765)
card2 = CC("Samo", 4405778990897213, 341)

print("What kind of fruit do you want to buy?")
user_fruit = input("> ")
if (user_fruit in fruit):
    print("Enter your name:")
    user_name = input("> ")
    if (user_name == "Tomas"):
        print("Enter your credit card number: ")
        user_ccnum = input("> ")
        if (user_ccnum == 4405778244562345):
            print("Enter the ccv of the card: ")
            user_ccv = input("> ")
            if (user_ccv == 765):
                print("The payment has been processed.")
                print(f"You just bought one {user_fruit}.")
            else:print("Wrong ccv!")
        else:print("Wrong credit card number!")     
    elif(user_name == "Samo"):
        print("Enter your credit card number: ")
        user_ccnum = input("> ")
        if (user_ccnum == 4405778990897213):
            print("Enter the ccv of the card: ")
            user_ccv = input("> ")
            if (user_ccv == 341):
                print("The payment has been processed.")
                print(f"You just bought one {user_fruit}.")
            else:print("Wrong ccv!")
        else:print("Wrong credit card number!")
    else: print("There is no card with such name assigned!")
else:print(f"There is no {user_fruit} in our shop momentarily.")


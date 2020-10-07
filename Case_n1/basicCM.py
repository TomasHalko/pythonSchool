def chooseYourDrink(x):
    products = {"c1" : 20, "c2" : 22, "c3" : 22, "t1" : 18, "t2" : 20,"t3" : 22, "h1" : 24, "h2" : 26,"h3" : 28}
    return(products[x])

def chooseYourSize(size):
    sizePool = {"S" : 0, "M" : 5, "L" : 10}
    return cost + sizePool[size]

def choosePaymentMethod():
    print("CARD | CASH")
    cardOrCash = input("> ")
    if cardOrCash == "CASH":
        print(f"Insert {cost} kr")
        global funds 
        funds = int(input("> "))
        checkBudget()
    else: 
        print(f"Pay {cost} kr by card")
        print("Here is your drink")

def checkBudget():
    if funds >= cost:
        print("Here is your drink")
        print(f"Returning {funds - cost} kr")
    else: 
        print(f"Insert {cost - funds} more kr")
        addition = int(input("> "))
        while addition < cost - funds:
            print(f"Insert {cost - funds - addition} more kr")
            addition = addition + int(input("> "))
        else:
            print("Here is your drink")
            print(f"Returning {funds + addition - cost} kr")
              
      
drink = input("Choose your drink: ")
cost = chooseYourDrink(drink)

cupSize = input("Choose your cup size: ")
cost = chooseYourSize(cupSize)

print("Please place the cup inside.")
choosePaymentMethod()



print("------")
input("End")



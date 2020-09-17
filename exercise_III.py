items = ['item_n1', 'item_n2', 'item_n3', 'item_n4', 'item_n5']

userInput = input("Input an item: ")    
for item in items:
    print(item)
if userInput in items:
    print("This item is already in the list")
else: print("The item has been added"), items.append(userInput), print(items)
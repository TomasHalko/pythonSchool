#A
import math  

def square_this (num):
    squared = math.sqrt(num)
    return int(squared)

print(square_this(25))

#B
def name_reader (name):
    name_chosen = name
    print(f"You have chosen the name: {name_chosen}")
    return name_chosen

print("Input the name:")
name_reader(input("> "))

#C

def neg_or_pos (number):
    if int(number) < 0:
        print(f"The number you have chosen ({number}) is a negative number")
    else: 
        print(f"The number you have chosen ({number}) is a positive number")

print("Choose a number: ")
neg_or_pos(input("> "))
def function_name():
    print("Something!")

function_name()

def add_two(number): 
    print(number + 2)

add_two(2)

def method1():
    a = 1 
    b = 2
    c = a + b
    return c

print(method1())    

def succ(number):
    return number + 1

print("Successor to 1 os " + str(succ(1)))


def sum(a,b):
    return a + b

print("The sum of 2 and 2 = " + str(sum(2,2)))

def dayIs(aDay):
    if aDay == "Saturday" or aDay == "Sunday":
        dayType = "weekend"
    else:
        dayType = "weekday"
    return dayType

day1 = "Monday"
day2 = "Sobota"

print(day1 + " is a " + dayIs(day1))
print(day2 + " is a " + dayIs(day2))

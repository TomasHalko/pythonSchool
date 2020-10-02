name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 # inches
height = round(height_in_inches * 2.54)
weight_in_pounds = 180 # lbs
weight = round(weight_in_pounds / 2.2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
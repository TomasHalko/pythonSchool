from sys import argv

script, user_name, user_age = argv
prompt = '> '

print(f'''Hi {user_name}, you are apparently {user_age} years old.
I'm the {script} script.''')
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""") #We make a variable, prompt, that is set to the prompt we
#want, and we give that to input instead of typing it over and over.
#Now if we want to make the prompt something else, we just change it
#in this one spot and rerun the script. Very handy
input()
class Warrior ():

    def __init__(self, name, age, strength, dexterity, inteligence):
        self.name = name
        self.age = age
        self.strength = strength
        self.dexterity = dexterity
        self.inteligence = inteligence

    def about(self):
        print(f"My name is {self.name} and my age is {self.age}.")
        print(f'''My stats are:
        Strength => {self.strength}
        Dexterity => {self.dexterity}
        Inteligence => {self.inteligence}''')

player1 = Warrior("Tomas", 19, 9001, 69, 420)

player1.about()
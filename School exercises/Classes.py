class Warrior ():

    def __init__(self, name, age, strength, dexterity, inteligence, ability):
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

class Human (Warrior):
    def __init__(self, name, age, strength, dexterity, inteligence, ability):
        self.ability = ability

    def getHuman (self):
        return (f'{self.name} Ability: {self.ability}')

player1 = Warrior("Tomas", 19, 9001, 69, 420, "Gigantic strength")
player2 = Human ("Samo", 19, 5, 4, 3, "Whining")

player1.about()
print(player2.getHuman())
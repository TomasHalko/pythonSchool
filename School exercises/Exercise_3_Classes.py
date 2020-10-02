class Name_person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def inform_print(self):
        print(f"The name is : {self.name} and the age is: {self.age}")

tomas = Name_person("Tomas", 19)

tomas.inform_print()
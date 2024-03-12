# inheritance means other class can 
# use whatever variables/properties that has been declare 
# at the main or other declared class

# exp: User can be many character: Wizards, Archers
# Wizards and Archers class can use User as base class
# to use as authentication for example in real-life application

# main/master class
class User:
    def signIn(self):
        print("Logged In")
        
# sub-class/derived
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"Attack with power level of {self.power}")
            
# sub-class/derived
class Archer(User):
    def __init__(self, name, numArrows):
        self.name = name
        self.numArrows = numArrows
    def attack(self):
        print(f"Attack with arrow of {self.numArrows}")

# -----------------------------------------------------------
# isinstance(instance, Class) //validate if the object is instance of the class
wizard1 = Wizard("Merlin", 50)
print(wizard1.signIn())
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, object))
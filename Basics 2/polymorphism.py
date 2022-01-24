# polymorphism

# exp: User can be many character: Wizards, Archers
# Wizards and Archers class can use User as base class
# to use as authentication for example in real-life application

# main/master class
class User:
    def signIn(self):
        print("Logged In")

    def attack(self):
        print("Rest")

# sub-class/derived
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)  # default callback
        print(f"{self.name} attack with power level of {self.power}")
            
# sub-class/derived
class Archer(User):
    def __init__(self, name, numArrows):
        self.name = name
        self.numArrows = numArrows
    def attack(self):
        User.attack(self) #default callback
        print(f"{self.name} attack with arrow of {self.numArrows}")

# --------------------------------------------------------
wizard1 = Wizard("Viper", 50)
archer1 = Archer("Blood", 80)

# POLYMORPHISM-----------------------------------------------------------------
# declare the object's class function just to callback
def player_attack(char):
    char.attack()
# SINGLE object call
player_attack(wizard1)
player_attack(archer1)
# or ARRAYS call
for char in [wizard1, archer1]:
    char.attack()
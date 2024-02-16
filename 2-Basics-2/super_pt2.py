# super

# exp: User can be many character: Wizards, Archers
# Wizards and Archers class can use User as base class
# to use as authentication for example in real-life applicationa

class User:
    def __init__(self, email):
        self.email = email
        
    def signIn(self):
        print("Logged In")

    def attack(self):
        print("Rest")

# sub-class/derived
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) #Calling attributes from super/parent class
        self.name = name
        self.power = power
        
    def attack(self):
        print(f"{self.name} attack with power level of {self.power}")
        
        
wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
print(wizard1.email)
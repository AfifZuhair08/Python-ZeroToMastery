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
        super().__init__(email)
        self.name = name
        self.power = power
        
    def attack(self):
        print(f"{self.name} attack with power level of {self.power}")
        
# introspection
wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
print(dir(wizard1))
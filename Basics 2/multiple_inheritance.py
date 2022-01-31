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
    def attack2(self):
        print(f"Attack with arrow of {self.numArrows}")

    def run(self):
        print("ran so fast")

# multi-inheritance class
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, numArrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, numArrows)

hb1 = HybridBorg("borgy", 50, 100)
print(hb1.attack())
print(hb1.attack2())
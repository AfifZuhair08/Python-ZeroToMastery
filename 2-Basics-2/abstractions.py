class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print("run")
        
    def speak(self):
        print(f"My name is {self.name} and my age is {self.age}")
       
player1 = PlayerCharacter("Afif", 25)
print(player1.speak())
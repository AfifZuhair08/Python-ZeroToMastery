# underscore ("_") means its private data
# cannot do modifications to the variables

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def run(self):
        print("run")
        
    def speak(self):
        print(f"My name is {self._name} and my age is {self._age}")
       
player1 = PlayerCharacter("Afif", 25)
print(player1.speak())


# ----------------------------------------------
# CANNOT do items modification of private data
player1.name = "Ahamd"
player1.speak = "blabka"
print(player1.speak()) #error here

class PlayerCharacter:
    
    # class objeet attributes - static value
    membership = True
    
    # constructor - also can define default value for properties
    def  __init__(self, name, age):
        # attributes - dynamic value
        self.name = name
        self.age = age
        
    def run(self):
        print("run")
        
    def shout(self):
        print(f"My name is {self.name} and I'm {self.age}")
        
    def isOver18(self):
        if(self.age > 20):
            print(self.age)

# object initialization  
player1 = PlayerCharacter("Ahmad", 12)
player2 = PlayerCharacter("Wani", 22)

# define attributes by external
player1.attack = 12

# fetching and display area #
print(player1.shout(), player1.isOver18())
print(player2.shout(), player2.isOver18())

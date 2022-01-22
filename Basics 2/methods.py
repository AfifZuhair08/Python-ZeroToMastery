class PlayerCharacters:
    
    # class objeet attributes - static value
    membership = True
    
    # constructor - also can define default value for properties
    def __init__(self, name, age ):
        # atttributes
        self.name = name
        self.age = age
        
    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    # really care about class attributes when to modify/change them
    def adding_objects(cls, num1, num2):
        return cls("Tom", num1 + num2)
    
    @staticmethod
    # doesn't really care about class attributes to modify/change them
    def adding_objects(num1, num2):
        return num1 + num2
    
    # conclusion,
    # the difference bwtween class & static method is that,
    # class method can access the "cls" as instantiation of its own class and modifying its attributes

# object initialization  
player1 = PlayerCharacters("Tom", 20)

# fetching and display area #
player1 = PlayerCharacters.adding_objects(3,5)
print(player1)
# List class that contains characters
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Character class
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

# character's user
class Simon(Cat):
    def sing(self, sounds):
        return f'~{sounds}~'

# character's user
class Sally(Cat):
    def sing(self, sounds):
        return f'~{sounds}~'

# character's user
#1 Add another Cat
class Orange(Cat):
    def sing(self, sounds):
        return f'~{sounds}~'
            
#2 Create a list of all of the pets (create 3 cat instances from the above)
simon1 = Simon("Simon1", 2)
sally1 = Sally("Sally1", 4)
orange1 = Orange("Orange1", 3)
my_cats = [simon1, sally1, orange1]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats) #using the parameters as arguments for Pets(animals)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()
# or
cat1 = Sally("Oyen", 20)
print(cat1.walk(), cat1.sing("Meow"))
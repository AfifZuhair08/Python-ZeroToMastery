class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# can be reuse multiple times
player1 = PlayerCharacter("Afif", 27)
print(player1.name)
print(player1.age)

# cannot be reuse multiple times / declare once only
player2 = {'name': "Sarah", 'age':24}
print(player2['name'])
print(player2['age'])

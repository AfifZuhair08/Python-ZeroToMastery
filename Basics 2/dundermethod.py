class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Alex",
            "has_pets": False
        }
        
    def __str__(self):
        return f'{self.color}'
        
    def __len__(self):
        return 5
    
    def __del__(self):
        print("deleted")
    
    def __call__(self):
        print("calling")
    
    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)

print(action_figure.__str__())
print(str(action_figure))

# define length
print(len(action_figure))

# del action_figure
print(action_figure())

# calling dict reference
print(action_figure["name"])
class Toy():
    def __init__(self, color, age, size):
        self.color = color
        self.age = age
        self.size = size
        self.my_dict = {
            "name": "Alex",
            "has_pets": False
        }
        
    def __str__(self):
        return f'Color is {self.color}, for age {self.age} and size of {self.size}'
        
    def __len__(self):
        return 5
    
    def __del__(self):
        print("deleted")
    
    def __call__(self):
        print("calling")
    
    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 4, "medium")

# print(action_figure.__str__())
# print(str(action_figure))

# define length
# print(len(action_figure))

# del action_figure
print(action_figure()) #--> will trigger __call__ method that created/exist
print(action_figure) # --> will trigger __str__ method that created/exist

# calling dict reference
# print(action_figure["name"])

# get items from self items properties
print(action_figure['name'])
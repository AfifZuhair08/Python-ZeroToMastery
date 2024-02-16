# function act as variables, callable using variable like name

def hello(func):
    func()
    
def greet():
    print("still here!")
    
a = hello(greet)    

print(a)
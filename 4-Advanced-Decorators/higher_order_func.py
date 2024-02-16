# Higher Order Function
# 1- accept a function as a parameter
# 2- function that return another function

def greet(func):
    func()
    
def greet2():
    
    def func():
        return 5
    
    return func
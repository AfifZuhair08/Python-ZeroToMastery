# TYPE 1 PASSING DIRECT WITH ONE PARAMETER/ARGUMENT
def my_decorator(func):
    def wrap_func(x):
        print("*********")
        func(x)
        print("*********")
        
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)
    
hello("hello")


# TYPE 2 PASSING DIRECT WITH MANY ONE PARAMETER/ARGUMENT 
# without need to update decorators param 
# *args = all arguments / **kwargs = all keywords arguments
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*********")
        func(*args, **kwargs)
        print("*********")
        
    return wrap_func

@my_decorator
def hello(greeting, emoji=":)"):
    print(greeting, emoji)
    
hello("hello")
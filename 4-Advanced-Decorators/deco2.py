# my_decorator takes a func that declares it as "@my_decorator",
# then use it under it wrap_func() function by passing as parameter (function as variables method)

def my_decorator(func):
    def wrap_func():
        print("*********")
        func()
        print("*********")
        
    return wrap_func

# TYPE 1 -------------------------------------
# call decorators "@my_decorator" by declare it above that function
@my_decorator
def hello():
    print("helloooo!")
    
hello()

# TYPE 2 -------------------------------------
# directly call the decorator and pass the function
def hello_again():
    print("helloooo!")
    
call_hello = my_decorator(hello_again)

call_hello()
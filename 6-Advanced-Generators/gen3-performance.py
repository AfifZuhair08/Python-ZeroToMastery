# generators works for processing big load of data

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, *kwargs)
        t2 = time()
        
        print(f'It tooks {t2-t1} seconds')
        
        return result
    return wrapper

@performance
def loop_range():
    print("1")
    for i in range(100000000):
        i*5
        
@performance
def loop_range2():
    print("2")
    for i in list(range(100000000)):
        i*5
        
loop_range() #--> faster
loop_range2() #--> slower
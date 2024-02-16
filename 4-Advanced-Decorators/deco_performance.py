# how decorators can be used in performance applications example
# for this example is to use time tracking in the wrapper

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
    for i in range(999999):
        i*5
        
loop_range()
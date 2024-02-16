# DEMONSTRATE GENERATORS PERFORMANCE

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, *kwargs)
        t2 = time()
        
        print(f'It tooks {t2-t1} seconds')
        
        return result
    return wrapper

# @performance
# def fib(num):
#     a = 0
#     b = 1
    
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
        
# for x in fib(500):
    # print(x) #1 not keeping in memory
    

# METHOD 2
@performance
def fib2(num):
    a = 0
    b = 1
    result = [] #2 keeping in memory

    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
        
    print(result)
    return result

fib2(10000) 
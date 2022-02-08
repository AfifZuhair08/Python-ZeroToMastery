# reduce function
# format is -> reduce(<accumulator>, <dataset>, <initial value>)
# import reduce from functools library

from functools import reduce

my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(my_list)
print(reduce(accumulator, my_list, 0))
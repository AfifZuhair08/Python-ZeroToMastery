# lambda expressions - anonymous functions, only used once/one place

# format> lambda param: action(param)

from functools import reduce


my_list = [1,2,3]

# ORIGINAL
# def multiply_by2(item):
#     return item*2
# print(list(map(multiply_by2, my_list)))

# USING LAMBDA for list
print(list(map(lambda item: item*2, my_list)))

# USING LAMBDA for reduce
print(reduce(lambda acc, item: acc+item, my_list))



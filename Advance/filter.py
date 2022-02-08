# filter function
# format is -> map(action, data)
my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0 

print(my_list)
print(list(filter(check_odd, [1,2,3])))
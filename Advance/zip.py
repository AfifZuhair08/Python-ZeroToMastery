# zip function
# format is -> zip(data1, data2,....n of data)
# Create a list of tuples, in pair of each data set

my_list = [1,2,3]
my_secondList = [10,20,30]

def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

print(my_list)
print(my_secondList)
print(list(zip(my_list, my_secondList)))
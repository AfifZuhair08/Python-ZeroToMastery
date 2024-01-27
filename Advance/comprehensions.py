# list, set, dictionary

my_list = []

# normal
# for char in 'hello':
#     my_list.append(char)
# print(my_list)

# [<param> for <param> in iterable]
# ["use" for "ref" in iterable] 
# first is the value being used, second is the reference to the list

# in char 
a_list = [char for char in 'hello']
print(a_list)

# in range
b_list = [num for num in range(1,100)]
print(b_list)

# in range
c_list = [num*2 for num in range(1,100)]
print(c_list)
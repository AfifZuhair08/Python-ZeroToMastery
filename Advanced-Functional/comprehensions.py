# list, set, dictionary

my_list = []

# normal
# for char in 'hello':
#     my_list.append(char)
# print(my_list)

# [<param> for <param> in iterable]
# ["use" for "ref" in iterable] 
# first is the value being used, second is the reference to the list

# LIST  ------------------------------------------------------
# in char 
a_list = [char for char in 'hello']
print(a_list)

# in range
b_list = [num for num in range(0,100)]
print(b_list)

# in range, times 2
c_list = [num*2 for num in range(0,100)]
print(c_list)

# in range, only even number 
d_list = [num**2 for num in range(0,100) if num % 2 == 0]
print(d_list)

# SET  ------------------------------------------------------
# in char 
a_list = {char for char in 'hello'}
print(a_list)

# in range
b_list = {num for num in range(0,100)}
print(b_list)

# in range, times 2
c_list = {num*2 for num in range(0,100)}
print(c_list)

# in range, only even number 
d_list = {num**2 for num in range(0,100) if num % 2 == 0}
print(d_list)

# DICT  ------------------------------------------------------
# in char 

simple_dict = {
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key, value in simple_dict.items()} #all
my_dict2 = {key:value**2 for key, value in simple_dict.items() if value%2==0} #only even number
print(my_dict)
print(my_dict2)
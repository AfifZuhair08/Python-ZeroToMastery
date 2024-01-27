# SQUARE
my_list = [5,4,3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list)


# LIST SORTING
a = [(0,2),(4,3),(10,-1),(9,9)]

#using second item of the tuple first -> x[0], second -> x[1]
a.sort(key=lambda x: x[1]) 

print(a)
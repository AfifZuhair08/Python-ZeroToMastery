some_list = ['a','b','c','d','e','d','a']

duplicates = []

# normal
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
            
# comprehension
duplicate_comp = list(set([x for x in some_list if some_list.count(x)>1]))
print(duplicate_comp)

            
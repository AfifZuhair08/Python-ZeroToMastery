new_list = ["a","b","c","c","b","a","b"]

duplicate = []

for value in new_list:
    if new_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
        
print(duplicate)
# note that SuperList class taking "list" as superclass,
# so that we can use the power of list as defined type in python

class SuperList(list):
    def __len__(self):
        return 1000

# instantiate
super_list1 = SuperList()

# call by function
print(len(super_list1))

# append list
super_list1.append(5)
print(super_list1[0])

# cross check of classes
print(issubclass(SuperList, list))
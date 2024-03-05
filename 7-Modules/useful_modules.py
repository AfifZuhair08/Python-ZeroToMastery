from collections import Counter, defaultdict, OrderedDict

# count items in list
list = [1,2,3,3,4,5,5,6]
print(Counter(list))

# set default dict items in case it accessed but doesnt exist
dictionary = defaultdict(lambda: 5,{ 'a':1, 'b':2 })
print(dictionary['c'])

# check ordered in dict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d2 == d)
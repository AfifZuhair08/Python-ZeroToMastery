x = int(5)
print(x)

x = float(2.8)
print(type(x))

x = "Hello"[0]
print(x)

x = " Hello ".strip()
print(x)

x = "Hello".upper()
print(x)

print("Hello".replace("H","B"))

# wrong var
# my-var = 5

# Python List
list = ["1","2","3"]

# DICTIONARY is a collection which is ordered*, changeable and do not allow duplicates.
# cannot have same key, as key is unique, therefore it could be take the latest
# {key : value} pair
my_dict = {"name" : "ali", "name" : "abu" }
print(my_dict) #<-- will return one dict only (latest)
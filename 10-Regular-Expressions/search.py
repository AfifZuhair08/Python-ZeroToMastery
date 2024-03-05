import re

pattern = re.compile("this")

# Example - search text in sentences
string = "this is sample text to search inside ths file"
# print("text" in string)

# match object
match = re.search("this", string)
print(match.span()) # location/index
print(match.group()) # return if match

# group if found and return one
a = pattern.search(string)
print("A: " ,a.group()) # return if match

# find and return all found string
b = pattern.findall(string)
print("B: " ,b)

# find the full string on target string
c = pattern.fullmatch(string)
print("C: " ,c)

d = pattern.match(string)
print("D: " ,d)
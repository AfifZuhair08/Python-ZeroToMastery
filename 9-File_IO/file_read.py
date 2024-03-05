my_file = open('my_file.txt')

# can only read a file once
print(my_file.read())
my_file.seek(0)
print(my_file.read())
print(my_file.read())

# read first line
print(my_file.readline())

# read multiple files
print(my_file.readlines())

# close the reading of files
my_file.close()
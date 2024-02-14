# make a list of number range
def make_list(num):
    numList = []
    for i in range(num):
        numList.append(i+1)
    return numList

read_list = make_list(100) #<-- call this function will affect the performance and memory if the number is bigger
print(read_list)
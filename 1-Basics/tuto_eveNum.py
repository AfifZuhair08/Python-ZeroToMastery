def highestEven(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highestEven([1,2,3,4,5]))
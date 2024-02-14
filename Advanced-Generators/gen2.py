# iterables
# iterate
# generators

def generator_function(num):
    for i in range(num):
        yield i

# this method does not store in any memory such as when we use append
for item in generator_function(100):
    print(item)
    
# this method will pause (yield) and trigger next steps when next() is use
g = generator_function(100)
next(g)
print(next(g))

# if next() is use but the range is exceeded, exception will happen to StopIteration
# prevent over/forced loop
p = generator_function(1)
next(p)
next(p)
next(p)
print(next(p))
# commonly used to display the comments out of a funtion

def testString(a):
    '''
    This is a long string
    wether it is few line in between the open and close tag
    '''
    print(a)
    
testString("Anything")

# type 1
# help(testString)
# type 2
print(testString.__doc__)
# to assign functions into an variables as part of larger expressions

def printlength(text):
    if((a := len(text)) > 10):
        print(a)
    if((b := len(text)) < 10):
        print(b)
        
printlength("deqwrgfg")
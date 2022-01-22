# // PARAMETERS //

# passing parameters
def sayHello(text, emoji):
    print(f"Helloo {text}! {emoji}")
    
# default parameters
def sayHello2(text="Person", emoji="😉"):
    print(f"Helloo {text}! {emoji}")

    
# // ARGUMENTS //
# positinal arguments
sayHello("Afif","😊")

# keyword arguments
sayHello(emoji="😁", text="Sarah")

# default arguments
sayHello2()
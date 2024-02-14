try:
    age = int(input("What is your age?"))
    print(age)
except:
    print("Wrong input bro!")


# OR

while True:
    try:
        age = int(input("What is your age?"))
        print(age)
        10/age
    except ValueError: #non number would be error
        print("Enter a number only !")
    except ZeroDivisionError: #if number is zero
        print("Cannot divide by zero")
    else:
        print("Bye2")
        break
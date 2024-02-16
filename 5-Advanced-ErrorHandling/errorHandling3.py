while True:
    try:
        age = int(input("What is your age?"))
        print(age)
        10/age
    except ValueError: #non number would be error
        print("Enter a number only !")
        continue
    except ZeroDivisionError: #if number is zero
        print("Cannot divide by zero")
        break
    else:
        print("Bye2")
        break
    finally: #run at the end regardless what case happen
        print("Finally done..")
    print("Can you hear me?") #will be called in situation no error trigger and no break
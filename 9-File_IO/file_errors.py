try:
    with open("my_filde.txt", mode="c") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("File does not found!")
    raise err
except IOError as err:
    print("IO ERROR Issue happen..")
    raise err
except ValueError as err:
    print("Invalid operation")
    raise err
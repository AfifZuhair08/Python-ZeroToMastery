# r = read, 
# r+ = read, write
# a = append
# w = write (replace)

with open("my_file.txt", mode="a") as my_file:
    
    text = my_file.write("=)")
    
    print(text)
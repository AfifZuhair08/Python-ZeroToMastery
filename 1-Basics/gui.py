picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

pixel_fill = "*"
pixel_empty = " "
for image in picture:
    for pixel in image:
        if pixel == 0:
            print(pixel_empty, end="") # end means preventing from creating new line
        if pixel == 1:
            print(pixel_fill, end="") # end means preventing from creating new line
    print("")


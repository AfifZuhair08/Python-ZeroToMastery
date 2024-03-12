from PIL import Image, ImageFilter

img = Image.open("charmander.jpg")

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("charmander_blur.png",'png')

filtered_img = img.convert('L')
filtered_img.save("charmander_grey.png",'png')
filtered_img.show("charmander_grey.png")
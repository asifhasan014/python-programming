from PIL import Image

img = Image.open('D:\cat-picture\img1.jpg')
img.save('images/img1.jpg')
img.save('images/img1.png')
img.save('images/img1.pdf')
img.show()

#thumbnail image
MAX_SIZE = (150,150)
img5 = Image.open('D:\cat-picture\img5.jpg')
img5.thumbnail(MAX_SIZE)
img5.save('images/catprofile.jpg')


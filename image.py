from PIL import Image, ImageEnhance, ImageFilter
import os

# img = Image.open('D:\cat-picture\img1.jpg')
# img.save('images/img1.jpg')
# img.save('images/img1.png')
# img.save('images/img1.pdf')
# img.show()

#thumbnail image
# MAX_SIZE = (150,150)
# img5 = Image.open('D:\cat-picture\img5.jpg')
# img5.thumbnail(MAX_SIZE)
# img5.save('images/catprofile.jpg')
# print(os.listdir('D:\cat-picture'))
folder = 'D:\cat-picture'
saveFolder = 'images'

for item in os.listdir(folder):
    print(folder+"\\"+item)
    img  = Image.open(folder+"\\"+item)
    filename,extension = os.path.splitext(item)
    print(f"filename {filename} , extension {extension}")
    img.save(saveFolder+"\\"+filename+'.png')




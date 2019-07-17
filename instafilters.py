from PIL import Image
#original image
base_img = Image.open("newpic.jpg")
#filter to be added
img_filter = Image.open("filter.jpg")
size=(760,760)
base_img=base_img.resize(size)
img_filter=img_filter.resize(size)
r,g,b=base_img.split()
R,G,B=img_filter.split()
im=Image.merge("RGB",(r,G,b))
im.show()
im.save('rand.jpg')
from PIL import Image

img = Image.open('D:\img\IMG_0001.JPG')

print(img.format, img.size, img.mode)
# JPEG (512, 512) RGB

#img_mono = img.convert('L')
#img_mono.show()
#img_mono.save('lena_mono.jpg')

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


def rndchar():
    return chr(random.randint(65, 90))

# 随机颜色
def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

im = Image.open("/home/asterwyx/Downloads/2.jpg")
w, h = im.size
print("Original image size: %sx%s" % (w, h))
im.thumbnail((w//2, h//2))
print("Resize image to: %sx%s" % (w//2, h//2))
im.save("thumbnail.jpg", 'jpeg')
im2 = im.filter(ImageFilter.BLUR)
im2.save("blur.jpg", "jpeg")
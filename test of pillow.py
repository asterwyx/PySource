from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


def rndchar():
    return chr(random.randint(65, 90))


# 随机颜色1
def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 规定图片大小
width = 60 * 4
height = 60

# 创建白底的新图片
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.load_default()
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每一个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndcolor())

# 输出文字
for t in range(4):
    draw.text((60*t + 10, 10), rndcolor(), font=font, fill=rndcolor2())
image = image.filter(ImageFilter.BLUR)
image.save("code.jpg", 'jpeg')

im = Image.open("/home/asterwyx/Downloads/2.jpg")
w, h = im.size
print("Original image size: %sx%s" % (w, h))
im.thumbnail((w//2, h//2))
print("Resize image to: %sx%s" % (w//2, h//2))
im.save("thumbnail.jpg", 'jpeg')
im2 = im.filter(ImageFilter.BLUR)
im2.save("blur.jpg", "jpeg")
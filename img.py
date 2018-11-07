from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from random import randint

# 创建一个画布
im = Image.new('RGB',(600,300),(255,255,255))
# 创建一个画笔
pen = ImageDraw.Draw(im)
# 画点
for i in range(1000):
	pen.point(([randint(0,600)][randint(0,300)],(randint(0,255),randint(0,255),randint(0,255))))



# 显示画布
im.show()









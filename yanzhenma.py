# from random import randint
# import random
# from PIL import Image,ImageFilter,ImageDraw,ImageFont
#
# img = Image.new("RGB",(150,150),(255,255,255))
# #第一个参数：采用RGB颜色模式
# #第二个参数：图片大小
# #第三个参数# 具体图片颜色
# #RGB:红，绿，蓝
#
# draw = ImageDraw.Draw(img)
# #绘制线条和点
# #绘制线
#
# for i in range(randint(1,10)):
#     draw.line(
#         #在绘制线条时有个特色，每条线有两个点，每个点靠XY来确定位置
#     [
#         (randint(1,150),randint(1,150)),
#         (randint(1,150),randint(1,150))
#     ],
#     fill = (0,0,0)
#     )
#
# for j in range(1000):
#     draw.point(
#                 [
#                     randint(1,150),randint(1,150)
#                 ],
#                 fill=(0,0,0)
#                 )
#
# font_list=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
# c_chars="".join(random.sample(font_list,5))
#
# font = ImageFont.truetype("simsun.ttc",25)
# draw.text((5,15),c_chars,font=font,fill="green")
# #第一个参数：文字位置  距离上和左的距离
# #第二个参数：文字内容
# #第三个参数：字体
# #第四个参数：字体颜色
#
# params = [1-float(randint(1,2))/100,
#           0,
#           0,
#           0,
#           1-float(randint(1,2))/100,
#           float(randint(1,2))/500,
#           0.001,
#           float(randint(1,1))/100,
#           ]
# img = img.transform((150,150),Image.PERSPECTIVE,params)
#
# #第一个参数：扭曲的范围
# #第二个参数：扭曲的样式
# #第三个参数：扭曲的参数
#
# img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
#
# img.show()







import pytesseract
from PIL import Image


def rgb(im):
    '''获取每一个像素的亮度     (r+g+b)/3
    '''
    width, heigth = im.size
    data = np.zeros((heigth, width))
    aa = []
    for w in range(width):
        for h in range(heigth):
            y, cb, cr = im.getpixel((w, h))
            data[h, w] = (y + cb + cr) / 3
            aa.append((y + cb + cr) / 3)
    data = pd.DataFrame(data)
    aa = pd.Series(aa)
    return aa, data

def topliangdu(liangdu, biaozhun=100):
    '''根据亮度排序，取大于标准的值
    '''
    c=liangdu.value_counts()
    return list(c[c>100].index)


def liangdutianbai(im,mubiao):
    '''将非目标区域填充白色'''
    width, heigth = im.size
    for w in range(width):
        for h in range(heigth):
            y,cb,cr=im.getpixel((w,h)) #提取点(10,10)位置的亮度、蓝色分量、红色分量的值。
            tmp = (y+cb+cr)/3
            if tmp not in mubiao:
                im.putpixel([w,h],(255, 255, 255))
    return im

def tongse(im):
    '''验证码验证文字的单个文字同色时，处理。'''
    global aa, data
    aa,data = rgb(im)
    mubiao = topliangdu(aa)
    im = liangdutianbai(im, mubiao)
    img_grey = im.convert('L')
    img_grey.show()
    return img_grey

im = Image.open('d://test.jpg')
pytesseract.pytesseract.tesseract_cmd = 'd://python/Tesseract-OCR//tesseract'
text = pytesseract.image_to_string(tongse(im))  # 将图片转成字符串
print (text)







#import pytesseract
#from PIL import Image
# def erzhihua(im, point=127):
#     '''图片二值化处理'''
#     img_grey = im.convert('L')
#     threshold = point
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     img_out = img_grey.point(table, '1')
#     img_out.show()
#     img_out.save('d://tmp.bmp')
#     return img_out
#
# im = Image.open('d://test.jpg')
# pytesseract.pytesseract.tesseract_cmd = 'd://python/Tesseract-OCR//tesseract'
# text = pytesseract.image_to_string(erzhihua(im))  # 将图片转成字符串
# print(text)





#import pytesseract
#from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = 'd://python/Tesseract-OCR//tesseract'
# im= Image.open("d://3.jpg")
# im.show()
# #image=Image.open("c:\\1yz.jpg")#打开验证码图片
# vcode=pytesseract.image_to_string(im)
# print(vcode)
from AipImageClassify import client

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/华为.jpg')

""" 调用logo商标识别 """
result = client.logoSearch(image)

logo = result['result'][0]
print(logo['name'])
print(logo['probability'])
from AipImageClassify import client


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/狮身人面像.jpg')

""" 调用地标识别 """
result = client.landmark(image)['result']

print(result)
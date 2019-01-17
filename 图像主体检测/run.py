from AipImageClassify import client

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/中信大厦.jpg')

""" 如果有可选参数 """
options = {}
options["with_face"] = 0

""" 带参数调用图像主体检测 """
result = client.objectDetect(image, options)

result = result['result']

print(result)

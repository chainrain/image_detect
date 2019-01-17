from AipImageClassify import client

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/仙人掌.jpg')

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用植物识别 """
result = client.plantDetect(image, options)

plant = result['result'][0]

print(plant['name'])
print(plant['baike_info'])
print(plant['score'])
from AipImageClassify import client

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/本田.jpg')

""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5

""" 带参数调用车辆识别 """
result = client.carDetect(image, options)

car = result['result'][0]

print(car['name'])
print(car['year'])
print(car['baike_info'])
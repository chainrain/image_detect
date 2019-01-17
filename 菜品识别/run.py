from AipImageClassify import client


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/哈士奇.jpg')

""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["filter_threshold"] = "0.7"
options["baike_num"] = 5

""" 带参数调用菜品识别 """
result = client.dishDetect(image, options)

food = result['result'][0]

print('名字',food['name'])
print('卡路里: ',food['calorie'])
print('是否有卡路里',food['has_calorie'])
print('百科信息',food['baike_info'])
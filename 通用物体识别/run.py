from AipImageClassify import client


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/home/python/Desktop/图像识别/image/狮身人面像.jpg')

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体识别 """
result = client.advancedGeneral(image, options)

# 最像值
print(result['result'][0]['keyword'])
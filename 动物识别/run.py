import AipImageClassify


"""图片"""
image = '/home/python/Desktop/图像识别/image/1.jpg'

"""图片需要参数"""
options = {}
options["top_num"] = 3  # 最像的前x个
options["baike_num"] = 5  # 返回相关信息

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(image)

""" 带参数调用动物识别 """
result = AipImageClassify.client.animalDetect(image, options=options)

# 最像值
print(result['result'][0]['name'])


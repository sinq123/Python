import AipFaceKey
from aip import AipFace
import base64
import os
import time
import shutil


# 接入百度AI人脸识别的参数
APP_ID = AipFaceKey.APP_ID
API_KEY = AipFaceKey.API_KEY
SECRET_KEY = AipFaceKey.SECRET_KEY
imageType = "BASE64"
options = {}
options["face_field"] = "gender,beauty"
options["face_type"] = "LIVE"

# 下载图片和筛选图片的文件夹
file_path = 'F://Pictrue/'
copy_file_path = 'F://highScore/'
file_lists = os.listdir(file_path)
# 登录AipFack
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
# 判断复制的文件夹是否存在
if not os.path.exists(copy_file_path):
    os.makedirs(copy_file_path)


# 将图片转换为BASE64格式，这是百度平台的要求
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')


for file_list in file_lists:
    result = aipFace.detect(get_file_content(os.path.join(file_path, file_list)), imageType, options)
    error_code = result['error_code']
    if error_code == 222202:
        # 没有人脸
        continue
    if error_code == 223110:
        # 人脸太多
        continue
    try:
        sex_type = result['result']['face_list'][-1]['gender']['type']
        # 只要美女图片
        if sex_type == 'male':
            continue
        beauty = result['result']['face_list'][-1]['beauty']
        new_beauty = round(beauty/10, 1)
        print(file_list, new_beauty)
        if new_beauty >= 6:
            copy_src = os.path.join(file_path, str(new_beauty)+'_'+file_list)
            copy_dst = os.path.join(copy_file_path, str(new_beauty)+'_'+file_list)
            # 重命名高分照片
            os.rename(os.path.join(file_path, file_list), copy_src)
            # 复制高分照片到另外的照片
            shutil.copyfile(copy_src, copy_dst)
            # 旧文件删除
            os.unlink(copy_src)
            time.sleep(1)
    except KeyError:
        pass
    except TypeError:
        pass

"""
os.getcwd() 返回当前目录
os.listdir(directory) 存储一个路径下的内容，形成列表，os.stat()
os.stat(path) 返回一个数值元组，
    st_mode:文件的访问权限
    st_ino：节点数
    st_dev:设备号
    st_nlink:连接号（UNIX）
    st_uid:所有者的用户ID
    st_gid：所有者的组ID
    st_size：文件大小
    st_atime:最后访问时间
    st_mtime：最后修改时间
    st_ctime:创建时间
os.path.split(path):将路径分割为符合当前操作系统的组成名称。返回一个元组
os.path.join(companents) 组合一个新的路径
os.path.normcase(path)规范化路径的大小写
os.walk(top, topdown=True, onerror=None, followlinks=False)自上而下目录，
"""
import os, os.path
import re
""" 
# 获取当前路径
print(os.getcwd())
# 拆分路径
print(os.path.split(os.getcwd()))
# 获取文件信息
print(os.stat("."))
# 列出文件目录内容
print(os.listdir("."))
 """


def print_pdf(root, dirs, files):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if not re.search(r".*\.pdf", path):
            continue
        if re.search(r" ", path):
            continue
        print(path)


for root, dirs, files in os.walk('.'):
    print_pdf(root, dirs, files)

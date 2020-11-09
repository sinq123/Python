# 文件操作
import os
# 时间
import time
# 文件移动，重命名， 移动，复制，删除
import shutil
# *开头配置所以文件
import glob


# 判断当前路径是否有文件
# 没有写入该文件
# 有 打印信息
def make_another_file():
    # 获取当前文件夹路径
    f = "%s" % (os.path.dirname(os.path.realpath(__file__)))
    f += "\\test.txt"
    if os.path.isfile(f):
        print("you are trying to create a file that already exists!")
    else:
        f = open(f, "w", encoding="UTF-8")
        f.write("This is how you create a new text file")
        f.close()


# 追加文件写入
# 判断是否有该文件， 有追加写入
# 无，创建改文件
def add_some_text():
    f = "%s" % (os.path.dirname(os.path.realpath(__file__)))
    f += "\\test.txt"
    if os.path.isfile(f):
        a = open(f, "a", encoding="UTF-8")
        a.write("\r\n Here is some additional text!")
        a.close()
    else:
        make_another_file()


# 读取文件操作
# 判断是否有该文件，有着读取并打印内容
def read_file():
    f = "%s" % (os.path.dirname(os.path.realpath(__file__)))
    f += "\\test.txt"
    if (os.path.isfile(f)):
        r = open(f, "r", encoding="UTF-8")
        print(r.read())
        r.close()
    else:
        print("无该文件")


# 分解完整路径
def split_fully(path):
    path, name = os.path.split(path)
    if (name == ""):
        return (path, )
    else:
        return split_fully(path) + (name, )


# 列举文件夹所以文件，并打印出绝对路径
def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print(os.path.join(dir_path, name))


# 列举文件夹所以文件
# 如文件夹，继续列举文文件夹的文件，知道列举完文件夹下所以内容
def print_tree(dir_path):
    for(name) in (os.listdir(dir_path)):
        path = os.path.join(dir_path, name)
        if (os.path.isdir(path)):
            print_tree(path)
        else:
            print(path)


# 版本控制，
# version > 0 时,路径增加一个后缀来表示
def make_version_path(path, version):
    if version == 0:
        # 0版本没有后缀，现在的版本。
        return path
    else:
        # 附加一个后缀来表示旧版本
        return path + "." + str(version)


# 版本控制
# 用递归方式先将旧+1处理
def rotate(path, version=0):
    # 我们旋转的版本的名字
    old_path = make_version_path(path, version)
    if not os.path.exists(old_path):
        # 根本不存在，那就抱怨吧
        raise IOError("'%s' 不存在" % (path))
    # 为该文件构造新的版本名称
    new_path = make_version_path(path, version+1)
    # 有这个名字的版本吗？
    if os.path.exists(new_path):
        # 是的，先把它旋转一下
        rotate(path, version+1)
    # 现在我们可以安全地重命名了
    shutil.move(old_path, new_path)


# 创建一个文件和删除文件
def rotate_log_file(path):
    if not os.path.exists(path):
        # 文件丢失了，所以创建它
        f = open(path, "w", encoding="UTF-8")
        f.close()
    rotate(path)
    # 删除文件，两个都可以
    # os.remove(path)
    # os.unlink(path)


# 创建文件夹和删除文件夹
def rotate_log_dir(path):
    # 必须有上一级目录
    # os.mkdir(path)
    # 不需要上一级目录
    # os.makedirs(path)
    # 删除目录 只针对空文件夹
    # os.rmdir(path)
    # 删除目录 包涵目录下的内容
    shutil.rmtree(path)


# 查找文件或？*开头的文件
def glob_File(path):
    return glob.glob(path)


if __name__ == "__main__":
    # make_another_file()
    # add_some_text()
    # read_file()
    """ # 组合路径
    # print(os.path.join("python", "test.txt")) """
    """ # 拆分路径
    # path, name = (os.path.split("E:\\python\\7章\\7章.py"))
    # print(path)
    # print(name) """

    """ # 分解完整路径
    # 获取拆分后的长度并每个都打印出来
    n = split_fully("E:\\python\\7章\\7章.py")
    for i in range(len(n)):
        print(n[i]) """

    """# 拆分扩展名
    # 包涵两个元素
    print(os.path.splitext("test.txt")) """

    """ # 修复和规范化路径
    print(os.path.normpath(r"E:\\python\7章\..\7章.py")) """

    # print_dir("C:\\Python\\Python38-32")

    # 排序
    # print(sorted(os.listdir("C:\\Python\\Python38-32")))

    # 判断是一个文件还是一个文件夹
    # os.path.isfile()判断是否一个文件 True：是，False：否
    # os.path.isdir()判断是否一个文件夹 True：是，False：否

    # print_tree("C:\\Python\\Python38-32")

    """ # 获取文件上次的修改时间
    mod_time = os.path.getmtime("C:\\Python\\Python38-32")
    print(time.ctime(mod_time))

    # 获取文件的大小
    n = os.path.getsize("C:\\Python\\Python38-32")
    print(n) """

    # 重命名
    # shutil.move("E:\\python\\text - 副本.txt", "E:\\python\\text1.txt")

    # 移动文件
    # shutil.move("E:\\python\\text1.txt", "E:\\")

    # 复制文件
    # shutil.copy("E:\\text1.txt", "E:\\python\\")

    # 删除文件
    # os.remove("E:\\python\\text1.txt")
    # os.unlink("E:\\text1.txt")

    print(glob_File("C:\\Program Files\\A*"))
    # 通配符
    # * A* 匹配A开头的文件 *.txt 匹配所以txt的文件
    # ？ 以问号为字符匹配
    # [...] 匹配[]的文件
    # [!...] 不匹配[]的文件

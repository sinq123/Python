# from string import Template
import string
import sys
import getopt
import os
"""
U = "Ab"
# 字符串大写
U = U.upper()
print(U)
# 字符串小写
U = U.lower()
print(U)
"""

# lambda用法
# 在filter中使用 lambda
# filter_me = [1, 2, 3, 4, 6, 7, 8, 11, 12, 14, 15, 19, 22]
# 这只对偶数返回 true (因为 x%2 是0，对奇数返回 false)
# result = filter(lambda x: x % 2 == 0, filter_me)
# print(*result)
# python 3.8 不允许这样操作
# func = lambda x: x % 2 == 0
# result = filter(lambda x: x % 2 == 0, filter_me)
# print(*result)
# lambda 主要用在map和filter函数

# Map 短路循环函数
# map_me = ["a", "b", "c", "d", "e", "f", "g"]
# result = map(lambda x: "The letter is %s\r\n" % x, map_me)
# print(*result)

# 列表解析
# # 创建一个列表，并打印偶数
# everything = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print([x for x in everything if x % 2 == 0])

# # 循环函数 range
# f = range(10, 20)
# print(*f)

# # 循环函数 range 生成间隔参数
# f = range(10, 55, 5)
# print(*f)

# # 字典
# # i(表示整数)，j(表示虚数)， l(表示长整数)， s(表示字符串)
# # f(表示浮点型)
# person = {"name": "James", "camera": "nikon", "handedness": "lefty", "baseball_team": "angels", "instrument": "guitar"}
# # print("%(name)s, %(camera)s, %(baseball_team)s" % person)
# person["height"] = 1.6
# person["weight"] = 80
# # Template 字符串替换方法
# t = string.Template("$name is $height m high and $weight kilos")
# print(t.substitute(person))

# # getopt 模块
# # 记住，在 sys.argv 列表中的第一件事是命令的名称 Remember, the first thing in the sys.argv list is the name of the command 
# # 你不需要那个 You don't need that
# cmdline_params = sys.argv[1:]

# opts, args = getopt.getopt(cmdline_params, 'hc:', ['help', 'config='])

# for option, parameter in opts:
#     if option == '-h' or option == '--help':
#         print("这个程序可以用“ h”或“ help”运行,")
#         print("也可以使用-c 或 -- config 文件来指定不同的配置文件")

#     if option in ('-c', '--config'): # 这和上面的意思一样
#         print("Using configuratio file %s" % parameter)

# Window 启动进程方式
# spawnl 传递一个简单的列表
# spawnle 传递一个包括名称和简单的字典
# spawnv 传递一个列表
# spawnve 传递一个包括名称和字典

if sys.platform == 'win32':
    print("在windows上运行")
    command = "cmd.exe"
    params = []

if sys.platform == 'linux2':
    print("在一个 linux 系统上运行, 由%s确定" % (sys.platform))
    command = "/bin/uname"
    params = ['uname', '-a']

print("运行 %s" % (command))
os.system(command)
# os.spawnv(os.P_WAIT, command, params)

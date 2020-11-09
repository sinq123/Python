# 1
for i in (0, 1, 2, 3, 4):
    if (True == i):
        print("True")
    else:
        print("False")

#2
s = input("输入一个正数字: ")
# 判断是否数字
if s.strip().isdigit():
    i = int(s)
    if i < 0:
        print("这是一个负数")
    elif i > 9:
        print("这是一个两位数")
    else:
        print("这是一个0-9的数")
else:
    print("非数字")


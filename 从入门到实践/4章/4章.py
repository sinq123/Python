"""
# 判断是否为数字


def is_number(s):
    try:
        float(s)
        return False
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return False
    except (TypeError, ValueError):
        pass
    return True

# 无限循环判断跳出循环方式
age = 0
while 1:
    how_old = input("你的年龄: ")
    if is_number(how_old):
        print("输入的不是年龄")
        break
    num = int(how_old)
    age = age+num
    print("你的年纪是:%d" % (age))

"""
"""
# continue 继续循环
for foot in ("pate", "cheese", "rotten apples", "crackes", "whip cream", "tomato soup"):
    if foot[0:6] == "rotten":
        continue
    print("Hey, you can %s" % (foot))

"""
# 抛出异常数据
fridge_contents = {"egg": 8, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 13}
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice!")
except KeyError:
    print("Awww, there is no juice. Let's go shopping!")

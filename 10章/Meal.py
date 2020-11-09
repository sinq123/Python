"""
用Python制作膳食的模块。
导入此模块，然后调用
makeBreakfast（）、makeDinner（）或makeLunch（）。
"""
"""设定公有类, 调用模块 from Meal import *"""
__all__ = ['Meal', 'AngryChefException', 'makeBreakfast',
           'makeLunch', 'makeDinner', 'Breakfast', 'Lunch', 'Dinner']


# 助手函数。
def makeLunch():
    """ 创建午餐对象。 """
    return Lunch()


def makeBreakfast():
    """ 创建早餐对象。 """
    return Breakfast()


def makeDinner():
    """ 创建晚餐对象。 """
    return Dinner()


# 异常类。
class SensitiveArtistException(Exception):
    """ 一个过于敏感的艺术家提出的例外。
    艺术类型的基类
    """
    pass


class AngryChefException(SensitiveArtistException):
    '''表示厨师不高兴的异常'''
    A = "白痴"
    pass


class Meal:
    """
    盛放食物和饮料。
    在真正的面向对象的传统中，这个类包括食物和饮料的setter方法。
    调用printIt来漂亮地打印值。
    """
    def __init__(self, food="omelet", drink="coffee"):
        """ 初始化为默认值。 """
        self.name = "generic meal"
        self.food = food
        self.drink = drink

    def printIt(self, prefix=""):
        """ 把数据打印出来。 """
        print(prefix, "名称=", self.name, self.food, "和", self.drink)

    # 准备食物。
    def setFood(self, food="omelet"):
        self.food = food

    # 准备饮料。
    def setDrink(self, drink="coffee"):
        self.drink = drink

    # 名字
    def setName(self, name=""):
        self.name = name


class Breakfast(Meal):
    """ 保存早餐的食物和饮料。 """
    def __init__(self):
        """ 用煎蛋和咖啡初始化 """
        Meal.__init__(self, "omelet", "coffee")
        self.setName("breakfast")


class Lunch(Meal):
    """ 为午餐准备食物和饮料。 """
    def __init__(self):
        """ 用三明治和杜松子酒和滋补品初始化。 """
        Meal.__init__(self, "sandwich", "gin and tonic")
        self.setName("midday meal")

    # 覆盖setFood（）
    def setFood(self, food="sandwich"):
        if (food != "sandwich" and food != "omelet"):
            # 输出异常参数
            raise AngryChefException
        Meal.setFood(self, food)


class Dinner(Meal):
    """ 为晚餐准备食物和饮料。 """
    def __init__(self):
        """ 用牛排和梅洛初始化。 """
        Meal.__init__(self, "steak", "merlot")
        self.setName("dinner")

    def printIt(self, prefix=""):
        """ 打印得更漂亮。 """
        print(prefix, "美食家", self.name, self.food, "和", self.drink)


def test():
    """ 测试功能。 """
    print("模块餐测试")

    # Generic no arguments
    print("试餐班")
    m = Meal()

    m.printIt('\t')

    m = Meal("green eggs and ham", "tea")
    m.printIt("\t")

    # 测试早餐
    print("Testing Breakfast class")
    b = Breakfast()
    b.printIt("\t")

    b.setName("breaking of the fast")
    b.printIt("\t")

    # 测试晚餐
    print('Testing Dinner class.')
    d = Dinner()
    d.printIt("\t")

    # 测试午餐
    print('Testing Lunch class.')
    l = Lunch()
    l.printIt("\t")

    print('Calling Lunch.setFood().')

    try:
        l.setFood('hotdog')
    except AngryChefException:
        print("\t", 'The chef is angry. Pick an omelet.')


if __name__ == "__main__":
    test()

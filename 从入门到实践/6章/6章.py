class Fridge:
    """This class impements a fridge where ingredients can be added and removed individually,
    or in groups."""

    def __init__(self, items):
        if (isinstance(items, dict)):  # 判断是否字典
            self.items = items
        else:
            raise TypeError("Fridge requires a dictionary but was given %s" % (type(items)))
        return 

    # 内部操作函数
    # food_name 字符串，字典的key
    # quantity 增加的数量
    def __add_multi(self, food_name, quantity):
        if (food_name not in self.items):
            # 等于输入的数据
            self.items[food_name] = quantity
        else:
            # 字典增加数量 原来的+增加的个数
            self.items[food_name] = self.items[food_name] + quantity

    # 增加一个操作
    # food_name str
    def add_one(self, food_name):
        if (isinstance(food_name, str)):  # 判断是否字符串
            self.__add_multi(food_name, 1)
            return True
        else:
            raise TypeError("add_one requires a string, given a %s" % (type(food_name)))
            return False

    # 增加很多操作
    # food_dict 字典
    def add_many(self, food_dict):
        if (isinstance(food_dict, dict)):  # 判断是否字典
            for item in food_dict.keys():
                self.__add_multi(item, food_dict[item])
        else:
            raise TypeError("add_many requires a dictonary, gor a %s" % (type(food_dict)))
        return

    # food_name 字符串 字典的key
    # quantity 数量 默认1
    # 返回99: 报错
    # 返回0: 少于设定的数量
    # 返回1: 多于等于设定的数量
    def has(self, food_name, quantity=1):
        return self.has_various({food_name: quantity})

    # foods 字典
    # 返回99: 报错
    # 返回0: 少于设定的数量
    # 返回1: 多于等于设定的数量
    def has_various(self, foods):
        try:
            for food in foods.keys():
                if (self.items[food] < foods[food]):
                    return 0
            return 1
        except KeyError:
            return 99

    # 取出食物
    # 内部函数
    # food_name 字符串 对应字典的key
    # quantity 数量
    def __get_mulit(self, food_name, quantity):
        try:
            if (self.items[food_name] is None):
                return -1
            elif (self.items[food_name] < quantity):
                return 0
            else:
                self.items[food_name] = self.items[food_name] - quantity
                return 1
        except TypeError:
            return 99

    # food_name 字符串 对应字典的key
    def get_one(self, food_name):
        if not(isinstance(food_name, str)):
            raise TypeError("get_one requires a string, given a %s" % (type(food_name)))
        else:
            result = self.__get_mulit(food_name, 1)
        return result

    # food_dict 字典
    def get_many(self, food_dict):
        n = self.has_various(food_dict)
        if (n == 1):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_mulit(item, food_dict[item])
            return foods_removed

    def get_ingreadients(self, food):
        try:
            ingredients = self.get_many(food.get_ingredients())
        except AttributeError:
            return False
        if (ingredients is not False):
            return ingredients


class Omelet:
    def __init__(self, kind="cheese"):
        self.set_kind(kind)
        return

    def __ingredients__(self):
        return self.needed_ingredients

    def get_ingredients(self):
        return self.__ingredients__()

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if (possible_ingredients is False):
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients
            return

    def __known_kinds(self, kind):
        k = {"eggs": 2, "milk": 1, "cheese": 1}
        if (kind == "cheese"):
            return k
        elif (kind == "mushroom"):
            k["mushroom"] = 2
            return k
        elif (kind == "onion"):
            k["onion"] = 1
            return k
        else:
            return False

    def get_ingreadients(self, fridge):
        self.from_fridge = fridge.get_ingreadients(self)

    def mix(self):
        for ingredient in self.from_fridge.keys():
            print("Mixing %d %s for the %s omelet" % (self.from_fridge[ingredient], ingredient, self.kind))
            self.mixed = True

    def make(self):
        if (self.mixed is True):
            print("Cooking the %s omelet!" % (self.kind))
            self.cooked = True


o = Omelet()
f = Fridge({"cheese": 5, "milk": 4, "eggs": 12})
o.get_ingreadients(f)
o.mix()
o.make()
"""
f = Fridge({"eggs": 6, "milk": 4, "cheese": 3})
print(f.items)
print(f.add_one("grape"))
print(f.items)
f.add_many({"mushroom": 5, "tomato": 3})
print(f.items)

n = f.has("grape", 1)
if (n == 1):
    print("grape only one")
elif (n == 0):
    print("  ")
else:
    print("  ")

"""
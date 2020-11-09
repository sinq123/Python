class Omelet:
    """
    这个类创建一个omelet对象。煎蛋卷可以有两种状态：配料或煮熟。
    omelet对象具有以下接口：
    get_kind（）-返回一个omelet类型的字符串
    set_kind（kind）-将煎蛋卷设置为名为
    mix（）-从冰箱收集所有成分后调用
    cook() -煎蛋卷
    """
    def __init__(self, kind="cheese"):
        """
        这会将Omelet类初始化为默认的cheese Omelet。
        """
        self.set_kind(kind)
        return

    def __ingredients__(self):
        """
        由冰箱或其他需要作用于配料的物体调用的内部方法。
        """
        return self.needed_ingredients

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if (possible_ingredients is False):
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients

    def set_new_kind(self, name, ingredients):
        self.kind = name
        self.needed_ingredients = ingredients
        return

    def __known_kinds(self, kind):
        dic = {"eggs": 2, "milk": 1, "cheese": 1}
        if kind == "cheese":
            return dic
        elif kind == "mushroom":
            dic["mushroom"] = 2
            return dic
        elif kind == "onion":
            dic["onion"] = 1
            return dic
        else:
            return False

    def get_ingredients(self, fridge):
        self.from_fridge = fridge.get_ingredients(self)

    def mix(self):
        for ingredient in self.from_fridge.keys():
            print("Mixing %d %s for the %s omelet" % (self.from_fridge[ingredient], ingredient, self.kind))
        self.mixed = True

    def make(self):
        if (self.mixed is True):
            print("Cooking the %s omelet!" % self.kind)
            self.cooked = True

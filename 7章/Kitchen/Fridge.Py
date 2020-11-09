class Fridge:
    """
    这个类实现了一个冰箱，可以在其中单独或分组添加和删除。冰箱将保留每种添加或去除的成分的计数，如果有足够数量的成分不存在。
    方法：has（food_name[，quantity]）-检查字符串food_name是否在冰箱中。
    如果不指定数字，数量将设置为1。有各种各样的食物吗？
    检查冰箱里是否有足够的食物添加一个（食物名称）-将一个食物名称添加到冰箱add_many（food_dict）
    -添加一整本装满食物的字典获取一个（食物名称）-从冰箱中取出一个食物名称多买（食物）拿出一整本字典里的食物。
    获取配料（食物）-如果传递的对象具有配料方法，get_many将调用此函数以获取成分列表。
    """
    def __init__(self, items={}):
        """可选地传入项的初始字典"""
        if not(isinstance(items, dict)):
            raise TypeError("冰箱需要一本字典，给了 %s" % type(items))
        self.items = items
        return

    def __add_multi(self, food_name, quantity):
        """
        __添加多个（食品名称、数量）-添加多个
        食物。返回添加的项目数
        这只应在类型检查完成后在内部使用
        完成
        """
        if (food_name not in self.items):
            self.items[food_name] = quantity
        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        """
        add_one（food_name）-在冰箱中添加一个food_name
        返回True，
        如果food_name不是字符串，则引发TypeError。
        """
        if not(isinstance(food_name, str)):
            raise TypeError("add_one 需要的是字符串, 给了 %s" % type(food_name))
        else:
            self.__add_multi(food_name, 1)
        return True

    def add_many(self, food_dict):
        """
        add_many（food_dict）-添加一整本以食物为键的字典数量作为价值。
        返回包含已删除食物的字典。
        如果food dict不是字典，则引发TypeError
        如果冰箱中没有足够的食物，则返回False。
        """
        if not(isinstance(food_dict, dict)):
            raise TypeError("add_many 需要一本字典, 给了 %s" % food_dict)
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return

    def has(self, food_name, quantity=1):
        """
        has（food_name，[数量]）-检查字符串food_name是否在冰箱中。数量默认为1，如果有足够的数量，
        则返回True，否则返回False。
        """
        return self.has_various({food_name: quantity})

    def has_various(self, foods):
        """
        has_variety（foods）确定字典中的food_name是否有足够的元素来满足请求。
        如果有足够的值，则返回true。
        如果没有，如果元素不存在，
        """
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False

    def __get_multi(self, food_name, quantity):
        """
        _获取多个（食物名称、数量）-移除多个食物项。
        返回删除的项目数如果冰箱中没有足够的食物名，则返回False。
        这只应在类型检查完成后在内部使用
        """
        try:
            if (self.items[food_name] is None):
                return False
            if (quantity > self.items[food_name]):
                return False
            self.items[food_name] = self.items[food_name] - quantity
        except KeyError:
            return False
        return quantity

    def get_one(self, food_name):
        """
        获取一个（食物名称）-从冰箱中取出一个食物名称，返回一个包含食物的字典：结果是1，
        如果冰箱中没有足够的食物，则返回False。
        """
        if not(isinstance(food_name, str)):
            raise TypeError("需要一个字符串, 给的是 %s" % type(food_name))
        else:
            result = self.__get_multi(food_name, 1)
        return result

    def get_many(self, food_dict):
        """
        多买（食物）拿出一整本字典里的食物。
        返回包含所有成分的词典
        如果没有足够的成分或字典，则返回False
        没有提供。
        """
        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed

    def get_ingredients(self, food):
        """
        获取食材（食物）-如果传递了一个具有“获取食材”方法的对象，则获取许多将调用此函数以获取食材列表。
        """
        try:
            ingredients = self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        
        if (ingredients is not False):
            return ingredients

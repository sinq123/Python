
class Recipe:
    """
    这个班有煎蛋卷班的食谱
    """
    
    def __init__(self):
        self.set_default_recipes()
        return
    
    def set_default_recipes(self):
        self.recipes = {"cheese": {"eggs": 2, "milk": 1, "cheese": 1},
                        "mushroom": {"eggs": 2, "milk": 1, "cheese": 1, "mushroom": 2},
                        "onion": {"eggs": 2, "milk": 1, "cheese": 1, "onion": 1}}

    def get(self, name):
        """
        get（name）-返回一个字典，其中包含了制作名煎蛋卷所需的成分。
        当名称未知时，返回False
        """
        try:
            recipe = self.recipes[name]
            return recipe
        except KeyError:
            return False

    def create(self, name, ingredients):
        """
        创建（名称，成分）-添加名为“名称”的煎蛋饼和成分“成分”，这是一个字典。
        """
        self.recipes[name] = ingredients


if __name__ == '__main__':
    r = Recipe()
    if (r.recipes != {"cheese": {"eggs": 2, "milk": 1, "cheese": 1},
                      "mushroom": {"eggs": 2, "milk": 1, "cheese": 1, "mushroom": 2},
                      "onion": {"eggs": 2, "milk": 1, "cheese": 1, "onion": 1}}):
        print("失败：默认配方不是正确的列表")
    cheese_omelette = r.get("cheese")
    if cheese_omelette != {"eggs": 2, "milk": 1, "cheese": 1}:
        print("失败：奶酪煎蛋卷的配料不对")
    western_ingredients = {"eggs": 2, "milk": 1, "cheese": 1, "ham": 1, "peppers": 1, "onion": 1}
    r.create("western", western_ingredients)
    if r.get("western") != western_ingredients:
        print("没有为西餐准备好配料")


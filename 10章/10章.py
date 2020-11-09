""" # import imp
# # 重新加载模块
# imp.reload(imp)

# # 第一种导入模块的方法
# import food
# print(food.favoriteFood())

# # 第二种导入模块的类
# from food import favoriteFood
# print(favoriteFood())
 """
""" 导入模块第一种方法 """
""" import Meal

print("Making a Breakfast")
breakfast = Meal.makeBreakfast()

breakfast.printIt("\t")

print("Making a Lunch")
lunch = Meal.makeLunch()

try:
    lunch.setFood("pancakes")
except Meal.AngryChefException:
    print("\t", Meal.AngryChefException().A)
    print("\t", "Cannot make a lunch of pancakes.")
    print("\t", "The chef is angry. Pick an omelet.") """

""" 导入模块第二种方法 """
from Meal import *

print("Making a Breakfast")
breakfast = makeBreakfast()

breakfast.printIt("\t")

print("Making a Lunch")
lunch = makeLunch()

try:
    lunch.setFood("pancakes")
except AngryChefException:
    print("\t", AngryChefException().A)
    print("\t", "Cannot make a lunch of pancakes.")
    print("\t", "The chef is angry. Pick an omelet.")

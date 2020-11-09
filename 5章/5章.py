def in_fridge():
    """黄丽霞大笨蛋
    """
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count


fridge = {'apples': 10, 'oranges': 3, 'milk': 2}
wanted_food = 'apples'
print("%s" % (in_fridge.__doc__))
print(in_fridge())

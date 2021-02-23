dairy_section = ["2009.03.31", "佳贝艾特", "800", "进口"]
print(dairy_section[0])
print(dairy_section[-1])

milk_expiration = ("2009", "03", "31")
print("This milk carton will expire on %s/%s/%s" % (milk_expiration[1], milk_expiration[2], milk_expiration[0]))

milk_carton = {}
milk_carton["expiration_date"] = milk_expiration
milk_carton["fl_oz"] = "20x40"
milk_carton["Cost"] = 468
milk_carton["brand_name"] = "佳贝艾特"
listmilk = milk_carton.values()
print(list(listmilk))
n = milk_carton["Cost"] * 6
print(n)

cheeses = ["奶酪饼", "奶酪棒"]
n2 = len(dairy_section)
dairy_section.extend(cheeses)
n1 = len(dairy_section)
print(dairy_section)
if n1 > n2:
    a = 0
    while a != len(cheeses):
        cheeses.pop()
print(dairy_section[4][2])


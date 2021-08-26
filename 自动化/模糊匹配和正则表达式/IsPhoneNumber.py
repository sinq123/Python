# 模糊匹配电话格式 格式为 ***-***-****

#def IsPhoneNumber(Text):
#    if (len(Text) != 12):
#        #长度不对
#        return False
#    for i in range(0, 3):
#        if not Text[i].isdecimal():
#            #前三个不是数字
#            return False
#    if (Text[3] != "-"):
#        #分隔符不是-
#        return False
#    for i in range(4, 7):
#        if not Text[i].isdecimal():
#            #中间三个不是数字
#            return False
#    if (Text[7] != "-"):
#        #分隔符不是-
#        return False
#    for i in range(8, 12):
#        if not Text[i].isdecimal():
#            #后四个不是数字
#            return False
#    return True

#print(IsPhoneNumber('415-123-1234'))
#print(IsPhoneNumber('Is'))

#使用正则表达式
import re
#使用()来进行分组分了3组
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

mo = phoneNumRegex.search("电话号码为：415-555-4242.")

print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group())
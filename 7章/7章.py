"""
设置自定义包的路劲
"""
import sys
sys.path.append("E:\\python\\7章\\Kitchen")

import Kitchen


# 程序入口(检查)
if __name__ == "__main__":
    r = Kitchen.Recipe()
    print(r.recipes)


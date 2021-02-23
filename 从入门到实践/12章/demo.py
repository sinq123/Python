'''
测试代码的方法
'''
# 断言
# Demonstrate the use of assert()

# large = 1000
# string = 'This is a string '
# float = 1.0
# broken_int = 'This should have been an int'

# assert large > 500
# print(large)
# assert isinstance(string, str)
# print(type(string))
# assert isinstance(broken_int, int)
# print(type(broken_int))

# 测试用例和测试套件

import unittest


class ArithTest (unittest.TestCase):
    def runTest(self):
        ''' Test addition and succeed'''
        self.failUnless(1 + 1 == 2, 'one plus one fails!')
        self.failIf(1 + 1 != 2, 'one plus one fails again!')
        self.failUnlessEqual(1 + 1, 2, 'more trouble with one plus one')
        self.failIfEqual(1 + 1, 2, 'expected failure here')
        self.failIfEqual(1 + 1, 2, 'second failure')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ArithTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)

import math
from threading import Thread
import time
import sys


class SquareRootCalculator:
    """
    这个类产生一个单独的线程来计算一串平方根并每秒在其中检查一次，
    直到它完成
    """
    def __init__(self, target):
        """
        打开计算器线程，在等待它完成时，定期监测它的进度。
        """
        self.results = []
        counter = self.CalculatorThread(self, target)
        print("打开计算器线程...")
        counter.start()
        while len(self.results) < (target):
            print("到目前为止算出的平方根%d" % (len(self.results)))
            time.sleep(1)
        print("计算%s平方根; 最后一个是 sqrt(%d)=%.2f" % (target, len(self.results), self.results[-1]))

    class CalculatorThread(Thread):
        """
        一个单独的线程，实际上做计算
        """
        def __init__(self, contorller, target):
            """
            设置这个线程，
            包括使它成为一个守护进程线程，
            以便脚本可以在没有完成该线程的情况下结束。
            """
            Thread.__init__(self)
            self.contorller = contorller
            self.target = target
            self.setDaemon(True)

        def run(self):
            """
            计算1和目标之间加数的平方根，
            包括
            """
            for i in range(1, self.target+1):
                self.contorller.results.append(math.sqrt(i))


if __name__ == "__main__":
    limit = None
    if len(sys.argv) >= 1:
        limit = sys.argv[0]
        try:
            # int(''.join(list(filter(str.isdigit, limit))))只保留数字
            # str(''.join(list(filter(str.isalpha, limit))))只保留字母
            # str(''.join(list(filter(str.isalnum, limit))))只保留字母和数字
            # float(''.join(list(filter(lambda ch: ch in ‘0123456789.’, limit))))
            limit = int(''.join(list(filter(str.isdigit, limit))))
            print(limit)
            SquareRootCalculator(limit)
        except ValueError:
            print("用法:% s [计算平方根的数目]" % (sys.argv[0]))

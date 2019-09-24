from threading import Condition

from mypy.typing import Callable

"""
    简单使用锁变量进行控制流程
"""


class Foo:
    def __init__(self):
        self.count = 0
        self.cond = Condition()

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self.cond:
            while self.count != 0:
                self.cond.wait()
            printFirst()
            self.count += 1
            self.cond.notify_all()

    def second(self, printSecond: "Callable[[], None]") -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.cond.acquire():
            while self.count != 1:
                self.cond.wait()
            printSecond()
            self.count += 1
            self.cond.notify_all()

    def third(self, printThird: "Callable[[], None]") -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.cond.acquire():
            while self.count != 2:
                self.cond.wait()
            printThird()
            self.count += 1
            self.cond.notify_all()

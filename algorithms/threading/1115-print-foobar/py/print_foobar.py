from mypy.typing import Callable

from threading import Lock

"""
    设置两个 锁
    首先锁定 bar，
    进而对 foo 加锁，
    等待 foo 执行完毕之后进而释放 bar的锁
    进而 申请 bar 的锁
    执行 bar
    执行完毕 释放 foo 锁

    依次循环
"""


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()

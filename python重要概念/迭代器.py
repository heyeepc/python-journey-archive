class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)  # 返回迭代器对象
class CountDownIterator:
    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 结束迭代
        value = self.current
        self.current -= 1
        return value

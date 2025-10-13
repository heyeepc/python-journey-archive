def custom_range_iterator(start, stop, step):
    current = start
    if step > 0:
        # 正步长的情况
        while current < stop:
            yield current  # 暂停执行，返回当前值，等待下次调用
            current += step
    elif step < 0:
        # 负步长的情况
        while current > stop:
            yield current
            current += step
    # 如果 step == 0，Python 会抛出 ValueError
    # 如果 start >= stop 且 step > 0，或 start <= stop 且 step < 0，则不执行任何操作。

# for i in range(1, 10, 2): 的迭代过程：
# for i in custom_range_iterator(1, 10, 2):
# 第一次：i = 1 (current=1, yield 1)
# 第二次：i = 3 (current=3, yield 3)
# 第三次：i = 5 (current=5, yield 5)
# 第四次：i = 7 (current=7, yield 7)
# 第五次：i = 9 (current=9, yield 9)
# 停止 (current=11, 11不小于10，while结束)

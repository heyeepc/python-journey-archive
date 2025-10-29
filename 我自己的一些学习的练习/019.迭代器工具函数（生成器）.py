# 基础生成器：产生数字 1 到 5
def num_generator():
    for i in range(1, 6):
        yield i

# 例子：g_double = map(lambda x: x * 2, num_generator())
# 这里的 lambda x: x * 2 就是我们的 function（匿名函数），作用是把数字乘以 2。
g_double = map(lambda x: x * 2, num_generator())

# 例子：g_even = filter(lambda x: x % 2 == 0, num_generator())
# 这里的 lambda x: x % 2 == 0 就是我们的 function，作用是检查数字是否为偶数 (True/False)。
g_even = filter(lambda x: x % 2 == 0, num_generator())

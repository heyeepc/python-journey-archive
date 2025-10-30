# 程序在遇到一个表达式时，不会立刻求值，而是等到真正需要结果时才进行计算。

nums = range(1, 10**9)
print(nums)        # 不会生成十亿个数字
print(nums[0])     # 只在这里取出需要的值


def squares():
    for i in range(1, 6):
        print(f"正在计算 {i} 的平方...")
        yield i * i  # 惰性生成

gen = squares()
for value in gen:
    print("得到：", value)

#yield 会让函数“暂停”，只有当循环取下一个值时，才继续计算。


a = [4.95,9.95,14.95,24.95]

z = map(lambda x:x * 0.6,a)

print(list(z))

# ( 表达式 for 变量 in 可迭代对象 if 条件 )
# 要计算 1 到 10 中所有偶数的平方和。

nums = range(1, 11)
gen_squares = (x * x for x in nums if x % 2 == 0)
total_sum = sum(gen_squares) 

print(f"生成器对象: {gen_squares}") # 打印的是一个生成器对象
print(f"偶数的平方和: {total_sum}") # 输出: 220 (4+16+36+64+100)

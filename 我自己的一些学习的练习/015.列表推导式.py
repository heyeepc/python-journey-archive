#( 表达式 for 变量 in 可迭代对象 if 条件 )
nums = range(1, 11)

# 列表推导式 (方括号)
list_squares = [x * x for x in nums if x % 2 == 0]

print(f"列表对象: {list_squares}") # 输出: [4, 16, 36, 64, 100]
print(f"偶数的平方和: {sum(list_squares)}") # 输出: 220

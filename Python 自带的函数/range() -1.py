# 生成 0, 1, 2, 3, 4
r1 = range(5)
print(list(r1)) # 通过 list() 转换为列表以便查看内容
# 输出: [0, 1, 2, 3, 4]

for i in range(5):
    print(i)
# 输出:
# 0
# 1
# 2
# 3
# 4

# 生成 2, 3, 4, 5
r2 = range(2, 6)
print(list(r2))
# 输出: [2, 3, 4, 5]

for i in range(2, 6):
    print(i)
# 输出:
# 2
# 3
# 4
# 5

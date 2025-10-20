nums = [5, 2, 8, 1]
min_val = float('inf')  # 初始设成最大可能值
for x in nums:
    if x < min_val:
        min_val = x
print(min_val)  # 输出 1

nums = [5, 2, 8, 1]
max_val = float('-inf')
for x in nums:
    if x > max_val:
        max_val = x
print(max_val)  # 输出 8

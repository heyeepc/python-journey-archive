devices_a = {101, 102, 103, 104}

devices_b = {103, 104, 105, 106}

print(f"A集合: {devices_a}")
print(f"B集合: {devices_b}")
print("------------------------")

# 1. 交集 (Intersection)
# 找到同时通过 A 和 B 
intersection_result = devices_a.intersection(devices_b)
# 或者使用运算符: devices_a & devices_b
print(f"1. 交集 (共同发现): {intersection_result}")
# 输出: {103, 104}

# 2. 并集 (Union)
# 找到通过 A 或 B 发现的所有不重复
union_result = devices_a.union(devices_b)
# 或者使用运算符: devices_a | devices_b
print(f"2. 并集 (所有不重复): {union_result}")
# 输出: {101, 102, 103, 104, 105, 106}

# 3. 差集 (Difference)
# 找到只通过 A 发现的 (在 A 中，不在 B 中)
difference_result = devices_a.difference(devices_b)
# 或者使用运算符: devices_a - devices_b
print(f"3. 差集 (只在A中发现): {difference_result}")
# 输出: {101, 102}

# 4. 对称差集 (Symmetric Difference)
# 找到在 A 或 B 中，但不同时在两者中发现的
symmetric_difference_result = devices_a.symmetric_difference(devices_b)
# 或者使用运算符: devices_a ^ devices_b
print(f"4. 对称差集 (任一独有): {symmetric_difference_result}")
# 输出: {101, 102, 105, 106}

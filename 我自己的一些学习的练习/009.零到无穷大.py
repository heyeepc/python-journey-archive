# 使用 float('inf') 来代表正无穷大
positive_infinity = float('inf')

# 范围 (0 到 无穷大，包括 0)
range_tuple = (0.0, positive_infinity)

print(range_tuple)  # 输出: (0.0, inf)

# 使用 float('-inf') 来代表负无穷大
negative_infinity = float('-inf')

# 范围 (负无穷大 到 0，包括 0)
range_tuple = (negative_infinity, 0.0)

print(range_tuple) # 输出: (-inf, 0.0)

# 范围 (0 到 无穷大，约定 None 表示无穷)
range_tuple = (0.0, None)

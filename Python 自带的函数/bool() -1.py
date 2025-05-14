# 转换为布尔值 (非空字符串、非零数字、非空集合等都为 True，空字符串、零、空集合等为 False)
print(bool(1))     # 输出: True
print(bool(0))     # 输出: False
print(bool("hello")) # 输出: True
print(bool(""))    # 输出: False
print(bool([]))    # 输出: False

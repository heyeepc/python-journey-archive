my_dict = {'name': 'Alice', 'age': 30}

# 键存在时
print(my_dict.get('name')) # 输出: Alice
print(my_dict.get('age'))  # 输出: 30

# 键不存在时，不提供默认值
print(my_dict.get('city')) # 输出: None

# 键不存在时，提供默认值
print(my_dict.get('city', 'Unknown')) # 输出: Unknown
print(my_dict.get('salary', 0)) # 输出: 0

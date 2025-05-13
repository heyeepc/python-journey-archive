my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

values_view = my_dict.values()
print(values_view) # 输出: dict_values(['Alice', 30, 'New York'])
print(type(values_view)) # 输出: <class 'dict_values'>

print("迭代值:")
for value in my_dict.values():
    print(value)

# 检查值是否存在（效率不高）
print('Alice' in values_view) # 输出: True
print(40 in values_view) # 输出: False

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

keys_view = my_dict.keys()
print(keys_view) # 输出: dict_keys(['name', 'age', 'city'])
print(type(keys_view)) # 输出: <class 'dict_keys'>

print("迭代键:")
for key in my_dict.keys():
    print(key)

# 检查键是否存在
print('name' in keys_view) # 输出: True
print('address' in keys_view) # 输出: False

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

items_view = my_dict.items()
print(items_view) # 输出: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
print(type(items_view)) # 输出: <class 'dict_items'>

print("迭代键值对:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

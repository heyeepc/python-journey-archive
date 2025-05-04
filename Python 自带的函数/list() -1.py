empty_list = list()
print(empty_list)
# 输出: []
print(type(empty_list))
# 输出: <class 'list'>

# 从元组创建列表
my_tuple = (1, 2, 3, 4)
list_from_tuple = list(my_tuple)
print(list_from_tuple)
# 输出: [1, 2, 3, 4]

# 从字符串创建列表 (每个字符成为列表的一个元素)
my_string = "hello"
list_from_string = list(my_string)
print(list_from_string)
# 输出: ['h', 'e', 'l', 'l', 'o']

# 从集合创建列表 (集合是无序的，转换后列表的顺序不确定)
my_set = {10, 20, 30, 40}
list_from_set = list(my_set)
print(list_from_set)
# 输出: [10, 20, 30, 40] (元素的顺序可能不同)

# 从字典创建列表 (默认情况下，列表将包含字典的键)
my_dict = {'a': 1, 'b': 2, 'c': 3}
list_from_dict_keys = list(my_dict)
print(list_from_dict_keys)
# 输出: ['a', 'b', 'c']

# 从字典的值创建列表
list_from_dict_values = list(my_dict.values())
print(list_from_dict_values)
# 输出: [1, 2, 3]

# 从字典的键值对创建列表 (列表将包含键值对元组)
list_from_dict_items = list(my_dict.items())
print(list_from_dict_items)
# 输出: [('a', 1), ('b', 2), ('c', 3)]

# 从 range 对象创建列表
my_range = range(5) # range 对象表示序列 0, 1, 2, 3, 4
list_from_range = list(my_range)
print(list_from_range)
# 输出: [0, 1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list) # 输出: [1, 2, 3, 4, 5]

my_list.insert(1, 1.5)
print(my_list) # 输出: [1, 1.5, 2, 3, 4, 5]

my_list.remove(2)
print(my_list) # 输出: [1, 1.5, 3, 4, 5]

popped_item = my_list.pop() # 移除最后一个
print(popped_item) # 输出: 5
print(my_list)     # 输出: [1, 1.5, 3, 4]

popped_item_at_index = my_list.pop(1) # 移除索引为 1 的元素
print(popped_item_at_index) # 输出: 1.5
print(my_list)              # 输出: [1, 3, 4]

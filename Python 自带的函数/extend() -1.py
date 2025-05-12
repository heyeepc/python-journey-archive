my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list) # 输出: [1, 2, 3, 4, 5]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
# 输出: [1, 2, 3, 4, 5, 6]
# list1 被修改，list2 不变

list_a = [1, 2]
list_b = [3, 4]
list_a.append(list_b)
print(list_a) # 输出: [1, 2, [3, 4]]


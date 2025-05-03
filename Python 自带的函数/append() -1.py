my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# 输出: [1, 2, 3, 4]

my_list = [1, 'hello']
my_list.append(True)
my_list.append(3.14)
print(my_list)
# 输出: [1, 'hello', True, 3.14]

my_list = ['apple', 'banana']
my_list.append('cherry')
print(my_list)
# 输出: ['apple', 'banana', 'cherry']

list1 = [1, 2]
list2 = [3, 4]
list1.append(list2)
print(list1)
# 输出: [1, 2, [3, 4]]
# 注意：list2 作为一个整体被添加，形成了嵌套。

squares = []
for i in range(5):
    squares.append(i * i)
print(squares)
# 输出: [0, 1, 4, 9, 16]]

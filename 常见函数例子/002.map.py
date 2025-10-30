list1 = [1, 2, 3]
list2 = [2, 3, 4]

result = list(map(lambda x: x[0] + x[1]， zip(list1, list2)))
print(result)  # 输出: [3, 5, 7]

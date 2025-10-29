# 本练习将创建一个程序，来计算用户输入的值集合的平均值。用户将输入0作为标记值，表示不再提供任何值。如果用户输入的第一个值是0，则程序应该显示适当的错误消息。
# 计算一组用户输入值的平均值
numbers = []  # 存储用户输入的数字

while True:
    value = float(input("请输入一个数（输入0结束）："))
    
    if value == 0:
        break  # 0 表示输入结束
    numbers.append(value)

# 检查是否输入了任何有效数字
if len(numbers) == 0:
    print("错误：没有输入任何数字。")
else:
    average = sum(numbers) / len(numbers)
    print("平均值为：", average)

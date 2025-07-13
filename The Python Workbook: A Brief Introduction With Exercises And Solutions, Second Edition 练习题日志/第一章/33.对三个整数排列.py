#创建一个程序，读取用户输入的三个整数，并按顺序（从小到大）显示它们。使用min（）和 max（）函数查找最小值和最大值。通过计算三个值的和，然后减去最小值和最大值，可以找到中间值

num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))
num3 = int(input("请输入第三个整数: "))

min_val = min(num1, num2, num3)
max_val = max(num1, num2, num3)

total_sum = num1 + num2 + num3
middle_val = total_sum - min_val - max_val

print(f"\n按照从小到大的顺序排列: {min_val}, {middle_val}, {max_val}")

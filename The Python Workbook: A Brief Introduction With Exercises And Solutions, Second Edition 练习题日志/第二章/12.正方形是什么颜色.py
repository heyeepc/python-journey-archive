# 棋盘上的位置由字母和数字来确定。字母表示列，数字表示行
# 编写一个程序，读取用户输入的位置。使用 if 语句确定列的开头是黑色方块还是白色方块。然后使用模运算来报告该行中正方形的颜色。
# 例如，如果用户输入al，那么程序应该报告正方形是黑色的。如果用户输入d5，那么程序应该报告正方形是白色的。
# 程序可能会假定用户总是输入一个有效位置。它不需要执行任何错误检查。
column = input("输入列: ")
row_str = input("输入行: ")

# 将行转换为整数
row = int(row_str)

# 将列转换为数字 (a=1, b=2, ..., h=8)
# ord() 函数可以获取字符的ASCII值。
# ord('a') 的 ASCII 值是 97。
# 列的数字 = ord(column) - ord('a') + 1
column_number = ord(column.lower()) - ord('a') + 1

# 核心逻辑：根据 (行号 + 列号) 的和的奇偶性来判断颜色
total_sum = row + column_number

# 使用模运算判断和是奇数还是偶数
if total_sum % 2 == 0:
    print("黑色")
else: # total_sum % 2 == 1
    print("白色")

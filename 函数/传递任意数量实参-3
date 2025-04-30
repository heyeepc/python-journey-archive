def add_numbers(*args):
    print("包括数字:")
    for num in args:
        print(f' {num}')

# 收集输入
numbers = []
while True:
    val = input("请输入数字（输入 q 退出）：")
    if val == "q":
        break
    if val.isdigit():  # 确保是数字
        numbers.append(int(val))
    else:
        print("请输入数字或 q")

# 调用函数
add_numbers(*numbers)

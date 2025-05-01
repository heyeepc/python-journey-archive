def sum_numbers(*args):
    print("包括数字:")
    total = 0
    for num in args:
        print(f' {num}')
        total += num
    print(f"总和为：{total}")

# 收集输入
numbers = []
while True:
    val = input("请输入数字（输入 q 退出）：")
    if val == "q":
        break
    if val.isdigit():
        numbers.append(int(val))
    else:
        print("请输入数字或 q")


sum_numbers(*numbers)  # 注意加 * 来解包列表


print("--- CIDR 前缀校验练习 ---")

# 1. 获取用户输入
first_char = input("请输入 CIDR 值的第一位数字 (0, 1, 2, 或 3): ")

# 2. 【核心代码修正】
#    使用 ord() 函数，并减去字符 '0' 的 ASCII 码，得到实际的数字值
digit_value = ord(first_char) - ord('0')

# 3. 打印转换结果
print(f"转换后的数字是：{digit_value}")

# 4. 【条件判断逻辑 - 正确】
#    使用 in 运算符进行高效判断
if digit_value in (0, 1):
    print("该前缀属于 [合法范围]。")
elif digit_value in (2, 3):
    print("该前缀属于 [需要进一步检查] 范围。")
else:
    print("该前缀属于 [超出范围]。")

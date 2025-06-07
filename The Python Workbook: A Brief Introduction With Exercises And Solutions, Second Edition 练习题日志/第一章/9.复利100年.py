# 从用户那里读取存入账户的金额
initial_amount = float(input("存入银行的金额: "))

# 年利率
annual_interest_rate = 0.04 # 4%的利率

# 设定要计算的年数
num_years = 100

# 初始化当前金额为初始金额
current_amount = initial_amount

# 使用循环计算每一年后的金额
for year in range(1, num_years + 1): # range(1, 101) 会从1循环到100
    current_amount = current_amount * (1 + annual_interest_rate)
    # 如果你想看每年的金额，可以取消下面这行的注释
    # print(f"第 {year} 年后金额: {current_amount:.2f}")

# 循环结束后，current_amount 就是100年后的金额
print(f"{num_years} 年后金额: {current_amount:.2f}")

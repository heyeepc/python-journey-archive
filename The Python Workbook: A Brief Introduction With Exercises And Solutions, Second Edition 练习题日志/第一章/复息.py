#假设你刚开了一个新的储蓄账户，每年的利息是4%。赚的利息在年底支付，然后加到储蓄账户的余额中。编写一个程序，它首先从用户那里读取存入账户的金额。
#然后，计算并显示储蓄账户在1年、2年和3年后的金额。显示每个金额，使其四舍五入到小数点后两位。
# 从用户那里读取存入账户的金额
initial_amount = float(input("存入银行的金额: ")) # 建议使用float，因为金额可能包含小数

# 年利率
annual_interest_rate = 0.04 # 4%的利率

# 计算并显示第一年后的金额
amount_after_1_year = initial_amount * (1 + annual_interest_rate)
print(f"第一年后金额: {amount_after_1_year:.2f}") # 使用.2f格式化为两位小数

# 计算并显示第二年后的金额
amount_after_2_years = amount_after_1_year * (1 + annual_interest_rate)
print(f"第二年后金额: {amount_after_2_years:.2f}")

# 计算并显示第三年后的金额
amount_after_3_years = amount_after_2_years * (1 + annual_interest_rate)
print(f"第三年后金额: {amount_after_3_years:.2f}")

#在一家特定的公司，员工业绩在每年年底都会被评估。评分表从0.0开始，较高数值表示更好的业绩，并导致更大的加薪。奖励给员工的值是0.0、0.4或0.6或更多。永远不会使用0.0和0.4之间以及0.4和 0.6之间的值。
#与每个评级相关的含义如下表所示。员工加薪的金额是2400.00美元乘以他们的评级。
#编写一个程序，从用户那里读取评级，并指出该评级的业绩是不可接受的、可接受的还是非常好的。也应该报告员工的加薪金额。如果输入了无效的评级，程序应该显示适当的错误消息。

BASE_SALARY_INCREASE = 2400.00

rating = float(input("请输入员工评级 (例如: 0.0, 0.4, 0.6 或更高): "))

if rating == 0.0:
    performance_description = "不可接受的业绩"
    # 加薪计算：2400.00 * 0.0
    salary_increase_amount = BASE_SALARY_INCREASE * rating

# 可接受的业绩 (0.4)
elif rating == 0.4:
    performance_description = "可接受的业绩"
    # 加薪计算：2400.00 * 0.4
    salary_increase_amount = BASE_SALARY_INCREASE * rating

# 非常好的业绩 (0.6 或更高)
elif rating >= 0.6:
    performance_description = "非常好的业绩"
    # 加薪计算：2400.00 * (评级)
    salary_increase_amount = BASE_SALARY_INCREASE * rating

# 3. 检查无效评级 (不符合规则的值)

# 检查 0.0 和 0.4 之间 (例如 0.1, 0.3)
elif 0.0 < rating < 0.4:
    performance_description = "无效评级：该评级值 (0.0 和 0.4 之间) 不会被使用。"
    salary_increase_amount = -1 # 用 -1 表示加薪无效

# 检查 0.4 和 0.6 之间 (例如 0.41, 0.59)
elif 0.4 < rating < 0.6:
    performance_description = "无效评级：该评级值 (0.4 和 0.6 之间) 不会被使用。"
    salary_increase_amount = -1

# 检查小于 0.0 的值
elif rating < 0.0:
    performance_description = "无效评级：评级不能是负数。"
    salary_increase_amount = -1

print(f"员工评级: {rating}")
print(f"业绩描述: {performance_description}")

if salary_increase_amount >= 0:
    # f-string 格式化输出，保留两位小数
    print(f"加薪金额: ${salary_increase_amount:.2f}")
else:
    print("加薪金额: 无法计算（评级无效）")

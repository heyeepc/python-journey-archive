#为此练习创建的程序从读取用户在餐厅订购的一顿饭的费用开始，然后程序计算这顿饭的税和小费。在计算应纳税额时使用当地税率。计算小费为餐费的18%（不含税）。
#程序的输出应该包括税的金额、小费的金额，以及包括税和小费的总餐费。格式化输出，以便所有值都使用两位小数来显示。
# input() 函数返回的是字符串，需要用 float() 转换为浮点数才能进行数学计算
Consumption_amount_str = input("输入消费金额: ")

try:
    Consumption_amount = float(Consumption_amount_str)

    # 定义当地税率。这里假设当地税率为 13%。
    # 如果当地税率有所不同，你可以在这里修改。
    local_tax_rate = 0.13

    # 计算税费：餐费 * 税率
    tax = Consumption_amount * local_tax_rate

    # 计算小费：餐费 * 18% (不含税)
    tip = Consumption_amount * 0.18

    # 计算总餐费：餐费 + 税 + 小费
    total_bill = Consumption_amount + tax + tip

    # 格式化输出所有值，保留两位小数
    # 注意：使用 :.2f 来指定保留两位小数
    print(f'税费: ${tax:.2f}')
    print(f'小费: ${tip:.2f}')
    print(f'总餐费: ${total_bill:.2f}')

except ValueError:
    print("输入无效。请输入一个有效的数字作为消费金额。")

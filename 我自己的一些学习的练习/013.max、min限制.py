#max(下限, 变量)  用于设置最小值（Floor）。
#min(上限, 变量)  用于设置最大值（Ceiling）。

MAX_DISCOUNT = 25  # 折扣上限
calculated_discount = 30 # 假设计算出来的折扣是 30

# 使用 min() 来确保折扣不超过 25
final_discount = min(MAX_DISCOUNT, calculated_discount) 

# 结果：min(25, 30) = 25
print(final_discount)

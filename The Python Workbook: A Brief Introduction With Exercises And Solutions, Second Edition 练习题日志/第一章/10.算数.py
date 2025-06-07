#创建一个程序，从用户那里读取两个整数a和b。程序应该计算和显示：
#a和b的总和
#从a中减去b的差
#a和b的乘积a除以b的商
#当a除以b时的余数
#lga的结果
#a的b次方的结果
import math # 导入 math 模块，用于数学运算，比如对数

# 从用户那里读取两个整数a和b
a = int(input("请输入第一个整数 a: "))
b = int(input("请输入第二个整数 b: "))

# 计算和显示：
# a和b的总和
sum_ab = a + b
print(f"a 和 b 的总和: {sum_ab}")

# 从a中减去b的差
difference_ab = a - b
print(f"a 减去 b 的差: {difference_ab}")

# a和b的乘积
product_ab = a * b
print(f"a 和 b 的乘积: {product_ab}")

# a除以b的商
# 注意：当b为0时，除法会报错。我们最好添加一个判断。
if b != 0:
    quotient_ab = a / b
    print(f"a 除以 b 的商: {quotient_ab}")
    # 当a除以b时的余数
    remainder_ab = a % b
    print(f"a 除以 b 时的余数: {remainder_ab}")
else:
    print("错误：除数 b 不能为零，无法计算商和余数。")

# lga的结果 (这里我们假设您想计算以10为底的对数 log10)
# 对数运算要求数字大于0。
if a > 0:
    log10_a = math.log10(a)
    print(f"log10(a) 的结果: {log10_a}")
else:
    print("错误：只有正数才能计算对数。")

# a的b次方的结果
power_ab = a ** b
print(f"a 的 b 次方的结果: {power_ab}")

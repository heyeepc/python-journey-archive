# 轮盘上有38个空格。在这些空格中，18个是黑色的，18个是红色的，2个是绿色的。绿色空格编号为0和00。
# 红色空格分别是1、3、5、7、9、12、14、16、18、19、21、23、25、27、30、32、34和 36。1到36之间的其余整数用于对黑色空格编号。

# 许多不同的赌注可放在轮盘上。本练习只考虑以下部分：单个数字（1~36、0或00）红色和黑色奇数和偶数（注意0和00不是偶数）1 to 18 19 to 36
# 编写一个程序，使用 Python的随机数生成器模拟一个旋转的轮盘赌轮。显示选中的号码和所有必须支付的赌注。例如，如果选择13，那么程序应该显示：

The spin resulted in 13...
Pay
13
Pay Black Pay Odd Pay 1 to 18

# 如果仿真结果是0或00，那么程序应该显示Pay0或 Pay 00，没有任何进一步的输出。

import random

wheel = [0, "00"] + list(range(1, 37))
random_digit = random.choice(wheel)

print(f"The spin resulted in {random_digit}...")
print("Pay")

if random_digit in [0, "00"]:
    print(f"Pay {random_digit}")
else:
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18,
                   19, 21, 23, 25, 27, 30, 32, 34, 36}

    print(f"Pay {random_digit}")

    if random_digit in red_numbers:
        print("Pay Red")
    else:
        print("Pay Black")

    if random_digit % 2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")

    if 1 <= random_digit <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

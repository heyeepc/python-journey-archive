#写一个计算二次函数实根的程序。程序应该先提示用户输入a、b和c的值。然后它应该显示一条消息，指示实根的数量，以及实根的值（如果有）。
import math

# 提示用户输入a, b, c的值
print("请为二次方程 ax^2 + bx + c = 0 输入系数。")
# 建议使用 float() 来允许小数输入，以适应更广泛的二次方程
try:
    a = float(input("输入数字 a: "))
    b = float(input("输入数字 b: "))
    c = float(input("输入数字 c: "))
except ValueError:
    print("输入无效。请确保输入的是数字。")
    exit() # 遇到非数字输入时退出程序

# 首先检查 a 是否为 0，如果 a=0，则不是二次方程
if a == 0:
    if b == 0:
        if c == 0:
            print("这不是一个二次方程，它是 0 = 0，有无限个解。")
        else:
            print("这不是一个二次方程，它是常数方程，没有解。")
    else:
        # 这是一个线性方程 bx + c = 0
        x = -c / b
        print("这是一个线性方程（a=0）。有一个实根：")
        print(f"实根的值为: {x}")
else:
    # 计算判别式 (b^2 - 4ac)
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        # 情况一：判别式小于 0，没有实数根
        print(f"对于方程 {a}x^2 + {b}x + {c} = 0:")
        print("实根数量: 0")
        print("没有实数根。")

    elif delta == 0:
        # 情况二：判别式等于 0，有两个相等的实数根
        # x = -b / (2a)
        # 确保分母 2*a 被视为一个整体
        root = -b / (2 * a)
        print(f"对于方程 {a}x^2 + {b}x + {c} = 0:")
        print("实根数量: 1 (两个相等的实根)")
        print(f"实根的值为: {root}")

    else: # delta > 0
        # 情况三：判别式大于 0，有两个不相等的实数根
        # 使用 math.sqrt() 来计算平方根
        sqrt_delta = math.sqrt(delta)
        
        # 确保分母 2*a 被视为一个整体
        root_1 = (-b + sqrt_delta) / (2 * a)
        root_2 = (-b - sqrt_delta) / (2 * a)

        print(f"对于方程 {a}x^2 + {b}x + {c} = 0:")
        print("实根数量: 2")
        print(f"两个不相等的实根是: {root_1} 和 {root_2}")

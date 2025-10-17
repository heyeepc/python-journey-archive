import math

# 1. 定义函数：负责计算逻辑
def solve_quadratic_equation(a, b, c):
    """
    计算二次方程 ax^2 + bx + c = 0 的实数根。
    它会打印实根的数量和相应的值（如果有）。
    """
    
    # 检查 a 是否为 0（线性方程或更简单的情况）
    if a == 0:
        if b == 0:
            if c == 0:
                print("【结果】这不是一个二次方程，它是 0 = 0，有无限个解。")
            else:
                print("【结果】这不是一个二次方程，它是常数方程，没有解。")
        else:
            # 线性方程：bx + c = 0
            x = -c / b
            print(f"【结果】这是一个线性方程（a=0）。有一个实根: {x}")
        return # 结束函数执行

    # 2. 计算判别式 (Delta)
    delta = (b**2) - (4 * a * c)

    print(f"\n--- 计算方程 {a}x^2 + {b}x + {c} = 0 ---")

    if delta < 0:
        # 情况一：没有实数根
        print("【结果】实根数量: 0")
        print("【结果】没有实数根。")

    elif delta == 0:
        # 情况二：有一个实根（两个相等的实根）
        root = -b / (2 * a)
        print("【结果】实根数量: 1 (两个相等的实根)")
        print(f"【结果】实根的值为: {root}")

    else: # delta > 0
        # 情况三：有两个不相等的实根
        sqrt_delta = math.sqrt(delta)
        
        # 使用求根公式，注意分母 (2 * a) 的括号
        root_1 = (-b + sqrt_delta) / (2 * a)
        root_2 = (-b - sqrt_delta) / (2 * a)

        print("【结果】实根数量: 2")
        print(f"【结果】两个不相等的实根是: {root_1} 和 {root_2}")


# 3. 主程序入口：负责用户交互和调用函数
def main():
    print(">> 二次方程实根计算器 <<")
    print("请为二次方程 ax^2 + bx + c = 0 输入系数。")
    
    # 集中处理用户输入
    try:
        # 允许用户输入浮点数（小数）
        a = float(input("输入数字 a: "))
        b = float(input("输入数字 b: "))
        c = float(input("输入数字 c: "))
    except ValueError:
        print("错误：输入无效。请确保输入的是数字。")
        return # 输入错误时退出主程序

    # 调用上面定义的函数进行计算
    solve_quadratic_equation(a, b, c)

# 4. 推荐的最佳实践：使用 if __name__ == "__main__":
# 这确保了只有当你直接运行这个文件时 (而不是作为模块导入时)，main() 函数才会被执行。
if __name__ == "__main__":
    main()

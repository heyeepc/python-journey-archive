#一个在线零售商销售两种产品：widget 和 gizmo。每个 widget重75克，每个gizmo重112克。编写一个程序，从用户那里读取 widget的数量和 gizmo的数量。然后程序应该计算和显示产品的总重量。
# 定义每种产品的重量（常量，方便修改和阅读）
WIDGET_WEIGHT = 75  # 克
GIZMO_WEIGHT = 112  # 克

while True:
    try:
        # 获取 widget 的数量
        num_widgets_str = input("请输入 widget 的数量：")
        num_widgets = int(num_widgets_str)

        # 获取 gizmo 的数量
        num_gizmos_str = input("请输入 gizmo 的数量：")
        num_gizmos = int(num_gizmos_str)

        # 确保输入的是非负整数
        if num_widgets < 0 or num_gizmos < 0:
            print("输入错误：数量不能是负数，请输入非负整数。")
            continue # 继续循环，让用户重新输入
        else:
            # 计算总重量
            # total_weight = (widget 数量 * widget 重量) + (gizmo 数量 * gizmo 重量)
            total_weight = (num_widgets * WIDGET_WEIGHT) + \
                           (num_gizmos * GIZMO_WEIGHT)

            # 显示总重量
            # 使用 f-string 格式化输出，明确告诉用户计算的是什么
            print(f"产品的总重量是：{total_weight} 克")
            break # 计算并显示结果后，退出循环

    except ValueError:
        # 捕获当用户输入非整数时的错误
        print("输入错误：请输入一个有效的整数作为数量。")
    except Exception as e:
        # 捕获其他未知错误
        print(f"发生了一个意外错误：{e}")

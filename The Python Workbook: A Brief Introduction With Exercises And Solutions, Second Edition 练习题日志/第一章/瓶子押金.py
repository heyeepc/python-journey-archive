#在许多司法管辖区，会在饮料瓶中加入小额押金，以鼓励人们对其进行回收利用。在一个特定的司法管辖区，装一升或以下饮料的容器有10美分的押金，装一升以上饮料的容器有25美分的押金。编写一个程序，从用户那里读取每种饮料瓶的数量。
#程序应该继续计算和显示将收到的退还饮料瓶的退款。格式化输出，使其包含美元符号，并保留两位小数。
def calculate_refund():
    
    deposit_large_bottle = 0.25  # 1升或以上饮料瓶的押金（美元）
    deposit_small_bottle = 0.10  # 1升以下饮料瓶的押金（美元）

    total_refund = 0.0  # 初始化总退款金额

    print("欢迎使用饮料瓶退款计算器！")
    print("请输入每种饮料瓶的数量。")
    print("输入 '大' 或 '小' 来选择瓶子类型，然后输入数量。")
    print("输入任何非数字内容（如 '结束'）来停止输入并查看总退款。")
    print("-" * 30) # 打印一条分隔线

    while True: # 无限循环，直到用户选择停止
        bottle_type_input = input("请输入瓶子类型（大/小）或输入 '结束' 退出：").strip().lower()

        if bottle_type_input == '结束':
            break # 如果用户输入 '结束'，跳出循环

        if bottle_type_input not in ['大', '小']:
            print("输入无效！请选择 '大' 或 '小'。")
            continue # 继续下一次循环，重新让用户输入

        try:
            # 尝试获取数量
            quantity_input = input(f"请输入 {bottle_type_input} 瓶子的数量：")
            quantity = int(quantity_input) # 将输入的数量转换为整数

            if quantity < 0:
                print("数量不能为负数，请重新输入。")
                continue

            if bottle_type_input == '大':
                total_refund += quantity * deposit_large_bottle
                print(f"已添加 {quantity} 个大瓶子。当前总退款：${total_refund:.2f}")
            elif bottle_type_input == '小':
                total_refund += quantity * deposit_small_bottle
                print(f"已添加 {quantity} 个小瓶子。当前总退款：${total_refund:.2f}")

        except ValueError:
            # 如果用户输入的数量不是有效的整数，捕获错误
            print("数量输入无效！请输入一个整数。")
            # 不跳出循环，让用户重新输入有效的数量
            continue

    print("-" * 30)
    # 格式化输出总退款金额，保留两位小数并添加美元符号
    print(f"您将收到的退款总额为：${total_refund:.2f}")
    print("感谢使用！")

# 运行程序
calculate_refund()

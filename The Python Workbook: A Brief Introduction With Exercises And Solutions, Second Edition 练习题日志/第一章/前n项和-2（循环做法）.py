while True:
    try:
        n_str = input("请输入一个正整数n：")
        n = int(n_str)

        if n <= 0:
            print("输入错误：请输入一个大于0的正整数。")
        else:
            # 初始化一个变量来存储总和
            total_sum = 0

            # 使用 for 循环从 1 遍历到 n
            # range(1, n + 1) 会生成一个序列：1, 2, ..., n
            for i in range(1, n + 1):
                total_sum = total_sum + i # 或者简写为 total_sum += i
                # print(f"当前数字: {i}, 累加和: {total_sum}") # 可以取消注释这行，看看每次循环的变化

            print(f"使用循环，从1到{n}的所有整数的和是：{total_sum}")
            break
    except ValueError:
        print("输入错误：请输入一个有效的整数。")
    except Exception as e:
        print(f"发生了一个意外错误：{e}")

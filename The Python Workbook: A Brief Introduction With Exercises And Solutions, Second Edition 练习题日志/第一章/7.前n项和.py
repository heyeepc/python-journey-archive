#编写一个程序，从用户那里读取一个正整数n，然后显示从1到n的所有整数的和.
while True:
    try:
        n_str = input("请输入一个正整数n：")
        n = int(n_str)

        # 检查输入的数是否为正整数
        if n <= 0:
            print("输入错误：请输入一个大于0的正整数。")
        else:
            # 使用高斯求和公式计算从1到n的和
            he = n * (n + 1) / 2

            # 打印结果
            # f-string 是一种方便的字符串格式化方式，可以把变量直接嵌入到字符串中
            print(f"从1到{n}的所有整数的和是：{int(he)}") # 将he转换为整数，因为和通常是整数
            break # 如果输入正确并计算完成，退出循环
    except ValueError:
        # 如果用户输入的内容不能转换为整数（比如输入了字母），会捕获 ValueError 错误
        print("输入错误：请输入一个有效的整数。")
    except Exception as e:
        # 捕获其他可能的错误
        print(f"发生了一个意外错误：{e}")

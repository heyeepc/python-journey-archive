def check_even(number):  # 函数定义时要有参数 number
    if number % 2 == 0:
        print("是偶数")
        return True       # 返回 True 表示是偶数
    else:
        print("是奇数")
        return False      # 返回 False 表示是奇数

a = int(input("请输入数字："))
b = check_even(a)        # 调用函数，传入变量 a
print("结果：", b)        # 打印返回的布尔值结果

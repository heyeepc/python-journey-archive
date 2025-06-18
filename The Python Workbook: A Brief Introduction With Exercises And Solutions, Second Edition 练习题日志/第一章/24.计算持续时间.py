#创建一个程序，将用户的持续时间读取为天数、小时、分钟和秒。计算并显示此持续时间所表示的总秒数。
while True:
        try:
            # 1. 获取天数
            days_str = input("请输入天数：")
            days = int(days_str)

            # 2. 获取小时数
            hours_str = input("请输入小时数：")
            hours = int(hours_str)

            # 3. 获取分钟数
            minutes_str = input("请输入分钟数：")
            minutes = int(minutes_str)

            # 4. 获取秒数
            seconds_str = input("请输入秒数：")
            seconds = int(seconds_str)

           
            if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
                print("输入错误：所有时间单位（天、小时、分钟、秒）都不能是负数。请重新输入。")
                continue # 继续循环，让用户重新输入


            total_seconds = (days * 24 * 60 * 60) + \
                            (hours * 60 * 60) + \
                            (minutes * 60) + \
                            seconds

            # 5. 显示结果
            print(f"\n输入的持续时间共计：{total_seconds} 秒。")
            break # 计算成功，退出循环
        except ValueError:
            # 捕获当用户输入非整数时的错误
            print("输入错误：请输入有效的整数。请重新输入。")

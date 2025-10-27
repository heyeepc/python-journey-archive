#该程序读取用户输入的年份，并报告该年份的1月1日是星期几。程序的输出应该包括星期几的全名，而不只是公式返回的整数。
import datetime

def find_jan_first_day():
    # 1. 提示用户输入年份
    while True:
        try:
            year_input = input("请输入您想查询的年份 (例如: 2025): ")
            year = int(year_input)
            # 简单检查年份是否合理
            if year < 1 or year > 9999:
                print("输入的年份不合理，请重新输入。")
                continue
            break # 输入有效，跳出循环
        except ValueError:
            print("输入无效，请输入一个整数年份。")

    # 2. 创建表示该年份1月1日的 datetime 对象
    # datetime(year, month, day)
    date_to_check = datetime.date(year, 1, 1)

    # 3. 获取星期几的整数表示
    # weekday() 方法返回 0（周一）到 6（周日）
    day_index = date_to_check.weekday()

    # 4. 定义星期几的完整名称列表 (从周一开始)
    # 因为您希望输出全名，并且您是中文用户
    week_days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    # 5. 根据索引获取全名
    day_name = week_days[day_index]

    # 6. 输出结果
    print(f"\n查询结果:")
    print(f"{year} 年的 1 月 1 日是: {day_name}")


# 运行函数
find_jan_first_day()

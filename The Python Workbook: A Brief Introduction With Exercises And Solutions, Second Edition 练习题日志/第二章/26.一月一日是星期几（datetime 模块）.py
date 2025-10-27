#该程序读取用户输入的年份，并报告该年份的1月1日是星期几。程序的输出应该包括星期几的全名，而不只是公式返回的整数。
import datetime

year = int(input("请输入年份："))
day = datetime.date(year, 1, 1).strftime("%A")
print(f"{year}年1月1日是{day}")

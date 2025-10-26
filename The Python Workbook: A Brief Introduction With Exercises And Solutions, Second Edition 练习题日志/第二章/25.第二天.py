#编写一个程序，从用户那里读取数据，并计算它的直接后续数据。例如，如果用户输入代表2019-11-18的值，那么程序应该显示一条消息，指示在2019-11-18之后的那一天是2019-11-19。
#如果用户输入的值代表2019-11-30，则程序应指示第二天是2019-12-01。如果用户输入代表2019-12-31的值，则程序应指示第二天是2020-01-01。
#日期将以数字形式输入，有三个单独的输入语句；分别输入年份、月份和日期。确保程序在闰年工作正常。
# 定义闰年判断函数 
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# --- 用户输入部分 ---
try:
    current_year = int(input("输入年份: "))
    current_month = int(input("输入月份 (1-12): "))
    current_day = int(input("输入日期: "))
except ValueError:
    print("输入无效。请输入整数作为年份、月份和日期。")
    # 退出程序，避免计算错误
    exit() 

# --- 初始化下一天的日期 ---
next_year = current_year
next_month = current_month
next_day = current_day + 1 # 默认情况下，日期加 1

# --- 确定当前月份的最大天数 ---

# 集合 {1, 3, 5, 7, 8, 10, 12} 都是 31 天
if current_month in {1, 3, 5, 7, 8, 10, 12}:
    days_in_month = 31
    
# 集合 {4, 6, 9, 11} 都是 30 天
elif current_month in {4, 6, 9, 11}:
    days_in_month = 30
    
# 特殊情况：二月 (2)
elif current_month == 2:
    if is_leap_year(current_year):
        days_in_month = 29  # 闰年 29 天
    else:
        days_in_month = 28  # 平年 28 天
        
# 检查输入的月份是否有效
else:
    print("月份输入错误。请输入 1 到 12 之间的数字。")
    exit()

# 额外的日期有效性检查
if current_day < 1 or current_day > days_in_month:
    print(f"日期输入错误。{current_year} 年 {current_month} 月只有 {days_in_month} 天。")
    exit()

# --- 日期进位逻辑 (核心部分) ---

# 情况 A: 日期没有达到当月最大天数，直接 +1
if current_day < days_in_month:
    # 默认的 next_day 已经设置为 current_day + 1，无需修改
    pass 
    
# 情况 B: 日期是当月最后一天，需要月份进位
elif current_day == days_in_month:
    
    next_day = 1              # 日期重置为 1 号
    next_month = current_month + 1 # 月份进位

    # 情况 B.1: 月份没有达到 12 月，只需月份进位
    if current_month < 12:
        # next_month 已经是 current_month + 1
        pass
        
    # 情况 B.2: 年末进位 (12月 31日)，需要年份进位
    elif current_month == 12:
        next_month = 1         # 月份重置为 1 月
        next_year = current_year + 1 # 年份进位
        
# --- 输出结果 ---

print("-" * 30)
print(f"当前日期: {current_year}-{current_month:02d}-{current_day:02d}")
print(f"直接后继: {next_year}-{next_month:02d}-{next_day:02d}")
print("-" * 30)

# 示例测试
# 2019-11-18 -> 2019-11-19
# 2019-11-30 -> 2019-12-01 (30天月进位)
# 2019-12-31 -> 2020-01-01 (年末进位)
# 2020-02-29 -> 2020-03-01 (闰年2月进位)
# 2023-02-28 -> 2023-03-01 (平年2月进位)

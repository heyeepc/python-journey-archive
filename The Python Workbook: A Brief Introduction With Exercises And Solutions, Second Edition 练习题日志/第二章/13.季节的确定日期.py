#一年分为四季：春、夏、秋、冬。虽然由于年历的构造方式不同，季节变化的确切日期每年略有不同，但本练习使用以下日期。
#创建一个程序，读取用户输入的月份和日期。用户以字符串形式输入月份的名称，然后以整数形式输入月份中的日期。此后，程序应该显示与输入日期相关的季节。
month_name = input("请输入月份的名称（例如：3月）: ")
date = int(input("请输入月份中的日期（例如：15）: "))

season = ""


# 1. 判断春季：(3月20日及以后) 或 (4月、5月) 或 (6月19日及以前)
if month_name == "3月":
    if date >= 20:
        season = "春季"
    else:
        season = "冬季" # 3月1日-19日属于冬季
elif month_name in ["4月", "5月"]:
    season = "春季"
elif month_name == "6月":
    if date < 20:
        season = "春季" # 6月1日-19日属于春季
    else:
        season = "夏季" # 6月20日及以后属于夏季

# 2. 判断夏季：(6月20日及以后) 或 (7月、8月) 或 (9月19日及以前)
elif month_name in ["7月", "8月"]:
    season = "夏季"
elif month_name == "9月":
    if date < 20:
        season = "夏季" # 9月1日-19日属于夏季
    else:
        season = "秋季" # 9月20日及以后属于秋季

# 3. 判断秋季：(9月20日及以后) 或 (10月、11月) 或 (12月19日及以前)
elif month_name in ["10月", "11月"]:
    season = "秋季"
elif month_name == "12月":
    if date < 20:
        season = "秋季" # 12月1日-19日属于秋季
    else:
        season = "冬季" # 12月20日及以后属于冬季

# 4. 判断冬季：(12月20日及以后) 或 (1月、2月) 或 (3月19日及以前)
elif month_name in ["1月", "2月"]:
    season = "冬季"
# 3月已经处理过了，在elif month_name == "3月": 中
# 12月也已经处理过了，在elif month_name == "12月": 中

# 最后的输出
if season: # 确保 season 变量已经被设置
    print(f"你输入的日期 {month_name}{date} 属于 {season}。")
else:
    print("输入的月份名称不正确或日期不合理。")

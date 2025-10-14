# 中国的十二生肖以12年为一个周期。下表显示了一个12年的周期。2012年是龙年，1999年是兔年
# 编写一个程序，读取用户输入的年份，并显示与那年相关的生肖。程序应该在大于或等于0的任何年份都能正常工作，而不仅是表中列出的年份。
years = abs(int(input("请输入年份(大于公元): ")))

Loong_Year = 2000

# 计算与基准年(2000)的差值对 12 取模的结果
# 结果 0 代表 2000 年，即龙年
years_a = (years - Loong_Year) % 12

# 使用 if/elif 结构完成全部 12 种情况
if years_a == 0:
    print("龙年")
elif years_a == 1:
    print("蛇年")
elif years_a == 2:
    print("马年")
elif years_a == 3:
    print("羊年")
elif years_a == 4:
    print("猴年")
elif years_a == 5:
    print("鸡年")
elif years_a == 6:
    print("狗年")
elif years_a == 7:
    print("猪年")
elif years_a == 8:
    print("鼠年")
elif years_a == 9:
    print("牛年")
elif years_a == 10:
    print("虎年")
elif years_a == 11:
    print("兔年")

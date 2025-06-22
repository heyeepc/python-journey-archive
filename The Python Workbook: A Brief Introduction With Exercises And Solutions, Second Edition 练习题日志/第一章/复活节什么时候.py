#复活节是春分后第一个月圆后的那个星期天。因为复活节的日期包含了月亮的成分，所以在公历中没有固定的日期。相反，它可以在3月22日和4月25日之间的任何日期。
#可以使用Anonymous Gregorian Computus 算法计算给定年份的复活节的月份和日期，如下所示。
year = int(input("输入年份"))

a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451

month_num = (h + l - 7 * m + 114) // 31
day_num = (h + l - 7 * m + 114) % 31 + 1

print(f"\n{year} 年的复活节日期是：{month_num}月{day_num} 日")

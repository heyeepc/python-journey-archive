year = int(input("请输入年份："))
m = 13  # 1月按上一年的13月处理
y = year - 1
q = 1   # 日期是1号
K = y % 100
J = y // 100
h = (q + 13*(m+1)//5 + K + K//4 + J//4 + 5*J) % 7
# h=0是Saturday
day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"{year}年1月1日是{day_names[h]}")

from datetime import datetime

zodiac_dates = [
    ((1, 20), (2, 18), "水瓶座"),
    ((2, 19), (3, 20), "双鱼座"),
    ((3, 21), (4, 19), "白羊座"),
    ((4, 20), (5, 20), "金牛座"),
    ((5, 21), (6, 21), "双子座"),
    ((6, 22), (7, 22), "巨蟹座"),
    ((7, 23), (8, 22), "狮子座"),
    ((8, 23), (9, 22), "处女座"),
    ((9, 23), (10, 23), "天秤座"),
    ((10, 24), (11, 22), "天蝎座"),
    ((11, 23), (12, 21), "射手座"),
    ((12, 22), (1, 19), "摩羯座"),
]

month = int(input("请输入出生月份："))
day = int(input("请输入出生日期："))
date = datetime(2024, month, day)  # 任意平年即可

for (start_m, start_d), (end_m, end_d), sign in zodiac_dates:
    start = datetime(2024, start_m, start_d)
    end = datetime(2024, end_m, end_d)
    if start <= date <= end or (start_m > end_m and (date >= start or date <= end)):
        print(f"你的星座是：{sign}")
        break

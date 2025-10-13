#编写一个程序，要求用户输入其出生日期和月份。然后，程序应该报告用户的星座，作为适当的输出消息的一部分。

from datetime import datetime


def find_zodiac_sign():
    # 你的方案：转化为一年中的第几天来判断区间

    while True:
        try:
            # 提示用户输入，并把输入转换为整数
            month = int(input("请输入您的出生月份（1-12）："))
            day = int(input("请输入您的出生日期（1-31）："))

            # 检查月份和日期的基本有效性
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
            else:
                print("输入的月份或日期无效，请重新输入。")
        except ValueError:
            print("输入必须是数字，请重新输入。")


    try:
        date_of_birth = datetime(2001, month, day)
    except ValueError:
        # 处理某些日期组合（如2月30日）的无效性
        print(f"无效的日期组合：{month}月{day}日。请确保输入正确的日期。")
        return

    # 获取日期是一年中的第几天 (1 到 365)
    day_number = date_of_birth.timetuple().tm_yday


    zodiac_signs = [
        (20, "水瓶座 (Aquarius)"),  # 1月20日 (第20天)
        (50, "双鱼座 (Pisces)"),  # 2月19日 (第50天)
        (80, "白羊座 (Aries)"),  # 3月21日 (第80天)
        (111, "金牛座 (Taurus)"),  # 4月21日 (第111天)
        (142, "双子座 (Gemini)"),  # 5月21日 (第142天)
        (173, "巨蟹座 (Cancer)"),  # 6月21日 (第173天)
        (204, "狮子座 (Leo)"),  # 7月23日 (第204天)
        (236, "处女座 (Virgo)"),  # 8月23日 (第236天)
        (266, "天秤座 (Libra)"),  # 9月23日 (第266天)
        (296, "天蝎座 (Scorpio)"),  # 10月23日 (第296天)
        (326, "射手座 (Sagittarius)"),  # 11月22日 (第326天)
        (356, "摩羯座 (Capricorn)")  # 12月22日 (第356天)
    ]


    if day_number >= 356:
        result_sign = "摩羯座 (Capricorn)"

    else:


        result_sign = ""
        for start_day, sign_name in reversed(zodiac_signs):
            if day_number >= start_day:
                result_sign = sign_name
                break

        if not result_sign:
            result_sign = "摩羯座 (Capricorn)"

    # 步骤4: 输出结果
    print("-" * 30)
    print(f"您的生日是 {month}月{day}日。")
    print(f"您是 {result_sign}！")
    print("-" * 30)

# 运行程序
find_zodiac_sign()

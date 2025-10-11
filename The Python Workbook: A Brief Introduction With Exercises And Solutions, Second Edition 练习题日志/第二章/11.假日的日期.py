#编写一个程序，读取用户输入的月份和日期。如果月份和日期与前面列出的假日之一匹配，那么程序应该显示假日的名称。
#否则，程序应指示输入的月份和日期不对应于固定日期的假日。
# 定义假日字典，键是“月日”格式的字符串，值是假日名称
Holiday = {
    "1月1日": "元旦",
    "7月1日": "加拿大国庆",
    "12月25日": "圣诞节",
}

# 提示用户输入日期
# 我们使用一个简单的 try-except 来捕获潜在的 I/O 错误，尽管对于简单输入不常用
try:
    # 读取用户输入的月份和日期，例如 "1月1日"
    Date = input("请输入日期（格式如 '1月1日'）：")

    # 尝试在 Holiday 字典中查找输入的日期
    # .get() 方法：如果找到键 Date，则返回对应的值；否则返回 None
    holiday_name = Holiday.get(Date)

    # 进行条件判断
    if holiday_name:
        # 如果 holiday_name 不为 None (即找到了假日)
        print(f"匹配成功：{Date} 是 {holiday_name}")
    else:
        # 如果 holiday_name 为 None (即未找到假日)
        print(f"未找到：输入的日期 {Date} 不对应于固定日期的假日。")

except Exception as e:
    # 捕获其他可能的运行时错误
    print(f"发生错误：{e}")
    print("程序未能正常执行。")

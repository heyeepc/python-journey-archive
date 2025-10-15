# 编写一个程序，从用户那里读取震级，并显示适当的描述符，作为有意义的消息的一部分。例如，如果用户输入5.5，程序应该表明，5.5级被认为是中度地震。

# 注意：最大震级使用 None 表示没有上限（例如 10.0 或更多）
MAGNITUDE_LEVELS = [
    # 特殊情况：小于 2.0
    (0.0, 2.0, "超微"),  # 假设从 0.0 开始

    # 左闭右开区间 [min, max)
    (2.0, 3.0, "甚微"),
    (3.0, 4.0, "微小"),
    (4.0, 5.0, "弱"),
    (5.0, 6.0, "中"),
    (6.0, 7.0, "强"),
    (7.0, 8.0, "甚强"),

    # 极强：9.0 到 10（不含）
    (9.0, 10.0, "极强"),

    # 超强：10 或更多
    (10.0, None, "超强"),
]

magnitude_input = input("请输入地震震级（例如：5.5）：")

magnitude = float(magnitude_input)

descriptor = "未知震级"

for min_mag, max_mag, level in MAGNITUDE_LEVELS:
    if max_mag is not None and min_mag <= magnitude < max_mag:
        descriptor = level
        break
    elif max_mag is None and magnitude >= min_mag:
        descriptor = level
        break

print(f"震级 {magnitude} 被认为是【{descriptor}】地震。")

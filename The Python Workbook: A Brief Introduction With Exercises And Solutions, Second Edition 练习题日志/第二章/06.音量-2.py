# 1. 使用字典存储数据
NOISE_LEVELS = {
    130: "手提钻",
    106: "割草机",
    70: "闹钟",
    40: "安静房间"
}

# 2. 从用户获取输入
try:
    noise_input = int(input("请输入噪音分贝: "))
except ValueError:
    print("输入无效，请输入一个整数。")
    # 可以在这里退出程序或者做其他处理
    exit()

# 3. 检查精确匹配
if noise_input in NOISE_LEVELS:
    # 如果用户输入的值在字典的“键”中，就找到了
    print(f"{noise_input} dB: {NOISE_LEVELS[noise_input]}")
else:
    # 否则，处理介于两者之间或超出范围的情况
    
    # 找出所有分贝值并排序
    sorted_levels = sorted(NOISE_LEVELS.keys(), reverse=True)
    
    found_range = False
    
    # 从最吵的开始向下遍历
    for i in range(len(sorted_levels) - 1):
        upper = sorted_levels[i]    # 较高的分贝值 (如 130)
        lower = sorted_levels[i+1]  # 较低的分贝值 (如 106)
        
        # 检查是否在两个已知值之间
        if lower < noise_input < upper:
            upper_name = NOISE_LEVELS[upper]
            lower_name = NOISE_LEVELS[lower]
            print(f"该值 {noise_input} dB 介于 {upper_name} ({upper} dB) 和 {lower_name} ({lower} dB) 之间。")
            found_range = True
            break # 找到后就退出循环

    # 如果没有找到范围，说明它在最安静之下或最吵闹之上
    if not found_range:
        max_noise = sorted_levels[0]   # 130
        min_noise = sorted_levels[-1]  # 40
        
        if noise_input > max_noise:
            print(f"该值 {noise_input} dB 大于表中最嘈杂的噪声，高于 {NOISE_LEVELS[max_noise]} ({max_noise} dB)。")
        elif noise_input < min_noise:
            print(f"该值 {noise_input} dB 小于表中最安静的噪声，低于 {NOISE_LEVELS[min_noise]} ({min_noise} dB)。")

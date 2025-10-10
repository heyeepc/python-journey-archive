#在前一个问题中，将一个音符的名称转换为它的频率。在这个问题中，你要写一个程序来逆转这个过程。首先读取用户输入的频率。如果频率在上题表中列出的值的1Hz内，那么报告相应的音符名称。否则报告的频率不对应已知的音符。
#在这个练习中，只需要考虑表中列出的音符。不需要考虑其他八度音阶的音符。
# C4音阶的基准频率（与上题相同）
Note_Frequency = {
    "c": 261.63,
    "d": 293.66,
    "e": 329.63,
    "f": 349.23,
    "g": 392.00,
    "a": 440.00,
    "b": 493.88,
}

# 1. 获取用户输入
try:
    # 接收用户输入的频率，并转换为浮点数
    user_frequency = float(input("请输入一个频率（Hz）："))
except ValueError:
    # 处理输入不是有效数字的情况
    print("输入无效。请输入一个有效的数字频率。")
    # 退出程序或重新开始
    exit()

# 2. 初始化查找标志
found_note = None

# 3. 遍历字典，进行查找和比较
# .items() 方法允许我们同时获取键（note）和值（base_freq）
for note, base_freq in Note_Frequency.items():
    
    # 计算误差范围：检查用户频率是否在 [base_freq - 1, base_freq + 1] 范围内
    # abs(user_frequency - base_freq) <= 1.0 是检查误差的常用且简洁的方式
    if abs(user_frequency - base_freq) <= 1.0:
        
        # 找到音符
        found_note = note
        # 一旦找到，就退出循环，提高效率
        break

# 4. 输出结果
if found_note:
    # 将找到的音符转换为大写并显示为 C4, D4 等（因为我们只考虑了4八度）
    print(f"频率 {user_frequency:.2f} Hz 对应于音符 {found_note.upper()}4。")
else:
    print(f"频率 {user_frequency:.2f} Hz 不对应于任何已知的音符（在 ±1Hz 范围内）。")

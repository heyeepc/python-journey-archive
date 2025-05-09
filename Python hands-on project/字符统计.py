a = input("请输入：")

english_count = 0
chinese_count = 0
symbol_count = 0

for char in a:
    if 'a' <= char.lower() <= 'z':  # 英文字母
        english_count += 1
    elif '\u4e00' <= char <= '\u9fff':  # 常见中文范围
        chinese_count += 1
    elif not char.isalnum():  # 不是字母或数字就是符号（粗略方式）
        symbol_count += 1

print("英文字符数：", english_count)
print("中文字符数：", chinese_count)
print("符号字符数：", symbol_count)

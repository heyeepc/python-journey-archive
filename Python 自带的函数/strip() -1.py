text3 = "---Hello---"
stripped_text3 = text3.strip("-")
print(f"原字符串: '{text3}'")
print(f"处理后: '{stripped_text3}'")

text4 = "ababaHelloababa"
stripped_text4 = text4.strip("ab") # 移除 'a' 和 'b'
print(f"原字符串: '{text4}'")
print(f"处理后: '{stripped_text4}'")

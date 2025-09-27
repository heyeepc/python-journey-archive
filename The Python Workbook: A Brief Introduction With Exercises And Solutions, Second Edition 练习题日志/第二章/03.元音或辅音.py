# 本练习将创建一个从用户那里读取字母的程序。
# 如果用户输入a、e、i、o或u，那么程序应该显示一条消息，指示输入的字母是元音。
# 如果用户输入y，程序应该显示一条消息，指示有时y是元音，有时y是辅音。否则，程序应该显示一条消息，指示字母是辅音字母。
Letter = input("请输入一个字母: ")

# 将输入转换为小写，这样无论用户输入 'A' 还是 'a' 都能正确判断
# 这样做可以让程序更健壮
Letter_lower = Letter.lower()

# 定义元音集合
vowels = ('a', 'e', 'i', 'o', 'u')

# 使用 'in' 运算符检查是否是元音
if Letter_lower in vowels:
    print(f"'{Letter}' 是元音。")

# 检查是否是 'y'
elif Letter_lower == 'y':
    print(f"'{Letter}'：有时是元音，有时是辅音。")

# 其他情况都是辅音
else:
    print(f"'{Letter}' 是辅音字母。")

print("程序结束。")

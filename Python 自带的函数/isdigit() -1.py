str1 = "12345"
print(str1.isdigit())  # 输出: True

str2 = "123a45"
print(str2.isdigit())  # 输出: False (包含字母 'a')

str3 = "12 345"
print(str3.isdigit())  # 输出: False (包含空格)

str4 = "123.45"
print(str4.isdigit())  # 输出: False (包含小数点 '.')

str5 = "-123"
print(str5.isdigit())  # 输出: False (包含负号 '-')

str6 = ""
print(str6.isdigit())  # 输出: False (空字符串)


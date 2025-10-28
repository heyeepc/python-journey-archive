#在一个特定的司法管辖区，旧的车牌由三个大写字母和三个数字组成。当使用所有遵循该模式的牌照后，格式更改为四个数字后面跟着三个大写字母。
#编写一个程序，首先读取用户输入的字符串。然后，程序应该显示一条消息，指示这些字符是对旧样式的车牌有效还是对新样式的车牌有效。如果用户输入的字符串对两种样式的车牌都是无效的，程序就应该显示一个适当的消息。
plate = input("输入车牌号: ").strip()

if len(plate) == 6:
    letters = plate[:3]
    digits = plate[3:]
    if letters.isalpha() and letters.isupper() and digits.isdigit():
        print("是旧车牌")
    else:
        print("不符合规矩的车牌")
elif len(plate) == 7:
    digits = plate[:4]
    letters = plate[4:]
    if digits.isdigit() and letters.isalpha() and letters.isupper():
        print("是新车牌")
    else:
        print("不符合规矩的车牌")
else:
    print("不符合规矩的车牌")

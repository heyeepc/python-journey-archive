#编写一个程序，从用户那里读取一个声音的分贝级别。如果用户输入的分贝级别与表中的噪声之一匹配，则程序应该显示只包含该噪声的消息。如果用户输入的若干分贝在列出的噪声之间，则程序应显示一条消息，指示该值位于哪两个噪声之间。
#确保程序还生成了合理的输出，其值小于表中最安静的噪声，而大于表中最嘈杂的噪声
Noise = int(input("请输入噪音分贝"))
if Noise > 130:
    print("手提钻之上")
elif Noise == 130:
    print("手提钻")
elif 130 > Noise > 106:
    print("手提钻和割草机之间")
elif Noise == 106:
    print("割草机")
elif 106 > Noise >70:
    print("割草机和闹钟之间")
elif Noise == 70:
    print("闹钟")
elif 70 > Noise > 40:
    print("闹钟和安静房间之间")
elif Noise == 40:
    print("安静房间")
elif Noise < 40:
    print("安静房间之下")

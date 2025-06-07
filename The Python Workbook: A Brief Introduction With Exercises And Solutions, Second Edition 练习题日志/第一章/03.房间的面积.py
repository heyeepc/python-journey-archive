#编写一个程序，要求用户输入房间的宽度和长度。一旦读取这些值，程序就应该计算和显示房间的面积。长度和宽度将作为浮点数输入。在提示和输出消息中包含单位：英尺或米，这取决于你使用哪个单位更舒服。
length_str = input("请输入房间的长度（米）：")
length = float(length_str) # 将字符串转换为浮点数

width_str = input("请输入房间的宽度（米）：")
width = float(width_str)   # 将字符串转换为浮点数

area = length * width
print("房间的面积是：", area, "平方米")

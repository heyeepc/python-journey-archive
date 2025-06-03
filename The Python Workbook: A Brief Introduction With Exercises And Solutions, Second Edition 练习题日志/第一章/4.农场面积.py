#创建一个程序，读取用户输入的农场的长度和宽度（单位是英尺）。以英亩为单位显示这块地的面积。
SQUARE_FEET_PER_ACRE = 43560

length_str = input("请输入农场的长度（英尺）：")
length = float(length_str) # 将字符串转换为浮点数

width_str = input("请输入农场的宽度（英尺）：")
width = float(width_str)   # 将字符串转换为浮点数

area = length * width
acre = area / SQUARE_FEET_PER_ACRE
print("农场的面积是：", area, "英尺",acre , "英亩")

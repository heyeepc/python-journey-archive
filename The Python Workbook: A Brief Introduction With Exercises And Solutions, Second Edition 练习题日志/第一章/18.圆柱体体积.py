#圆柱体的体积可以用圆底面积乘以高来计算。编写一个程序，从用户那里读取圆柱体的半径和高，并计算其体积。显示四舍五入到小数点后一位的结果。
import math

radius_str = input("请输入圆柱体的半径 (r)：")
radius = float(radius_str)

height_str = input("请输入圆柱体的高度 (h)：")
height = float(height_str)

volume = math.pi * (radius ** 2) * height

print(f"\n圆柱体的体积是：{volume:.1f}")

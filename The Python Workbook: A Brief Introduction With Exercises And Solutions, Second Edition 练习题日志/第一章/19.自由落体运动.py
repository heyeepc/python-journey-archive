#创建一个程序来确定物体落地时的速度。用户输入物体下落的高度，单位为米，因为物体下落的初始速度为0米/秒。假设重力加速度是9.8米/秒2。当初始速度v、加速度a和距离d已知时.
import math

GRAVITY_ACCELERATION = 9.8

height_str = input("请输入物体下落的高度（单位：米）：")
height = float(height_str)

final_velocity = math.sqrt(2 * GRAVITY_ACCELERATION * height)

print(f"\n物体落地时的速度是：{final_velocity:.2f} 米/秒")

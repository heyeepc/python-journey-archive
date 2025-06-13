#编写一个程序，首先读取用户的半径r。程序将计算和显示半径为r的圆的面积，以及半径为r的球体的体积。在计算中使用math 模块中的pi常数。
r = float(input("输入半径:"))
Area = r ** 2 * math.pi
Volume = 4/3 * math.pi * r ** 3
print(f"面积等于：{Area:.2f}")
print(f"体积等于：{Volume:.2f}")

#如果一个多边形的所有边长都相同，并且所有相邻边之间的夹角都相等，那么这个多边形就是正多边形。正多边形的面积可以用以下公式计算，其中s为边长，n为边的个数：
#编写一个程序，从用户那里读取s和n，然后显示由这些值构成的正多边形的面积。
import math

s_str = input("边长 (s)：")
s = float(s_str)

n_str = input("边的个数 (n)：")
n = int(n_str)

# 使用正确的正多边形面积公式
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(f"面积: {area:.2f}")

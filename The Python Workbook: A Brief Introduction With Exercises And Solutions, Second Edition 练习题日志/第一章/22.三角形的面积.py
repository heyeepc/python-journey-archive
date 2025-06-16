#在前面的练习中，创建了一个程序，该程序在已知三角形的底和高时计算三角形的面积。当已知三角形的三边长度时，也可以计算三角形的面积。设s1、S2、83为边的长度。设s=（s1+s2+s3）/2。
#然后用以下公式计算三角形的面积：开发一个程序，从用户那里读取三角形的边长，并显示其面积。
import math

while True:
        try:
            # 1. 从用户获取三条边长
            s1_str = input("请输入第一条边的长度 (s1)：")
            s1 = float(s1_str)

            s2_str = input("请输入第二条边的长度 (s2)：")
            s2 = float(s2_str)

            s3_str = input("请输入第三条边的长度 (s3)：")
            s3 = float(s3_str)

            
            # 检查边长是否为正数
            if s1 <= 0 or s2 <= 0 or s3 <= 0:
                print("输入错误：边的长度必须是正数。请重新输入。")
                continue

            # 检查三角形不等式定理：
            # 任意两边之和必须大于第三边，否则无法构成三角形。
            if not (s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
                print("输入错误：这三条边无法构成一个有效的三角形。")
                print("任意两边之和必须大于第三边。请重新输入。")
                continue

            # 2. 计算半周长 (s)
            s = (s1 + s2 + s3) / 2

            # 3. 使用海伦公式计算面积
            # 面积 = sqrt(s * (s - s1) * (s - s2) * (s - s3))
            # math.sqrt() 用于计算平方根
            area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

            # 4. 显示结果，四舍五入到小数点后两位
            print(f"\n三角形的面积是：{area:.2f}")
            break # 计算成功，退出循环

        except ValueError:
            # 捕获当用户输入非数字字符时的错误
            print("输入错误：请输入有效的数字作为边长。请重新输入。")
        except Exception as e:
            # 捕获其他任何意外错误
            print(f"发生了一个意外错误：{e}")


#许多人以英尺和英寸来计算身高，甚至在一些主要使用公制单位的国家也是如此。编写一个程序，读取用户的英尺数，然后是英寸数。一旦读取了这些值，程序就应该计算并显示相应的厘米数。
def convert_height_to_cm():

    while True:
        try:
            # 获取英尺数
            feet_str = input("请输入您的英尺数（例如：5）：")
            feet = int(feet_str)

            # 获取英寸数
            inches_str = input("请输入您的英寸数（例如：10）：")
            inches = int(inches_str)

            # --- 输入验证 ---
            if feet < 0 or inches < 0:
                print("输入错误：英尺和英寸不能是负数。请重新输入。")
                continue  # 继续循环，让用户重新输入

            # 假设英寸不会超过12，如果用户输入例如15英寸，也可以处理
            # 也可以在这里添加一个提示，如果英寸大于等于12，提示用户将其合并到英尺
            # 例如：if inches >= 12: print("提示：英寸数通常小于12，您可以将其合并到英尺数中。")

            # 1. 将英尺转换为总英寸数
            total_inches = (feet * 12) + inches

            # 2. 将总英寸数转换为厘米
            # 1 英寸 = 2.54 厘米
            total_centimeters = total_inches * 2.54

            # 3. 显示结果，保留两位小数，更符合身高显示习惯
            print(f"\n您的身高是：{total_centimeters:.2f} 厘米")
            break  # 转换成功，退出循环

        except ValueError:
            # 捕获当用户输入非整数时的错误
            print("输入错误：请输入有效的整数。请重新输入。")
        except Exception as e:
            # 捕获其他可能的错误
            print(f"发生了一个意外错误：{e}")


# 调用主函数来运行程序
if __name__ == "__main__":
    convert_height_to_cm()

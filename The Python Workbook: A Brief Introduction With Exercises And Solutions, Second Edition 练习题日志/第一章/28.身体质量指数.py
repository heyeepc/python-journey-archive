#编写一个程序来计算一个人的身体质量指数（BMI）。程序应首先读取用户的身高和体重，然后使用以下两个公式之一计算BMI，之后显示它。如果用英寸表示身高，用磅表示体重，那么体重指数的计算方法如下。
def calculate_bmi():
    """
    计算并显示一个人的身体质量指数（BMI）。
    程序会根据用户选择的单位（公制或英制）进行计算。
    """
    print("--- 身体质量指数 (BMI) 计算器 ---")
    print("请选择您想输入的单位类型：")
    print("1. 公制 (身高：米, 体重：千克)")
    print("2. 英制 (身高：英寸, 体重：磅)")

    while True:
        unit_choice = input("请输入您的选择 (1 或 2)：")
        if unit_choice == '1' or unit_choice == '2':
            break
        else:
            print("选择无效，请输入 1 或 2。")

    while True:
        try:
            if unit_choice == '1':  # 公制单位
                height_m_str = input("请输入您的身高（单位：米，例如 1.75）：")
                height_m = float(height_m_str)

                weight_kg_str = input("请输入您的体重（单位：千克，例如 70）：")
                weight_kg = float(weight_kg_str)

                # --- 输入验证 ---
                if height_m <= 0 or weight_kg <= 0:
                    print("身高和体重都必须是正数。请重新输入。")
                    continue

                # 计算 BMI (公制)
                bmi = weight_kg / (height_m ** 2)

            else:  # 英制单位
                height_in_str = input("请输入您的身高（单位：英寸，例如 68）：")
                height_in = float(height_in_str)

                weight_lbs_str = input("请输入您的体重（单位：磅，例如 150）：")
                weight_lbs = float(weight_lbs_str)

                # --- 输入验证 ---
                if height_in <= 0 or weight_lbs <= 0:
                    print("身高和体重都必须是正数。请重新输入。")
                    continue

                # 计算 BMI (英制)
                # 英制公式需要乘以一个转换系数 703
                bmi = (weight_lbs / (height_in ** 2)) * 703

            # 显示 BMI 结果
            print(f"\n您的身体质量指数 (BMI) 是：{bmi:.2f}")

            # 简单地根据 BMI 值给出一些解释（可选，但很实用）
            if bmi < 18.5:
                print("根据您的 BMI，您可能偏瘦。")
            elif 18.5 <= bmi < 24.9:
                print("根据您的 BMI，您的体重正常。")
            elif 25 <= bmi < 29.9:
                print("根据您的 BMI，您可能超重。")
            else:
                print("根据您的 BMI，您可能肥胖。")

            break  # 计算成功，退出循环

        except ValueError:
            print("输入错误：请输入有效的数字。请重新输入。")
        except Exception as e:
            print(f"发生了一个意外错误：{e}")


# 当脚本直接运行时，调用计算函数
if __name__ == "__main__":
    calculate_bmi()

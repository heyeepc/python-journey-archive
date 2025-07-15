def calculate_dog_age(human_age):
    
    if human_age < 0:
        return "错误：人类年龄不能是负数。"
    elif human_age <= 2:
        dog_age = human_age * 10.5
    else:
        # 前两年每一年算作 10.5 狗年
        dog_age = 2 * 10.5
        # 两年后每一年算作 4 狗年
        dog_age += (human_age - 2) * 4
    return dog_age

# 获取用户输入
try:
    human_input = float(input("请输入人类的年龄（年）："))
    result = calculate_dog_age(human_input)

    if isinstance(result, str):
        print(result)
    else:
        print(f"{human_input} 人年相当于 {result:.2f} 狗年。")
except ValueError:
    print("输入无效。请输入一个数字。")

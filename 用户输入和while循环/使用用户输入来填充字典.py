students = {}

# 输入姓名（不做限制）
name = input("请输入姓名：")

# 输入年龄（必须是阿拉伯数字）
while True:
    age = input("请输入年龄（数字）：")
    if age.isdigit():  # 判断是否只包含数字字符
        age = int(age)  # 转为整数
        break
    else:
        print("年龄必须是阿拉伯数字，请重新输入。")

# 输入性别（只能是男或女）
while True:
    gender = input("请输入性别（男/女）：")
    if gender in ["男", "女"]:
        break
    else:
        print("性别只能是'男'或'女'，请重新输入。")

# 填入字典
students["名字"] = name
students["年龄"] = age
students["性别"] = gender

# 打印信息
print("录入信息：")
for key, value in students.items():
    print(f"{key}: {value}")

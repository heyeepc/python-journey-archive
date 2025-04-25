aaa = []

def evaluate(name, score):
    if score >= 90:
        print(f"{name}：优秀")
    elif score >= 60:
        print(f"{name}：及格")
    else:
        print(f"{name}：不及格")

while True:
    name = input("请输入学生名字（输入 q 退出）：")
    if name.lower() == "q":
        break  # 如果输入q，则退出输入

    score_input = input("请输入成绩：")
    if not score_input.isdigit():
        print("成绩必须是数字！请重新输入。")
        continue

    score = int(score_input)

    # 添加到列表中
    aaa.append({"name": name, "score": score})

# 输出评价
print("\n学生评价如下：")
for student in aaa:
    evaluate(student["name"], student["score"])

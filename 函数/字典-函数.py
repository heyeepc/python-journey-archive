aaa = [
    {"name": "小明", "score": 100},
    {"name": "小亮", "score": 99}
]

def evaluate(name, score):
    if score >= 90:
        print(f"{name}：优秀")
    elif score >= 60:
        print(f"{name}：及格")
    else:
        print(f"{name}：不及格")

for student in aaa:
    evaluate(student["name"], student["score"])

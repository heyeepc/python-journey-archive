import re

plate = input("输入车牌号: ").strip()

if re.fullmatch(r"[A-Z]{3}\d{3}", plate):
    print("是旧车牌")
elif re.fullmatch(r"\d{4}[A-Z]{3}", plate):
    print("是新车牌")
else:
    print("不符合规矩的车牌")

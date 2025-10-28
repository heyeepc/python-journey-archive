plate = input("输入车牌号: ").strip()
letters = sum(1 for c in plate if c.isupper())
digits = sum(1 for c in plate if c.isdigit())

if len(plate) == 6 and letters == 3 and digits == 3:
    print("是旧车牌")
elif len(plate) == 7 and letters == 3 and digits == 4:
    print("是新车牌")
else:
    print("不符合规矩的车牌")

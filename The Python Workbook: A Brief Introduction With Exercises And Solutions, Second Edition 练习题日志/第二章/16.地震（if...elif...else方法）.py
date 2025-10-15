m = float(input("震级："))

if m < 2.0:
    level = "超微"
elif m < 3.0:
    level = "甚微"
elif m < 4.0:
    level = "微小"
elif m < 5.0:
    level = "弱"
elif m < 6.0:
    level = "中"
elif m < 7.0:
    level = "强"
elif m < 8.0:
    level = "甚强"
elif m < 10.0:
    level = "极强"
else:
    level = "超强"

print(level)

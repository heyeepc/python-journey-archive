numbers = []
while True:
    x = int(input("输入数字"))

    if x == 0:
       break  # 0 表示输入结束
    numbers.append(x)

a = sum(z for z in numbers)
print(a)

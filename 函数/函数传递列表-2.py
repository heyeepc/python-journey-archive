basket = []  # 创建空列表

while True:
    fruit = input("请输入水果名字（输入q退出）：")
    if fruit == "q":
        break  # 退出循环
    basket.append(fruit)  # 加到列表里

print("你的水果篮子里有：")
for f in basket:
    print(f)

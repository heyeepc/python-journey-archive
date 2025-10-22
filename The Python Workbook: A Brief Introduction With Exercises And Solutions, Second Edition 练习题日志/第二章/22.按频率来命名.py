#编写一个程序，读取来自用户的辐射频率，并显示辐射的名称，作为适当消息的一部分

try:
    f = float(input("请输入辐射频率（Hz）："))
    if f < 0:
        name = "频率值无效（小于零）"
    elif f >= 3e19:
        name = "伽马射线"
    elif f >= 3e17:
        name = "X 射线"
    elif f >= 7.5e14:
        name = "紫外线"
    elif f >= 4.3e14:
        name = "可见光"
    elif f >= 3e12:
        name = "红外光"
    elif f >= 3e9:
        name = "微波"
    else:
        name = "无线电波"

    print(f"频率 {f:.2e} Hz 属于{name}")
except ValueError:
    print("输入无效，请输入数字。")

with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # 去掉换行符

with open("example.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:  # 读到末尾时返回空字符串
            break
        print(line.strip())

with open("example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 返回一个列表，每一行是一个元素
    for line in lines:
        print(line.strip())

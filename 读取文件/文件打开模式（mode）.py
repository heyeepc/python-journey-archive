# r 模式：只读
with open("data.txt", "r") as f:
    content = f.read()

# w 模式：写入（会清空原文件）
with open("data.txt", "w") as f:
    f.write("Hello, world!")

# a 模式：追加写入
with open("data.txt", "a") as f:
    f.write("\nNew line added")

# r+ 模式：读写（但不会自动创建文件）
with open("data.txt", "r+") as f:
    old = f.read()
    f.seek(0)
    f.write("Replaced start")

# 为演示创建一个虚拟文件
with open('my_document.txt', 'w', encoding='utf-8') as f:
    f.write("第一行文本。\n")
    f.write("第二行。\n")
    f.write("第三行也是最后一行。\n")

# 现在，读取整个文件
with open('my_document.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()
    print("整个文件内容:")
    print(content)
  
with open('my_document.txt', 'r', encoding='utf-8') as file_obj:
    # 读取前 5 个字符
    first_part = file_obj.read(5)
    print(f"前 5 个字符: '{first_part}'") # 输出: '第一行文'

    # 从当前指针位置读取接下来的 8 个字符
    next_part = file_obj.read(8)
    print(f"接下来的 8 个字符: '{next_part}'") # 输出: '本。\n第二'

    # 读取文件的其余部分
    rest_of_file = file_obj.read()
    print(f"文件剩余部分: '{rest_of_file}'")

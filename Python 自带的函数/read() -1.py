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
  

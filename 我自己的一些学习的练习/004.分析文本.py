filename = "alice.txt"

try:
    # 尝试打开文件
    with open(filename, encoding='utf-8') as f_obj: # 推荐加上编码参数
        contents = f_obj.read()

except FileNotFoundError: 
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 文件成功读取后执行的代码
    words = contents.split()
    num_words = len(words)
    
    print("The file " + filename + " has about " + str(num_words) + " words.")

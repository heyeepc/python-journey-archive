with open("data.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents)
#上面这个 with ... as 结构就是上下文管理器，它的作用是：

#在进入代码块时 自动打开文件

#在代码块结束时（无论是否出错）自动关闭文件

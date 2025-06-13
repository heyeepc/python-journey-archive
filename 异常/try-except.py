try:
    # 可能出错的代码
    f = open("不存在的文件.txt", "r")
except FileNotFoundError:
    print("文件没找到！")

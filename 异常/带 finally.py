try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print("其他错误：", e)
finally:
    print("不管出不出错，这里都会执行")

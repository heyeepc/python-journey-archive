#Exception 是所有异常的父类
try:
    x = int(input("分子："))
    y = int(input("分母："))
    print(x / y)
except ZeroDivisionError:
    print("不能除以 0！")
except ValueError:
    print("请输入整数！")
    
except Exception as e:
    print("出错了：", e)

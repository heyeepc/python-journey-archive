def multiply(x, y):
    product = x * y
    return product # 返回计算出的乘积

result = multiply(4, 5) # 函数返回 20，该值存储在 'result' 变量中
print(result)

def my_function():
    print("这行代码会运行。")
    return "返回值"
    print("这行代码不会运行。") # 这行代码是不可达的

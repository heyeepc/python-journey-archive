def greet(name, message="欢迎！"):
    print(f"{message} {name}")

greet("小明")             # 没有给message，使用默认的"欢迎！"
greet("小红", "早上好~")   # 给了message，用新的

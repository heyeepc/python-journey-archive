class Person:
    def __init__(self, name, age):  # 构造函数
        self.name = name            # 设置属性
        self.age = age

# 创建对象时，__init__ 会被自动调用
p = Person("Alice", 18)

print(p.name)  # 输出: Alice
print(p.age)   # 输出: 18

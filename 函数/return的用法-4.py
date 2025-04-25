def is_even(num):
    if num % 2 == 0:
        return "是偶数"
    else:
        return "是奇数"

a = int(input("输入一个数字："))
result = is_even(a)
print(result)

#编写一个表达式，统计列表 data_list 中所有奇数的个数
data_list = [10, 21, 30, 45, 52, 67, 80, 93, 100]
a = sum(1 for x in data_list if x % 2 == 1)
print(a)

#编写一个表达式，计算一个字符串列表中所有字符串的总长度。
names = ["Python", "Network", "Engineer", "Raspberry Pi 5", "Gemini"]
b = sum(len(s) for s in names )
print(b)

#编写一个表达式，找出列表 ports 中大于 1024 且小于 65535 的端口号，并将它们组合成一个新的列表。
ports = [21, 80, 1024, 3389, 5000, 60000, 65536, 110, 22]
c = [z for z in ports if 1040 < z < 65535]
print(c)

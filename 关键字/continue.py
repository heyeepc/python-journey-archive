for i in range(5):
    if i == 2:
        continue # 当 i 等于 2 时，跳过当前循环的 print，进入下一次循环
    print(i)
# 输出:
# 0
# 1
# 3
# 4

#Python的time 模块包括几个与时间相关的函数。其中之一是asctime（）函数，它从计算机的内部时钟读取当前时间，并以人类可读的格式返回。使用此函数编写一个程序，显示当前时间和日期。程序不需要用户输入
import time
t = time.asctime()
print(t)

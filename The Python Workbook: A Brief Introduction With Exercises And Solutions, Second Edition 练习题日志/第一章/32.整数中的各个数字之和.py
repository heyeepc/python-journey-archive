#开发一个程序，从用户那里读取一个四位数的整数并显示其位数的和。例如，如果用户输入3141，那么程序应该显示3+1+4+l=9。
number_str = input("请输入一个四位数的整数：")
number = int(number_str)

digit1 = abs_number % 10
remaining_number = abs_number // 10 
digit2 = remaining_number % 10
remaining_number = remaining_number // 10
digit3 = remaining_number % 10
remaining_number = remaining_number // 10
digit4 = remaining_number 
total_sum = digit1 + digit2 + digit3 + digit4
print(f"{digit4} + {digit3} + {digit2} + {digit1} = {total_sum}")

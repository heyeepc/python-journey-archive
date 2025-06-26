#编写一个程序，首先读取用户输入的温度（以摄氏度为单位）。
#然后程序应该以华氏度和开尔文度显示等效温度。转换不同温度单位所需的计算公式可在因特网上找到。
celsius_str = input("请输入温度（单位：摄氏度 ℃）：")
celsius = float(celsius_str)

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f"\n等效的华氏度是：{fahrenheit:.2f} °F")
print(f"等效的开尔文度是：{kelvin:.2f} K")


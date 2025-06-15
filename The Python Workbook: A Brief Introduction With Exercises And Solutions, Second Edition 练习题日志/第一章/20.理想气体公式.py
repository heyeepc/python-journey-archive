#编写一个程序，当用户提供了压力、体积和温度时，计算气体量，单位是mol。测试程序：确定 SCUBA 水箱中气体的摩尔数。典型的 SCUBA 水箱能在2000万Pa（约3000PSI）的压力下装12L气体。室温大约是20摄氏度或68华氏度。
import math

IDEAL_GAS_CONSTANT_R = 8.314  # 理想气体常数，单位：J/(mol·K)
LITERS_TO_CUBIC_METERS = 0.001 # 1 升 = 0.001 立方米
CELSIUS_TO_KELVIN_OFFSET = 273.15 # 摄氏度转开尔文的偏移量

pressure_pa_str = input("请输入气体压力（单位：帕斯卡 Pa）：")
pressure_pa = float(pressure_pa_str)

volume_liters_str = input("请输入气体体积（单位：升 L）：")
volume_liters = float(volume_liters_str)

temperature_celsius_str = input("请输入气体温度（单位：摄氏度 ℃）：")
temperature_celsius = float(temperature_celsius_str)

volume_cubic_meters = volume_liters * LITERS_TO_CUBIC_METERS

temperature_kelvin = temperature_celsius + CELSIUS_TO_KELVIN_OFFSET

moles = (pressure_pa * volume_cubic_meters) / \
                    (IDEAL_GAS_CONSTANT_R * temperature_kelvin)

print(f"\n气体量 n 是：{moles:.2f} 摩尔 (mol)")

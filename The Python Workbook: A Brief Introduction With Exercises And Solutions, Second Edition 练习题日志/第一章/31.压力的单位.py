#这个练习将创建一个程序，来读取用户输入的千帕斯卡压力。一旦读取了压力，程序应该报告等效的压力（以磅/平方英寸、毫米汞柱和大气压为单位）。利用研究技能来确定这些单位之间的转换系数。
KPA_TO_PSI = 0.1450377
KPA_TO_MMHG = 7.50062
KPA_TO_ATM = 0.00986923

pressure_psi = pressure_kpa * KPA_TO_PSI
pressure_mmhg = pressure_kpa * KPA_TO_MMHG
pressure_atm = pressure_kpa * KPA_TO_ATM

print(f"  {pressure_psi:.2f} PSI (磅/平方英寸)")
print(f"  {pressure_mmhg:.2f} mmHg (毫米汞柱)")
print(f"  {pressure_atm:.2f} atm (标准大气压)")

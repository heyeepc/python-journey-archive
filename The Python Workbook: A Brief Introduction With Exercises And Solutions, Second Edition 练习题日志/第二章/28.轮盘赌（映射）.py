import random

# 用 37 表示 "00"
n = random.randint(0, 37)  # 0..37
def label(x):
    return "00" if x == 37 else str(x)

red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}

print(f"The spin resulted in {label(n)}...\nPay")
if n in (0, 37):
    print(f"Pay {label(n)}")
else:
    print(f"Pay {n}")
    print("Pay Red" if n in red else "Pay Black")
    print("Pay Even" if n % 2 == 0 else "Pay Odd")
    print("Pay 1 to 18" if 1 <= n <= 18 else "Pay 19 to 36")

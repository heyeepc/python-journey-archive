import random

wheel = [0, "00"] + list(range(1, 37))
red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}

result = random.choice(wheel)
print(f"The spin resulted in {result}...\nPay")
if result in (0, "00"):
    print(f"Pay {result}")
else:
    print(f"Pay {result}")
    print("Pay Red" if result in red else "Pay Black")
    print("Pay Even" if result % 2 == 0 else "Pay Odd")
    print("Pay 1 to 18" if 1 <= result <= 18 else "Pay 19 to 36")

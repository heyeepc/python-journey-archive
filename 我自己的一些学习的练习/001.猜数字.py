import random
secret_number = random.randint(1, 100)
guesses = 0
while True:
    guesses += 1
    guess = int(input("输入一个数字: "))

    if guess > secret_number:
        print("数字大了，再猜一次")
    elif guess < secret_number:
        print("数字小了，再猜一次")
    elif guess == secret_number:
        print("猜对了")
        break

print(f"一共猜了{guesses}次")

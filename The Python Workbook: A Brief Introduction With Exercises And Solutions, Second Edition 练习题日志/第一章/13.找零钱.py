#考虑在自动结账机上运行的软件。它必须能执行的一项任务是，确定当购物者用现金购买时，需要提供多少零钱。编写一个程序，首先从用户那里读取一个整数。然后，计算和显示硬币的面额，这些硬币应该用来给购物者提供足够的零钱。
#零钱应该尽可能少用硬币。假设这台机器装满了1分、5分、10分、25分、1元和2元硬币。
#一美元硬币于1987年在加拿大发行。它称为loonie，因为硬币的一面有一个潜鸟图像。两美元硬币称为toonie，是在9年后推出的。它的名字来源于数字2和loonie的组合。
def calculate_change(amount_cents):
    denominations = {
        200: "2 加元 (Toonie)",
        100: "1 加元 (Loonie)",
        25: "25 分 (Quarter)",
        10: "10 分 (Dime)",
        5: "5 分 (Nickel)",
        1: "1 分 (Penny)"
    }
    # 存储每种硬币的数量
    change_breakdown = {}
    for coin_value in sorted(denominations.keys(), reverse=True):
        if amount_cents == 0:
            break  # 如果已经找完零，就停止循环

        num_coins = amount_cents // coin_value
        if num_coins > 0:
            change_breakdown[denominations[coin_value]] = num_coins
            # 更新剩余需要找零的金额
            # % 是模运算，例如 275 % 200 = 75 （剩余75分）
            amount_cents %= coin_value
        if not change_breakdown and amount_cents == 0:
            print("无需找零。")
        elif not change_breakdown and amount_cents > 0:
            # 这种情况通常不会发生，除非硬币面额列表不完整或者输入金额为负数
            print(f"无法找零剩余的 {amount_cents} 分。")
        else:
            print("\n应找零的硬币明细：")
            for coin_name, count in change_breakdown.items():
                print(f"- {coin_name}: {count} 个")

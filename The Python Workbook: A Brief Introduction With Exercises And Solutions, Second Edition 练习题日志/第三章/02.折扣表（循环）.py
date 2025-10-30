prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount_rate = 0.6

print(f"{'原价':<10}{'折扣金额':<10}{'新价':<10}")
for price in prices:
    new_price = price * discount_rate
    discount = price - new_price
    print(f"${price:<8.2f}${discount:<8.2f}${new_price:<8.2f}")

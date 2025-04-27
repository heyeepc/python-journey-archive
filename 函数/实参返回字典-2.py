def build_order(food, drink="矿泉水"):
    order = {
        "food": food,
        "drink": drink
    }
    return order

customer_order = build_order("炸鸡", "可乐")
print(customer_order)

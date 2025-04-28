def process_orders(unprocessed, completed):
    while unprocessed:
        current_order = unprocessed.pop()  # 取出一个
        print(f"正在处理订单：{current_order}")
        completed.append(current_order)

unprocessed_orders = ["汉堡", "薯条", "炸鸡"]
completed_orders = []

process_orders(unprocessed_orders, completed_orders)

print("已完成的订单：", completed_orders)

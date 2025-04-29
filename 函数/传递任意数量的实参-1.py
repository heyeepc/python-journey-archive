def make_soup(*ingredients):
    print("这碗汤包含：")
    for item in ingredients:
        print(f"- {item}")

make_soup("土豆", "胡萝卜", "排骨")

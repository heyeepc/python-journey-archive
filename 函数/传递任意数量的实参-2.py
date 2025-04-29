def create_user(**info):
    print("创建的用户信息：")
    for key, value in info.items():
        print(f"{key}：{value}")

create_user(name="小红", age=18, gender="女")

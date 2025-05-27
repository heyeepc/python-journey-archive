def customer_service_scenario():
    """
    模拟顾客在餐馆遇到问题并与服务员互动的场景。
    """
    dishes = ["菜1", "菜2", "菜3", "菜4"] 
    # 假设菜里真的有“瓶盖”，或者这是模拟一个错误情况
    if "瓶盖" in dishes: # 这个条件如果 dishes 里没有“瓶盖”就永远不会触发
        print("哥们儿咋开的瓶盖啊？都开我菜里啦!")
        
        response_from_waiter = input("请输入文本: ")
        
        if response_from_waiter == "对不起哥们，我给你换一盘吧，实在对不起。":
            print("你都这么说了那还有啥事呢？直接挑出来不就行了")
            
            
            print("哎哥们你还有烟吗？")
            # 这里的逻辑是如果服务员回答“没有”，就触发后续
            
            
            # if waiter_has_cigarette == "没有":
            
            print("哎，服务员……") 
            
            # 询问是否去后备箱拿烟
            go_to_car_for_cigarette = input("是否去后备箱拿烟给他 (y/n): ")
            
            if go_to_car_for_cigarette.lower() == "y": # .lower() 可以让大小写Y都识别
                print("哎呀哥们你这太性情了，谢谢昂")
                print("行哥们，你先吃我们走了昂")
                return "结账" # 结束这个场景并返回“结账”
            else:
                print("那好吧，谢谢。") # 如果不去拿烟
        else:
            print("请给我一个合理的解释。") # 如果服务员没有说“对不起”
    else:
        print("菜品很干净，没有瓶盖。") # 如果菜里没有瓶盖，这个分支会执行

# 运行模拟
final_status = customer_service_scenario()
print(f"场景结束，状态: {final_status}")

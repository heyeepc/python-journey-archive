#这是它最直接的用途。当程序执行到某个点，你确定无法继续或已经完成了所有必要的任务时，可以使用 sys.exit() 来立即停止程序，而不是等待代码执行到最后一行。
call_minutes = float(input("输入通话时间(分): ").strip())
text_messages = int(input("输入短信数量: ").strip())
if call_minutes < 0 or text_messages < 0:
    print("输入无效：通话时间和短信数量不能为负。")
    sys.exit(1)

#0 (默认或 sys.exit(0)): 表示程序成功执行完毕，正常退出
#任何非零值 (例如 sys.exit(1)): 表示程序因错误或异常情况而退出。

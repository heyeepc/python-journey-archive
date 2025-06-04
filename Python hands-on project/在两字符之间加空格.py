def add_spaces_to_sentence_join(sentence):
    """
    在句子的每两个字符之间添加一个空格。
    例如: "你好" -> "你 好"
    """
    return " ".join(sentence)

# 获取用户输入
user_input = input("请输入一段文字，我会在每两个字符之间添加空格：")

# 处理并打印结果
print(add_spaces_to_sentence_join(user_input))

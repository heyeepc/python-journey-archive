def add_book(library, title, author):
    """把一本书添加到图书馆列表"""
    book = {"书名": title, "作者": author}
    library.append(book)


# 创建空的图书馆列表
library = []

# 开始循环添加书籍
while True:
    title = input("请输入书名（输入q退出）：")
    if title == "q":
        break
    author = input("请输入作者（输入q退出）：")
    if author == "q":
        break

    add_book(library, title, author)  # 调用函数，把书加进列表

# 循环结束，打印所有书
print("\n录入的所有图书信息：")
for book in library:
    print(f'书名：{book["书名"]}，作者：{book["作者"]}')

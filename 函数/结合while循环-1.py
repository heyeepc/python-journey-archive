def make_book(title, author):
    books = {
        "书名": title,
        "作者": author
    }
    return books

library = []  # 用来存所有的书

while True:
    title = input("请输入书名（输入q退出）：")
    if title == "q":
        break
    author = input("请输入作者：")
    if author == "q":
        break

    # 调用函数，得到一本书的字典
    book = make_book(title, author)

    # 把这本书添加到列表
    library.append(book)

# 最后输出
print("录入的图书信息有：")
for book in library:
    print(book)

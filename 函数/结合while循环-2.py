def make_book(title, author, publication_year=None):
    book = {
        "书名": title,
        "作者": author
    }
    if publication_year:  # 如果有出版年
        book["出版年"] = publication_year
    return book

library = []

while True:
    title = input("请输入书名（输入q退出）：")
    if title == "q":
        break
    author = input("请输入作者（输入q退出）：")
    if author == "q":
        break
    pub_input = input("请输入出版年（不输入，输入no跳过）：")
    if pub_input == "no":
        publication_year = None
    else:
        publication_year = pub_input  # 有输入年份

    # 创建图书字典
    book = make_book(title, author, publication_year)
    library.append(book)

print("\n录入的图书信息有：")
for book in library:
    print(book)

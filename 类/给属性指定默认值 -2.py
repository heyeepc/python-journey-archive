class Book:
    genre = "小说"  # 所有书籍默认都是“小说”

    def __init__(self, title, author, year=2000):
        self.title = title
        self.author = author
        self.year = year

book = Book("红楼梦", "曹雪芹")
print(book.genre)  # 输出“小说”

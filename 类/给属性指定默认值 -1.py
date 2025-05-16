class Book:
    def __init__(self, title="未知书名", author="佚名", year=2000):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f'书名：{self.title}\n作者：{self.author}\n出版年份：{self.year}')

book1 = Book()
book1.describe()

book2 = Book("三体", "刘慈欣")
book2.describe()

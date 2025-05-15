class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f'书名：{self.title}\n作者：{self.author}\n出版年份：{self.year}')

    def is_classic(self):
        if self.year >= 2000:
            print("这是现代书籍")
        else:
            print("这是经典书籍")

b1 = Book("三体", "刘慈欣", 2008)
b1.describe()
b1.is_classic()

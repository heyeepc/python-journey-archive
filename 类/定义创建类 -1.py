class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f'书名：{self.title}，作者：{self.author}')
        
b1 = Book("红楼梦", "曹雪芹")
b1.describe()

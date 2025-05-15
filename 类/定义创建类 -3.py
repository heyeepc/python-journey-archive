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

    # 新增：修改书名的方法
    def set_title(self, new_title):
        self.title = new_title

    # 新增：修改作者的方法
    def set_author(self, new_author):
        self.author = new_author

    # 新增：修改年份的方法
    def set_year(self, new_year):
        self.year = new_year

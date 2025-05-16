class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0  # 默认里程数为 0

    def describe(self):
        print(f'{self.year} {self.brand} {self.model}，已行驶 {self.odometer} 公里')

my_car = Car("Toyota", "Camry", 2020)
my_car.describe()

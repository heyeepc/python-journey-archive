class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0  # 默认值为 0

    def describe(self):
        print(f'{self.year} {self.brand} {self.model}，已行驶 {self.odometer} 公里')

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("不能回调里程数！")


my_car = Car("Toyota", "Camry", 2020)
my_car.update_odometer(15000)
my_car.describe()

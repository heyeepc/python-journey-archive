class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0  # 初始里程为0

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("不能调低里程！")

    def increment_odometer(self, km):
        if km >= 0:
            self.odometer += km
        else:
            print("不能增加负数的公里数！")

    def describe(self):
        print(f'{self.year} {self.brand} {self.model}，行驶了 {self.odometer} 公里')
      
my_car = Car("Honda", "Civic", 2021)
my_car.update_odometer(5000)
my_car.increment_odometer(150)
my_car.describe()

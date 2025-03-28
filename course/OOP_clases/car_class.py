class Car:
    def __init__(self, model, year, engine, price, run):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.run = run
        self.wheel = 4
        print("Запись о новом автомобиле создана")
    
    def description(self):
        description = (f"Модель - {self.model}, Год выпуска - {self.year},"
                       f" Объём двигателя - {self.engine}, Цена - {self.price}, Количество колёс - {self.wheel}")
        print(description)

class Truck(Car):
    def __init__(self, model, year, engine, price, run):
        super().__init__(model, year, engine, price, run)
        self.wheel = 8


prius = Car('Toyota', 2020, 2, 2000000, 100000)

prius.description()
TGM = Truck('MAN', 2025, 15, 20000000, 1000000)
TGM.description()
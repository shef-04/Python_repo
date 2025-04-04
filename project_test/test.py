# macでの初めてのコーディング
# まずは簡単なコードから書いていこう

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print(f"{self.color}の車が時速{self.speed}kmで走ります！")

my_car = Car("赤", 120)
your_car = Car("青", 100)

my_car.drive()   # 赤の車が時速120kmで走ります！
your_car.drive() # 青の車が時速100kmで走ります！

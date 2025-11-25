"""
Финальная задача №1
https://stepik.org/lesson/2010820/step/1?unit=2039017

Задача: "Транспортная система"
Легенда: Вы работаете в компании, которая разрабатывает программу для управления парком транспортных средств.
Вам нужно спроектировать иерархию классов для разных видов транспорта.

Техническое задание:
Вам необходимо создать три класса: Vehicle (Транспортное средство), Car (Автомобиль) и Bicycle (Велосипед).
"""

class Vehicle:
    vehicles_created = 0

    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        Vehicle.vehicles_created += 1

    def get_max_speed(self):
        return self._max_speed

    def get_mileage(self):
        return self._mileage

    def drive(self, distance):
        self._mileage += distance

    def display_info(self):
        print(f"Марка: {self.brand}\nМакс. скорость: {self._max_speed} км/ч\nПробег: {self._mileage} км")


class Car(Vehicle):
    def __init__(self, brand, max_speed, engine_type):
        super().__init__(brand, max_speed)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Тип двигателя: {self.engine_type}")


class Bicycle(Vehicle):
    def __init__(self, brand, max_speed, frame_material):
        super().__init__(brand, max_speed)
        self.frame_material = frame_material

    def display_info(self):
        super().display_info()
        print(f"Материал рамы: {self.frame_material}")


def main():
    # Создаем объекты разных классов
    tesla = Car("Tesla", 250, "Электро")
    bmw = Car("BMW", 280, "Бензин")
    trek = Bicycle("Trek", 40, "Карбон")

    # Демонстрируем полиморфизм: работаем с разными объектами через общий интерфейс
    vehicles = [tesla, bmw, trek]
    for vehicle in vehicles:
        print("---")
        vehicle.display_info() # Один и тот же вызов - разное поведение
        vehicle.drive(100)
        print(f"Пробег после поездки: {vehicle.get_mileage()} км")

    print("\n" + "="*30)
    # Демонстрируем работу атрибута класса
    print(f"Всего создано транспортных средств: {Vehicle.vehicles_created}")


if __name__ == "__main__":
    main()
"""
Финальная задача №3
https://stepik.org/lesson/2010820/step/3?unit=2039017

Финальная задача №3: "Иерархия Персонажей в Игре"

Легенда: Вы создаете классы для персонажей в компьютерной игре. Вам нужна иерархия для обычных воинов и магов.
"""
class Character:
    def __init__(self, name, damage):
        self.name = name
        self._health = 100
        self._damage = damage

    def attack(self, target):
        target.take_damage(self._damage)

    def take_damage(self, damage):
        self._health -= damage

    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self._health}"


class Warrior(Character):
    def __init__(self, name, damage, armor):
        super().__init__(name, damage)
        self.armor = armor

    def take_damage(self, amount):
        self._health -= (amount - self.armor) if amount > self.armor else 0


class Mage(Character):
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            super().attack(target)
            self.mana -= 10


def main():
    # Создаем персонажей
    warrior = Warrior("Конан", 15, 5) # Урон 15, Броня 5
    mage = Mage("Раистлин", 20, 100) # Урон 20, Мана 100

    print(warrior.get_status())
    print(mage.get_status())
    print("--- Битва ---")

    # Маг атакует воина
    mage.attack(warrior)
    print(warrior.get_status()) # Воин должен получить 15 урона (20 - 5 брони)

    # Воин атакует мага
    warrior.attack(mage)
    print(mage.get_status()) # Маг должен получить 15 урона

    # Проверка логики мага
    mage.mana = 5 # Устанавливаем мало маны
    mage.attack(warrior)
    print(warrior.get_status()) # Здоровье воина не должно измениться


if __name__ == '__main__':
    main()

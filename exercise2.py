"""
Финальная задача №2
https://stepik.org/lesson/2010820/step/2?unit=2039017

Финальная задача №2: "Система Библиотеки"

Легенда: Вы разрабатываете простую систему для учета печатных изданий в библиотеке.
Вам нужно создать иерархию классов для книг и журналов.
"""

class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self._year = year

    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year})'


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def get_info(self):
        res = super().get_info() + f", ISBN: {self.isbn}"
        return res


class Magazine(Publication):
    def __init__(self, title, editor, year, issue_number):
        super().__init__(title, editor, year)
        self.issue_number = issue_number

    def get_info(self):
        return  f'"{self.title}" (Ред. {self._author}, {self._year}), Выпуск №{self.issue_number}'


def main():
    # Создаем объекты разных классов
    book = Book("Война и мир", "Лев Толстой", 1869, "978-5-389-06254-2")
    magazine = Magazine("National Geographic", "Сьюзан Голдберг", 2021, 8)

    # Демонстрируем полиморфизм
    publications = [book, magazine]
    for pub in publications:
        # Один и тот же вызов - разное поведение
        print(pub.get_info())


if __name__ == "__main__":
    main()
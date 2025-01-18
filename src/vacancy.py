class Vacancy:
    """Класс для обработки вакансий"""

    def __init__(self, title, url, salary, description):
        """Создание экземпляра класса"""
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        """Вывод информации об экземпляре класса"""
        return f"{self.title} - {self.salary} руб.\n{self.url}\nОписание: {self.description}\n"

    def __lt__(self, other):
        """Сравнение экземпляра класса"""
        return self.salary > other.salary

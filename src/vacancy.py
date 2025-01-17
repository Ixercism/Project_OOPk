class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{self.title} - {self.salary} руб.\n{self.url}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.salary > other.salary

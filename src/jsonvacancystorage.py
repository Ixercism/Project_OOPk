import json
from src.vacancystorage_abc import VacancyStorage


class JSONVacancyStorage(VacancyStorage):

    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def save_to_file(self, vacancies):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([vacancy.__dict__ for vacancy in vacancies], file, ensure_ascii=False, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Vacancy(**item) for item in data]
        except:
            print('Файл не найден')

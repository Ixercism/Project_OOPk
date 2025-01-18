import json

from src.vacancystorage_abc import VacancyStorage
from src.vacancy import Vacancy


class JSONVacancyStorage(VacancyStorage):
    """Класс для работы с JSON файлами"""

    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def save_to_file(self, vacancies):
        """Метод для сохранения вакансий в файл"""

        new_vacancies = []
        try:
            old_vacancies = self.load_from_file()
        except Exception:
            old_vacancies = []
        with open(self.filename, "w", encoding="utf-8") as file:
            if old_vacancies is not None:
                new_vacancies.extend(old_vacancies)
            new_vacancies.extend(vacancies)
            json.dump(
                [vacancy.__dict__ for vacancy in new_vacancies],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def load_from_file(self):
        """Метод для загрузки вакансий из файла"""

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Vacancy(**item) for item in data]
        except FileNotFoundError:
            print("Файл не найден")

    def delete_from_file(self) -> None:
        """Общий функционал для удаления данных из файла"""

        self.save_to_file([])

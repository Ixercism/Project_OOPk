import json

from src.vacancystorage_abc import VacancyStorage
from src.vacancy import Vacancy


class JSONVacancyStorage(VacancyStorage):
    """Класс для работы с JSON файлами"""

    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def save_to_file(self, vacancies):
        """Метод для сохранения вакансий в файл"""

        # new_vacancies = [vacancy.__dict__ for vacancy in vacancies]
        # old_vacancies = self.load_from_file()
        # for vac in old_vacancies:
        #     vac_obj = Vacancy(vac["title"], vac["url"], vac["salary"], vac["description"])
        #     vacancies.append(vac_obj)
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [vacancy.__dict__ for vacancy in vacancies],
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
        except Exception(FileNotFoundError):
            print("Файл не найден")

    def delete_from_file(self) -> None:
        """Общий функционал для удаления данных из файла"""

        self.save_to_file([])
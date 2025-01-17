import json
from abc import ABC, abstractmethod

import requests

from src.jobapi_cls import JobAPI


class HeadhunterAPI(JobAPI):
    def get_vacancies(self, keyword, vacancies_count):
        BASE_URL = "https://api.hh.ru/vacancies"

        params = {"text": keyword, "area": 113, "per_page": vacancies_count}

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()["items"]
        else:
            return f"Ошибка при получении данных. Код ошибки: {response.status_code}"


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


class VacancyStorage(ABC):

    @abstractmethod
    def save_to_file(self, vacancies):
        """Метод для сохранения вакансий в файл"""
        pass

    @abstractmethod
    def load_from_file(self):
        """Метод для загрузки вакансий из файла"""
        pass


class JSONVacancyStorage(VacancyStorage):

    def __init__(self, filename="vacancies.json"):
        self.filename = filename

    def save_to_file(self, vacancies):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [vacancy.__dict__ for vacancy in vacancies],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Vacancy(**item) for item in data]
        except Exception(FileNotFoundError):
            print("Файл не найден")

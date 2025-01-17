import requests

from src.jobapi_cls import JobAPI


class HeadhunterAPI(JobAPI):
    """Класс для взаимодействия с API HH"""

    def get_vacancies(self, keyword, vacancies_count):
        """Метод для получения вакансий"""

        BASE_URL = "https://api.hh.ru/vacancies"

        params = {"text": keyword, "area": 113, "per_page": vacancies_count}

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()["items"]
        else:
            return f"Ошибка при получении данных. Код ошибки: {response.status_code}"

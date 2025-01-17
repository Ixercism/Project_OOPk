from abc import ABC, abstractmethod


class JobAPI(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод для получения вакансий по ключевому слову"""
        pass

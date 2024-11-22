from abc import ABC, abstractmethod


class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        """Метод для получения вакансий по ключевому слову"""
        pass


from abc import ABC, abstractmethod


class VacancyStorage(ABC):

    @abstractmethod
    def save_to_file(self, vacancies):
        """Метод для сохранения вакансий в файл"""
        pass

    @abstractmethod
    def load_from_file(self):
        """Метод для загрузки вакансий из файла"""
        pass

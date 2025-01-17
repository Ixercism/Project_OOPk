from abc import ABC, abstractmethod


class VacancyStorage(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_to_file(self, vacancies):
        """Метод для сохранения вакансий в файл"""
        pass

    @abstractmethod
    def load_from_file(self):
        """Метод для загрузки вакансий из файла"""
        pass

    @abstractmethod
    def delete_from_file(self) -> None:
        """Общий функционал для удаления данных из файла"""

        pass

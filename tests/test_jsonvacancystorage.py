import pytest
import json
from unittest.mock import mock_open, patch
from src.jsonvacancystorage import JSONVacancyStorage
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    """Фикстура для списка вакансий"""
    return [
        Vacancy(
            title="Python Developer",
            url="https://example.com/python-dev",
            salary=120000,
            description="Develop Python applications"
        ),
        Vacancy(
            title="Data Scientist",
            url="https://example.com/data-scientist",
            salary=150000,
            description="Analyze data and build ML models"
        ),
    ]


def test_save_to_file(sample_vacancies):
    """Тестирует сохранение вакансий в файл"""
    mock_data = '[{"title": "Old Vacancy", "url": "https://example.com/old-vacancy", "salary": 100000, "description": "Old description"}]'

    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked_file, \
         patch("json.load", return_value=json.loads(mock_data)), \
         patch("json.dump") as mocked_dump:

        storage = JSONVacancyStorage("test_vacancies.json")
        storage.save_to_file(sample_vacancies)

        # Проверяем, что файл открывался для записи
        # mocked_file.assert_called_once_with("test_vacancies.json", "w", encoding="utf-8")
        # Проверяем вызов json.dump с правильными данными
        mocked_dump.assert_called_once_with(
            [
                {"title": "Old Vacancy", "url": "https://example.com/old-vacancy", "salary": 100000, "description": "Old description"},
                {"title": "Python Developer", "url": "https://example.com/python-dev", "salary": 120000, "description": "Develop Python applications"},
                {"title": "Data Scientist", "url": "https://example.com/data-scientist", "salary": 150000, "description": "Analyze data and build ML models"},
            ],
            mocked_file(),
            ensure_ascii=False,
            indent=4,
        )


def test_load_from_file(sample_vacancies):
    """Тестирует загрузку вакансий из файла"""
    mock_data = json.dumps([vacancy.__dict__ for vacancy in sample_vacancies])

    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked_file:
        storage = JSONVacancyStorage("test_vacancies.json")
        result = storage.load_from_file()

        # Проверяем, что файл открывался для чтения
        mocked_file.assert_called_once_with("test_vacancies.json", "r", encoding="utf-8")
        # Проверяем корректность возвращаемых объектов Vacancy
        assert len(result) == len(sample_vacancies)
        for res_vac, sample_vac in zip(result, sample_vacancies):
            assert res_vac.title == sample_vac.title
            assert res_vac.url == sample_vac.url
            assert res_vac.salary == sample_vac.salary
            assert res_vac.description == sample_vac.description


def test_load_from_file_file_not_found():
    """Тестирует обработку ошибки, если файл не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError), \
         patch("builtins.print") as mocked_print:
        storage = JSONVacancyStorage("test_vacancies.json")
        result = storage.load_from_file()

        # Проверяем, что print вызывается с правильным сообщением
        mocked_print.assert_called_once_with("Файл не найден")
        # Проверяем, что результат равен None
        assert result is None


def test_delete_from_file():
    """Тестирует удаление всех данных из файла"""
    with patch("src.jsonvacancystorage.JSONVacancyStorage.save_to_file") as mocked_save:
        storage = JSONVacancyStorage("test_vacancies.json")
        storage.delete_from_file()

        # Проверяем, что save_to_file вызывается с пустым списком
        mocked_save.assert_called_once_with([])
import pytest
from unittest.mock import patch, MagicMock
from src.headhunterapi import HeadhunterAPI


@pytest.fixture
def hh_api():
    return HeadhunterAPI()


def test_get_vacancies_success(hh_api):
    mock_response_data = {
        "items": [
            {"id": "1", "name": "Software Engineer"},
            {"id": "2", "name": "Data Scientist"},
        ]
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(status_code=200, json=lambda: mock_response_data)

        keyword = "Python"
        vacancies_count = 2
        result = hh_api.get_vacancies(keyword, vacancies_count)

        mock_get.assert_called_once_with(
            "https://api.hh.ru/vacancies",
            params={"text": keyword, "area": 113, "per_page": vacancies_count},
        )

        assert result == mock_response_data["items"]

def test_get_vacancies_error(hh_api):
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(status_code=404)

        keyword = "Python"
        vacancies_count = 2
        result = hh_api.get_vacancies(keyword, vacancies_count)

        mock_get.assert_called_once_with(
            "https://api.hh.ru/vacancies",
            params={"text": keyword, "area": 113, "per_page": vacancies_count},
        )

        assert result == "Ошибка при получении данных. Код ошибки: 404"
import pytest

from src.vacancy import Vacancy


def test_vacancy_creation():
    vacancy = Vacancy("Developer", "http://example.com", 100000, "Python developer")
    assert vacancy.title == "Developer"
    assert vacancy.url == "http://example.com"
    assert vacancy.salary == 100000
    assert vacancy.description == "Python developer"

def test_vacancy_salary_validation_int():
    vacancy = Vacancy("Manager", "http://example.com", 50000, "Manager position")
    assert vacancy.salary == 50000

def test_vacancy_salary_validation_dict():
    vacancy = Vacancy("Designer", "http://example.com", {"from": 60000}, "Graphic designer")
    assert vacancy.salary == 60000

def test_vacancy_salary_validation_none():
    vacancy = Vacancy("Intern", "http://example.com", None, "Internship")
    assert vacancy.salary == 0

def test_vacancy_str():
    vacancy = Vacancy("Tester", "http://example.com", 70000, "QA tester")
    expected_str = "Tester - 70000 руб.\nhttp://example.com\nОписание: QA tester\n"
    assert str(vacancy) == expected_str

def test_vacancy_comparison():
    vacancy1 = Vacancy("Junior Developer", "http://example.com", 50000, "Entry-level developer")
    vacancy2 = Vacancy("Senior Developer", "http://example.com", 150000, "Experienced developer")
    assert vacancy2 < vacancy1  # Senior Developer зарплата выше, поэтому он меньше в порядке обратного сравнения
from src.headhunterapi import HeadhunterAPI
from src.jsonvacancystorage import JSONVacancyStorage
from src.vacancy import Vacancy


def main():
    """Функция - точка входа в программу"""
    job_title = input("Введите название вакансии: ")
    top_vacancy = int(
        input("Введите сколько вакансий, отсортированных по зарплате вам нужно: ")
    )

    hh_api = HeadhunterAPI()
    raw_vacancies = hh_api.get_vacancies(job_title, top_vacancy)
    storage = JSONVacancyStorage("sample.json")

    vacancies = []

    for item in raw_vacancies:
        vac_obj = Vacancy(
            item["name"], item["alternate_url"], item["salary"], item["snippet"]
        )
        vacancies.append(vac_obj)

    sorted_vacancies = sorted(vacancies)
    storage.save_to_file(sorted_vacancies)

    for i in sorted_vacancies:
        print(i.__dict__)


if __name__ == "__main__":
    main()
